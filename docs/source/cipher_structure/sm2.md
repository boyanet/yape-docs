# SM2数字签名算法验签

GMSSL预编译合约的地址为：0x1000 - 0x10FF，总共预留了256个，sm2-verify 地址为 0x1002。0x0000 - 0x00FF reserved for ETH precompiles.

SM2是国密椭圆曲线密码标准，其中包括加密、签名和密钥交换协议，SM2标准默认使用一个256比特的素域曲线参数。SM2RECOVER在功能上类似于以太坊的ECRECOVER预编译合约，SM2RECOVER预编译可以用于验证标准的SM2签名或以太坊EIP风格的SM2签名。
本文写作时Solidity编译器还不支持SM2RECOVER预编译合约，因此在编写合约时需要通过内联汇编(Inline Assembly)来调用SM2RECOVER合约。
下面给出调用SM2RECOVER预编译合约的合约代码例子：

```solidity
pragma solidity >=0.8;

contract SysContracts {
    
    function sm2verify(string memory spk, bytes memory sig, string memory sdata) public view returns (uint8){
       	//0-2, public key type, default pem
        //2, public key len
        //3, sig len
        //4-?, public key
        //?-?, sig
        //?-?, data

        //gas estimatie 156543

        //example
        /*
        ins.sm2verify("-----BEGIN PUBLIC KEY-----\nMFkwEwYHKoZIzj0CAQYIKoEcz1UBgi0DQgAESqZ8l4sMcyjURbwsPpyw6cFKaMGw\nmIEBwVpMJkr+PB6C7ADq5NBERXQKdjzeNSweTXmVM5J4JZmZFC6MhuPrIg==\n-----END PUBLIC KEY-----","0x3045022063CA1B61FE5CA093D11297722AC9555BF7CDED24B17C66FF567C9B9F7A94364C022100BBF90EED502DB7A9B18256F552E3B3E97391B38F27BB993662CEA7E596478914","The Go appserver can access an array created by the C++ library")
        */


        bytes memory pk = bytes(spk);
        bytes memory data = bytes(sdata);

        uint8 pklen = uint8(pk.length);
        uint8 siglen = uint8(sig.length);
        uint32 datalen = uint32(data.length);

        bytes memory input = new bytes(pklen + siglen + datalen + 4);
        
        uint32 i;
        input[2] = bytes1(pklen);
        input[3] = bytes1(siglen);

        uint32 offset = 4;
        for(i=0;i<pklen;i++) input[offset+i] = pk[i];

        offset+= pklen;
        for(i=0;i<siglen;i++) input[offset+i] = sig[i];

        offset+= siglen;
        for(i=0;i<datalen;i++) input[offset+i] = data[i];

        bytes1[1] memory ret;
        assembly{
            if iszero(
                staticcall(100000, 0x0102, add(input, 32) , mload(input), ret, 1)
            ) {
                invalid()
            }
        }
        //ret = 0: verification successful, ret = 1: verification failed
        return uint8(ret[0]);
    }
}
```
### 合约调用示例
```
ins.sm2verify(
    "-----BEGIN PUBLIC KEY-----\nMFkwEwYHKoZIzj0CAQYIKoEcz1UBgi0DQgAESqZ8l4sMcyjURbwsPpyw6cFKaMGw\nmIEBwVpMJkr+PB6C7ADq5NBERXQKdjzeNSweTXmVM5J4JZmZFC6MhuPrIg==\n-----END PUBLIC KEY-----",
"0x3045022063CA1B61FE5CA093D11297722AC9555BF7CDED24B17C66FF567C9B9F7A94364C022100BBF90EED502DB7A9B18256F552E3B3E97391B38F27BB993662CEA7E596478914", 
"The Go appserver can access an array created by the C++ library")

Result: 0 (success)
```