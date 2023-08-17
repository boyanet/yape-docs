# SM9标识密码算法

GMSSL预编译合约的地址为：0x1000 - 0x10FF，总共预留了256个，sm9 地址为 0x0109 - 0x0111。0x0000 - 0x00FF reserved for ETH precompiles.

SM9是国密标识密码算法标准，其中包括标识加密、标识签名和标识密钥交换协议，SM9标准中还包括一个推荐的BN曲线参数。博雅链EVM中增加了针对SM9曲线的椭圆曲线算术运算操作，合约可以通过调用椭圆曲线算法运算实现零知识证明、秘密共享、同态加密等上层密码方案。

## SM9ADD - 0x0109

SM9Add预编译合约实现SM9椭圆曲线点的点加操作，其输入是两个椭圆曲线点的仿射坐标，输出是两个结果点的仿射坐标。本文写作时Solidity编译器还不支持SM9Add预编译合约，因此在编写合约时需要通过内联汇编(Inline Assembly)来调用SM9Add合约。下面给出调用SM9Add预编译合约的合约代码例子：

```solidity
pragma solidity >=0.8.1;

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

## SM9MUL - 0x0110

SM9Mul预编译合约实现SM9椭圆曲线点的标量乘法操作，其输入是一个曲线点的仿射坐标和一个`uint256`整数表示的标量，输出是两个点乘操作的结果，点的仿射坐标。本文写作时Solidity编译器还不支持SM9Mul预编译合约，因此在编写合约时需要通过内联汇编(Inline Assembly)来调用SM9Mul合约。下面给出调用SM9Mul预编译合约的合约代码例子：

```solidity
pragma solidity >=0.8.1;

contract Precompiles {
    function sm9mul(string memory x, string memory y, string memory iv) public view returns (string memory , string memory ){
        bytes memory input = new bytes(192);
        uint32 i;
        uint32 offset =0;

        bytes memory bx = bytes(x);
        bytes memory by = bytes(y);
        bytes memory biv = bytes(iv);

        //input
        //0-64 x
        //64-128 y
        //128-192 iv

        for(i=0;i<64;i++) input[offset+i] = bx[i]; offset +=64;
        for(i=0;i<64;i++) input[offset+i] = by[i]; offset +=64;
        for(i=0;i<64;i++) input[offset+i] = biv[i]; 
        
        bytes32[4] memory ret32;

        assembly{
            if iszero(
                staticcall(100000, 0x0110, add(input, 32) , mload(input), ret32, 128)
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
ins.sm9mul("917be49d159184fba140f4dfc5d653464e94f718fe195b226b3f715829e6e768", "288578d9505d462867a50acee40ee143b896e72505be10e8ce4c6b0c945b642b", "123456789abcdef00fedcba987654321123456789abcdef00fedcba987654321")
Result {
  '0': '997fcff625adbae62566f684f9e89181713f972c5a9cd9ce6764636761ba87d1',
  '1': '8142a28d1bd109501452a649e2d68f012e265460e0c7d3da743fb036eb23b03b'
}
```

## SM9PAIRING - 0x0111

SM9Pairing预编译合约实现SM9曲线参数上的双线性对(Pairing)操作，可以用于零知识证明等复杂密码方案。本文写作时Solidity编译器还不支持SM9Pairing预编译合约，因此在编写合约时需要通过内联汇编(Inline Assembly)来调用SM9Pairing合约。下面给出调用SM9Pairing预编译合约的合约代码例子：

```solidity
pragma solidity >=0.8.1;

contract Precompiles {
    function sm9pairing(string memory px, string memory py,string memory twistpx, string memory twistpy) public view returns (bytes32[24] memory ){
        bytes memory input = new bytes(384);
        uint32 i;
        uint32 offset =0;

        bytes memory bx1 = bytes(px);
        bytes memory by1 = bytes(py);
        bytes memory bx2 = bytes(twistpx);
        bytes memory by2 = bytes(twistpy);

        for(i=0;i<64;i++) input[offset+i] = bx1[i]; offset +=64;
        for(i=0;i<64;i++) input[offset+i] = by1[i]; offset +=64;
        for(i=0;i<128;i++) input[offset+i] = bx2[i]; offset +=128;
        for(i=0;i<128;i++) input[offset+i] = by2[i]; 
        bytes32[24] memory ret;

        assembly{
            if iszero(
                staticcall(100000, 0x0111, add(input, 32) , mload(input), ret, 768)
            ) {
                invalid()
            }
        }
        
        return ret;
    }
}
```

### 合约调用示例
```
ins.sm9pairing(
    "7CBA5B19069EE66AA79D490413D11846B9BA76DD22567F809CF23B6D964BB265", "A9760C99CB6F706343FED05637085864958D6C90902ABA7D405FBEDF7B781599", "74CCC3AC9C383C60AF083972B96D05C75F12C8907D128A17ADAFBAB8C5A4ACF701092FF4DE89362670C21711B6DBE52DCD5F8E40C6654B3DECE573C2AB3D29B2","44B0294AA04290E1524FF3E3DA8CFD432BB64DE3A8040B5B88D1B5FC86A4EBC18CFC48FB4FF37F1E27727464F3C34E2153861AD08E972D1625FC1A7BD18D5539")
Result {
    "4e378fb5561cd0668f906b731ac58fee25738edf09cadc7a29c0abc0177aea6d"
	"28b3404a61908f5d6198815c99af1990c8af38655930058c28c21bb539ce0000"
	"38bffe40a22d529a0c66124b2c308dac9229912656f62b4facfced408e02380f"
	"a01f2c8bee81769609462c69c96aa923fd863e209d3ce26dd889b55e2e3873db"
	"67e0e0c2eed7a6993dce28fe9aa2ef56834307860839677f96685f2b44d0911f"
	"5a1ae172102efd95df7338dbc577c66d8d6c15e0a0158c7507228efb078f42a6"
	"1604a3fcfa9783e667ce9fcb1062c2a5c6685c316dda62de0548baa6ba30038b"
	"93634f44fa13af76169f3cc8fbea880adaff8475d5fd28a75deb83c44362b439"
	"b3129a75d31d17194675a1bc56947920898fbf390a5bf5d931ce6cbb3340f66d"
	"4c744e69c4a2e1c8ed72f796d151a17ce2325b943260fc460b9f73cb57c9014b"
	"84b87422330d7936eaba1109fa5a7a7181ee16f2438b0aeb2f38fd5f7554e57a"
	"aab9f06a4eeba4323a7833db202e4e35639d93fa3305af73f0f071d7d284fcfb"
}
```


#define px, py \
	"7CBA5B19069EE66AA79D490413D11846B9BA76DD22567F809CF23B6D964BB265\n" \
	"A9760C99CB6F706343FED05637085864958D6C90902ABA7D405FBEDF7B781599"
#define twistpx twistpy \
	"74CCC3AC9C383C60AF083972B96D05C75F12C8907D128A17ADAFBAB8C5A4ACF7\n" \
	"01092FF4DE89362670C21711B6DBE52DCD5F8E40C6654B3DECE573C2AB3D29B2\n" \
	"44B0294AA04290E1524FF3E3DA8CFD432BB64DE3A8040B5B88D1B5FC86A4EBC1\n" \
	"8CFC48FB4FF37F1E27727464F3C34E2153861AD08E972D1625FC1A7BD18D5539"

	

#define r \
	"4e378fb5561cd0668f906b731ac58fee25738edf09cadc7a29c0abc0177aea6d\n" \
	"28b3404a61908f5d6198815c99af1990c8af38655930058c28c21bb539ce0000\n" \
	"38bffe40a22d529a0c66124b2c308dac9229912656f62b4facfced408e02380f\n" \
	"a01f2c8bee81769609462c69c96aa923fd863e209d3ce26dd889b55e2e3873db\n" \
	"67e0e0c2eed7a6993dce28fe9aa2ef56834307860839677f96685f2b44d0911f\n" \
	"5a1ae172102efd95df7338dbc577c66d8d6c15e0a0158c7507228efb078f42a6\n" \
	"1604a3fcfa9783e667ce9fcb1062c2a5c6685c316dda62de0548baa6ba30038b\n" \
	"93634f44fa13af76169f3cc8fbea880adaff8475d5fd28a75deb83c44362b439\n" \
	"b3129a75d31d17194675a1bc56947920898fbf390a5bf5d931ce6cbb3340f66d\n" \
	"4c744e69c4a2e1c8ed72f796d151a17ce2325b943260fc460b9f73cb57c9014b\n" \
	"84b87422330d7936eaba1109fa5a7a7181ee16f2438b0aeb2f38fd5f7554e57a\n" \
	"aab9f06a4eeba4323a7833db202e4e35639d93fa3305af73f0f071d7d284fcfb"