# 委员会节点

## 对外RPC接口

### verify_cert(address: Address, secret: String)

* 接收秘密分享
* 验证秘密分享的正确性

## 内部接口

### revoke(address: Address, tx_hash: H256)

* 监控event，收到revoke请求后进行恢复身份操作
* 验证tx_hash对应的交易是否存在违规行为（暂时不需要实现）
* 将秘密分享片段上传到身份合约
