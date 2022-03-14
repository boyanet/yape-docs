# 国密算法

## SM2数字签名算法

SM2数字签名算法是由中国国家密码管理局公布的中国密码行业标准《SM2椭圆曲线公钥密码算法》的一部分，规定了数字签名生成算法和验证算法，适用于商用密码应用中的数字签名与验证，可满足多种密码应用中的身份认证和数据完整性、真实性的安全需求。同时，还可为安全产品生产商提供产品和技术的标准定位以及标准化的参考，提高安全产品的可信性与互操作性。

本框架实现了SM2数字签名算法中签名验证、从签名恢复公钥功能的智能合约实现，用于在链上提供签名验证平台。

## SM3哈希算法

哈希函数是一类用途广泛的基础密码算法，其基本用途为计算任意长度数据的摘要值（哈希值），保证数据完整性。此外，哈希函数还是数字签名、消息认证码等众多密码方案、安全协议的基本组成部分。

SM3哈希算法是由中国国家密码管理局公布的中国密码行业标准，用于在商用领域中取代SHA-1、SHA-2等国外算法，同时也是SM2公钥密码算法、SSL VPN协议等商用密码标准中的关键组成部分。

本框架实现了SM3算法的智能合约实现，用于在链上高效地计算数据摘要或配合其他密码算法使用。