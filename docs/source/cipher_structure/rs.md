# 环签名验证

环签名是一种支持隐私保护的数字签名方案。常规的签名方案，如SM2签名和ECDSA签名，签名方的地址可以通过签名值导出，无法实现签名的匿名性。在环签名方案中，验证方仅能够验证一个有效的签名来自一个群组中的某个成员，但是无法获得确切的签名方身份信息。环签名用于需要身份匿名和隐私保护的场景，如投票、拍卖等。

YAPE支持SM2环签名算法，其中预编译合约(SM2RingVerify)仅完成环签名验证功能，环签名的生成需要通过调用YAPE SDK完成。

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
