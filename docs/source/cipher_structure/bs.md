# 盲签名验证

盲签名是一种特殊的具有隐私保护功能的签名，签名者可以在不暴露消息内容的同时获得有效的签名值。博雅链EVM支持盲签名验签预编译合约。下面给出调用盲签名验签预编译合约的合约代码例子：

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
