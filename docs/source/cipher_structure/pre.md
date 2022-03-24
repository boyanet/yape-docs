# 代理重加密和代理重签名

代理重加密是一种基于公钥加密体系的密码学方案。在代理重加密中，基于授权人公钥加密的密文可以被转换为另一种密文，且保持对应明文不变，被转换后的密文可以由被授权人的私钥进行解密。该密文转换过程由一个半可信的第三方代理执行，在执行该过程前，代理需要持有一个由授权人到被授权人的转换密钥，该转换密钥一般由授权人事先生成并交给代理。同时在密文转换的整个过程中，代理者无法获取关于该密文对应明文的任何信息。这一方案使得数据拥有着可以将加密后的数据存放在云计算服务商等中间机构中，并在需要时允许其他用户下载并解密。

类似地，代理重签名允许第三方半可信代理使用一个重签名转换密钥，将授权人的签名转换为被授权人在同一消息上的签名，但代理并不能伪装为任何一方对任何消息产生合法的签名。

代理重加密功能通过基于预编译合约的Solidity Library实现。

```solidity
pragma solidity >=0.8;

contract Precompiles {
    function callSM9Pairing(bytes memory input) public returns (bytes32 result) {
        // input is a serialized bytes stream of (a1, b1, a2, b2, ..., ak, bk) from (G_1 x G_2)^k
        uint256 len = input.length;
        require(len % 192 == 0);
        assembly {
            let memPtr := mload(0x40)
            let success := call(gas, 0x08, 0, add(input, 0x20), len, memPtr, 0x20)
            switch success
            case 0 {
                revert(0,0)
            } default {
                result := mload(memPtr)
            }
        }
    }
}
```

