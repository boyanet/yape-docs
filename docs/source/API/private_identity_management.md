# 隐私身份管理

## 身份认证节点

### 对外RPC接口

#### register(c: String, user_info: String)

接收用户身份注册请求，如果成功，发送盲签名给用户

#### get_user_info(c: String)

查询用户的身份信息

### 内部接口

#### gen_cert(c: String, user_info: String)

* 记录用户身份信息（c与user_info的键值对）
* 生成盲签名
* 更新Merkle Tree并在链上更新Merkle root

#### revoke(c: String, user_address: Address)

在链上揭示用户的身份信息

## 委员会节点

### 对外RPC接口

#### verify_cert(address: Address, secret: String)

* 接收秘密分享
* 验证秘密分享的正确性

### 内部接口

#### revoke(address: Address, tx_hash: H256)

* 监控event，收到revoke请求后进行恢复身份操作
* 验证tx_hash对应的交易是否存在违规行为（暂时不需要实现）
* 将秘密分享片段上传到身份合约

## 用户注册节点

### 对外RPC接口

#### register(addr: Address, user_info: String)

返回值为注册结果

### 内部函数

#### apply_cert(addr: Address, user_info: String)

对address 进行盲化，向认证节点申请盲签名证书（发送RPC请求）

#### request_verify(addr: Address, cert: String)

* 对盲签名证书进行去盲，得到证书
* 对盲化因子进行秘密分享并生成证明
* 对秘密分享的值做零知识证明
* 跟合约进行交互，发送验证请求（发送证书、address、零知识证明、秘密分享证明）
* 发送秘密分享的值及合约的request id给各个委员会节点

#### revoke(addr: Address)

跟合约交互，撤销掉该身份

#### is_ok(addr: Address)

查询用户地址是否注册
