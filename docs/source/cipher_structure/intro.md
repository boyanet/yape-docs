# 概述

博雅正链EVM虚拟机的一些功能特性是通过系统合约或预编译合约(Pre-compiled Contracts)体现的，随着博雅正链的升级，系统合约也会增加。

YAPE预编译合约地址如下：

| 合约名称     | 地址   | 描述                 |
| ------------ | ------ | -------------------- |
| SM3          | 0x2001 | 计算SM3哈希          |
| SM2RECOVER   | 0x2002 | SM2数字签名验签      |
| SM2CIPHERADD | 0x2003 | SM2密文同态加法      |
| PAILLIERADD  | 0x2007 | Paillier密文同态加法 |
| SM9ADD       | 0x2004 | SM9点加              |
| SM9MUL       | 0x2005 | SM9点乘              |
| SM9PAIRING   | 0x2006 | SM9双线性对计算      |
