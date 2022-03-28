# 用户注册节点

## 对外RPC接口

### register(addr: Address, user_info: String)

返回值为注册结果

## 内部函数

### apply_cert(addr: Address, user_info: String)

对address 进行盲化，向认证节点申请盲签名证书（发送RPC请求）

### request_verify(addr: Address, cert: String)

* 对盲签名证书进行去盲，得到证书
* 对盲化因子进行秘密分享并生成证明
* 对秘密分享的值做零知识证明
* 跟合约进行交互，发送验证请求（发送证书、address、零知识证明、秘密分享证明）
* 发送秘密分享的值及合约的request id给各个委员会节点

### revoke(addr: Address)

跟合约交互，撤销掉该身份

### is_ok(addr: Address)

查询用户地址是否注册
