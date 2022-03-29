身份管理服务的Identity合约：

```solidity
// SPDX-License-Identifier: GPL-3.0
pragma solidity >=0.7.0 <0.9.0;

import "@openzeppelin/contracts/access/Ownable.sol";

contract Identity is Ownable {

    struct User{
        uint256 s;
        uint256 r;
        int n;
        string proof1;
        string proof2;
        uint256 register_status;//0:not registered, 1:deleted, 2:in
        uint256 register_time;
        uint256 approval_num;
        mapping(address => bool) approval_from_committee;
    }

    struct CA{
        address addr;
        uint256 pubkey_x;
        uint256 pubkey_y;
    }

    //struct for user_info
    struct sub_Info{
        address addr;
        uint256 tx_hash;
        string[] sec_list;
        mapping(address => bool) approval_from_committee;
        string info;
    }

    CA public ca;
    mapping(address => User) public users;
    mapping(address => bool) public user_list;//the list for users in status: 1,2
    mapping(address => bool) public committee;

    uint256 public min_approval_num = 2;

    uint256 apply_reveal_num = 0;
    mapping(uint256 => sub_Info) public user_info;

    uint256[] public root_list;

    event reveal(uint256 apply_id);

    function set_ca(address ca_addr, uint256 pubkey_x, uint256 pubkey_y) public onlyOwner {
        ca.addr = ca_addr;
        ca.pubkey_x = pubkey_x;
        ca.pubkey_y = pubkey_y;
    }
 
    function add_committee(address addr) public onlyOwner {
        committee[addr] = true;
    }

    function remove_committee(address addr) public onlyOwner {
        committee[addr] = false;
    }

    function set_num(uint256 n) public onlyOwner {
        min_approval_num = n;
    }

    function update_root(uint256 root) public onlyOwner {
        root_list.push(root);
    }

    function register(uint256 s, uint256 r, int n, string  calldata proof1, string calldata proof2) public{
        User storage u = users[msg.sender];
        u.s = s;
        u.r = r;
        u.n = n;
        u.proof1 = proof1;
        u.proof2 = proof2;
    }

    function approve_register(address addr) public{
        require(committee[msg.sender], "Only member of committee can call this");
        require(!users[addr].approval_from_committee[msg.sender], "Each member of committee can only approve of each user_register once.");
        
        users[addr].approval_num += 1;
        users[addr].approval_from_committee[msg.sender] = true;
        
        if(users[addr].approval_num >= min_approval_num){
            users[addr].register_status = 2;
            users[addr].register_time = block.timestamp;
            user_list[addr] = true;
        }
    }

    function check(address addr) public view returns (uint){
        if(!user_list[addr]){
            return 0;
        }
        else if(users[addr].register_status == 2){
            return users[addr].register_time;
        }
        else{
            return 1;
        }
    }

    function apply_reveal(address addr, uint256 tx_hash) public returns (uint){
        apply_reveal_num += 1;
        sub_Info storage si = user_info[apply_reveal_num];
        si.addr = addr;
        si.tx_hash = tx_hash;
        return apply_reveal_num;
    }

    function agree_reveal(uint256 apply_id, string calldata sec) public{
        require(committee[msg.sender], "Only member of committee can call this");
        require(!user_info[apply_id].approval_from_committee[msg.sender], "Each member of committee can only approve of each user_info once.");
        
        user_info[apply_id].sec_list.push(sec);
        user_info[apply_id].approval_from_committee[msg.sender] = true;
        
        if(user_info[apply_id].sec_list.length >= min_approval_num){
            emit reveal(apply_id);
        }
    }

    function do_reveal(uint256 apply_id, string calldata info) public{
        require(msg.sender == ca.addr, "Only CA can call this.");
        
        user_info[apply_id].info = info;
    }

}
```



下面我们基于身份管理服务实现一个身份验证的例子：

- 注册user地址：0x78731D3Ca6b7E34aC0F824c42a7cC18A495cabaB，注册时间：1648530833。
- 未注册user地址：0x617F2E2fD72FD9D5503197092aC168c91465E7f2。

Identity_test合约：

```solidity
// SPDX-License-Identifier: GPL-3.0
pragma solidity >=0.7.0 <0.9.0;

contract Identity_test{
    
    address registered_user = 0x78731D3Ca6b7E34aC0F824c42a7cC18A495cabaB;
    address unregistered_user = 0x617F2E2fD72FD9D5503197092aC168c91465E7f2;

    function test(address Identity_contract_addr) public returns (uint256, uint256){
        (bool success1, bytes memory bytes_result_registered_user) = Identity_contract_addr.call(abi.encodeWithSignature("check(address)", registered_user));
        require(success1, "failed");
        (bool success2, bytes memory bytes_result_unregistered_user) = Identity_contract_addr.call(abi.encodeWithSignature("check(address)", unregistered_user));
        require(success2, "failed");

        uint256 result_registered_user = bytesToUint(bytes_result_registered_user);
        uint256 result_unregistered_user = bytesToUint(bytes_result_unregistered_user);

        return (result_registered_user, result_unregistered_user);
    }

    function bytesToUint(bytes memory b) public pure returns (uint256){
        
        uint256 number;
        for(uint i = 0; i < b.length; i++){
            number = number + uint8(b[i])*(2**(8*(b.length - (i + 1))));
        }
        return number;
    }

}
```

- 部署Identity_test合约，并调用test函数，得到返回结果：
![eaabe66b1951535d15190e47b02ec34](https://user-images.githubusercontent.com/48012348/160555856-397aa600-9e7f-4f3f-8169-f37b3581fb00.png)


- 返回结果与用户实际注册状态一致。
