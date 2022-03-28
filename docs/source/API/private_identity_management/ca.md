# 身份认证节点

## 对外RPC接口

### register(c: String, user_info: String)

接收用户身份注册请求，如果成功，发送盲签名给用户

### get_user_info(c: String)

查询用户的身份信息

## 内部接口

### gen_cert(c: String, user_info: String)

* 记录用户身份信息（c与user_info的键值对）
* 生成盲签名
* 更新Merkle Tree并在链上更新Merkle root

### revoke(c: String, user_address: Address)

在链上揭示用户的身份信息
