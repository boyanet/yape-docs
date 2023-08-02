# SM9标识密码算法

GMSSL预编译合约的地址为：0x1000 - 0x10FF，总共预留了256个，sm9 地址为 0x0109 - 0x0111。0x0000 - 0x00FF reserved for ETH precompiles.

SM9是国密标识密码算法标准，其中包括标识加密、标识签名和标识密钥交换协议，SM9标准中还包括一个推荐的BN曲线参数。博雅链EVM中增加了针对SM9曲线的椭圆曲线算术运算操作，合约可以通过调用椭圆曲线算法运算实现零知识证明、秘密共享、同态加密等上层密码方案。

## SM9ADD - 0x0109

SM9Add预编译合约实现SM9椭圆曲线点的点加操作，其输入是两个椭圆曲线点的仿射坐标，输出是两个结果点的仿射坐标。本文写作时Solidity编译器还不支持SM9Add预编译合约，因此在编写合约时需要通过内联汇编(Inline Assembly)来调用SM9Add合约。下面给出调用SM9Add预编译合约的合约代码例子：

```solidity
pragma solidity >=0.4.21;

contract Precompiles {
    function sm9add(string memory x1, string memory y1, string memory x2, string memory y2) public view returns (string memory x, string memory y){
        bytes memory input = new bytes(256);
        uint32 i;
        uint32 offset =0;

        bytes memory bx1 = bytes(x1);
        bytes memory by1 = bytes(y1);
        bytes memory bx2 = bytes(x2);
        bytes memory by2 = bytes(y2);

        //input
        //0-64 x1
        //64-128 y1
        //128-192 x2
        //192-256 y2
        for(i=0;i<64;i++) input[offset+i] = bx1[i]; offset +=64;
        for(i=0;i<64;i++) input[offset+i] = by1[i]; offset +=64;
        for(i=0;i<64;i++) input[offset+i] = bx2[i]; offset +=64;
        for(i=0;i<64;i++) input[offset+i] = by2[i];
        
        bytes32[4] memory ret32;

        assembly{
            if iszero(
                staticcall(100000, 0x0109, add(input, 32) , mload(input), ret32, 128)
            ) {
                invalid()
            }
        }

        bytes memory ret1 = abi.encodePacked(ret32);
        return (string(bytes_slice(ret1,0,64)),string(bytes_slice(ret1,64,128)));
    }
}
```

### 合约调用示例
```
ins.sm9add("917be49d159184fba140f4dfc5d653464e94f718fe195b226b3f715829e6e768", "288578d9505d462867a50acee40ee143b896e72505be10e8ce4c6b0c945b642b", "593417680f252445fd0522383e23c77a54b11fe222de4a886eabc26e16bffa3c", "38e8fc9a8b60f5ba0c6c411f721c117044435a833757d8fee65828511b8b245d")
Result {
  '0': '5e4ff71938d96a2569d289dc13d3129fcf3dbc13ad7ebc53941c6ca331d400cb',
  '1': '10002bca9f0e8aa073ad25456d75c57238f7eb1883d8df0a99af5f46fc45b501'
}
```

## SM9MUL

SM9Mul预编译合约实现SM9椭圆曲线点的标量乘法操作，其输入是一个曲线点的仿射坐标和一个`uint256`整数表示的标量，输出是两个点乘操作的结果，点的仿射坐标。本文写作时Solidity编译器还不支持SM9Mul预编译合约，因此在编写合约时需要通过内联汇编(Inline Assembly)来调用SM9Mul合约。下面给出调用SM9Mul预编译合约的合约代码例子：

```solidity
pragma solidity >=0.4.21;

contract Precompiles {
    function callBn256ScalarMul(bytes32 x, bytes32 y, bytes32 scalar) public returns (bytes32[2] memory result) {
        bytes32[3] memory input;
        input[0] = x;
        input[1] = y;
        input[2] = scalar;
        assembly {
            let success := call(gas, 0x07, 0, input, 0x60, result, 0x40)
            switch success
            case 0 {
                revert(0,0)
            }
        }
    }
}
```

## SM9PAIRING

SM9Pairing预编译合约实现SM9曲线参数上的双线性对(Pairing)操作，可以用于零知识证明等复杂密码方案。本文写作时Solidity编译器还不支持SM9Pairing预编译合约，因此在编写合约时需要通过内联汇编(Inline Assembly)来调用SM9Pairing合约。下面给出调用SM9Pairing预编译合约的合约代码例子：

```solidity
pragma solidity >=0.4.21;

contract Precompiles {
    function callBn256Pairing(bytes memory input) public returns (bytes32 result) {
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
