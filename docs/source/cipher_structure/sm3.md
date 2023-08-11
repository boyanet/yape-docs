# SM3哈希算法

GMSSL预编译合约的地址为：0x1000 - 0x10FF，总共预留了256个，sm3-hash 地址为 0x1003。0x0000 - 0x00FF reserved for ETH precompiles.

SM3哈希算法是国密密码杂凑算法标准，用于替代由美国NIST设计的SHA-1、SHA-256算法。SM3输出的哈希值长度和SHA-256一样，均为256比特（32字节或者64个十六进制字符），但是设计安全性比SHA-256更高。在标准的EVM虚拟机支持SHA-256预编译合约，博雅链EVM中增加了SM3算法的预编译合约。
本文写作时Solidity编译器还不支持SM3预编译合约，因此在编写合约时需要通过内联汇编(Inline Assembly)来调用SM3合约。下面给出调用SM3预编译合约的合约代码例子：

```solidity
pragma solidity >=0.8;

contract SysContracts {
	function sm3(string memory data) public view returns (bytes32){
        bytes32[1] memory h;
	    assembly{
            if iszero(
                staticcall(1000000, 0x0103, add(data, 32) , mload(data), h, 32)
            ) {
                invalid()
            }
        }
        return h[0];
    }
}
```

### 合约调用示例
```
ins.sm3("hello world")
Result: '0x44f0061e69fa6fdfc290c494654a05dc0c053da7e5c52b84ef93a9d67d3fff88'
```
