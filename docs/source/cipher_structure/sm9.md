# SM9标识密码算法

SM9是国密标识密码算法标准，其中包括标识加密、标识签名和标识密钥交换协议，SM9标准中还包括一个推荐的BN曲线参数。博雅正链EVM中增加了针对SM9曲线的椭圆曲线算术运算操作，合约可以通过调用椭圆曲线算法运算实现零知识证明、秘密共享、同态加密等上层密码方案。

## SM9ADD

SM9Add预编译合约实现SM9椭圆曲线点的点加操作，其输入是两个椭圆曲线点的仿射坐标，输出是两个结果点的仿射坐标。本文写作时Solidity编译器还不支持SM9Add预编译合约，因此在编写合约时需要通过内联汇编(Inline Assembly)来调用SM9Add合约。下面给出调用SM9Add预编译合约的合约代码例子：

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

### SM9MUL

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

### SM9PAIRING

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
