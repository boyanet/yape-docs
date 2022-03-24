# SM2数字签名算法验签

SM2是国密椭圆曲线密码标准，其中包括加密、签名和密钥交换协议，SM2标准默认使用一个256比特的素域曲线参数。SM2RECOVER在功能上类似于以太坊的ECRECOVER预编译合约，SM2RECOVER预编译可以用于验证标准的SM2签名或以太坊EIP风格的SM2签名。本文写作时Solidity编译器还不支持SM2RECOVER预编译合约，因此在编写合约时需要通过内联汇编(Inline Assembly)来调用SM2RECOVER合约。下面给出调用SM2RECOVER预编译合约的合约代码例子：

```solidity
pragma solidity >=0.8;

contract SysContracts {
    function sm3(bytes memory data) public view returns (bytes32) {
        bytes32[1] memory h;
        assembly {
            if iszero(
                staticcall(not(0), 0x400, add(data, 32), mload(data), h, 32)
            ) {
                invalid()
            }
        }
        return h[0];
    }
}
```
