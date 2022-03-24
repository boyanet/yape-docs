# 同态加密

同态加密是一种公钥加密算法，有别于常规的公钥加密算法，同态加密支持密文上的计算。YAPE通过预编译合约支持两种同态加密算法：SM2同态加密和Paillier同态加密。这两种算法在功能上相同，当整型数值加密并通过交易上链后，智能合约可以调用对应的预编译合约对密文进行加法计算并得到和的密文。注意，预编译合约的调用方应保证计算不会溢出。

同态加密的预编译合约仅完成密文加法计算功能，数值的加密和解密算法需要通过调用YAPE SDK完成。

下面给出调用SM2密文加法的预编译合约的合约代码例子：

```
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

下面给出调用Paillier密文加法的预编译合约的合约代码例子：

```
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
