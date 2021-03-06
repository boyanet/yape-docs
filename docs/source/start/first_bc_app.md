# 开发第一个区块链应用

这个实例主要针对没有区块链去中心化应用经验的开发者，这里我们以一个简化的存证应用为例，介绍如何在区块链上开发、部署一个完整的应用。注意，本实例不依赖EVM虚拟机中的YAPE扩展功能，因此这个例子应用也可以运行在其他区块链的EVM环境中。

典型的数据库Web应用主要包括前端界面、后端应用逻辑和数据库构成，其中前端界面主要由HTML/JavaScript实现，后端应用以Java/PHP/Python/Node等语言实现，数据库如MySQL通常运行在一个专用的服务器中，通过网络和后端应用所在的服务器连接。用户在访问一个数据库应用时，首先需要通过用户名和口令登录到应用系统中，用户的操作请求被后端应用逻辑转化为SQL查询请求，发送给数据库，数据库运行SQL查询后给应用端返回查询结果，最终通过浏览器将结果呈现给用户。基于区块链的去中心化应用(dApp)和数据库应用大体类似，区别在于，用户在登录应用时不使用口令登录，而是通过浏览器插件客户端以数字签名的方式进行高安全等级的认证，后端数据库被区块链取代，后端应用对数据库的SQL查询请求也被智能合约查询请求所取代。

下图显示了一个dApp的主要组成部分：浏览器插件客户端、前端和应用逻辑、智能合约。

下面给出具体的代码示例和开发过程，这个例子只依赖Remix开发环境、JavaScript/HTML代码编辑器和Yallet客户端。
