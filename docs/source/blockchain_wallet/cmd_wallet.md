# 命令行全节点客户端（boyanetool）

​博雅正链测试网络使用boyanetool作为命令行工具，来启动区块链网络、与其他客户建立p2p通信信道、签署和广播交易、挖掘，部署和与智能合约交互等。该工具由golang语言编写，需要完整的go语言编译与执行环境。

​		boyanetool主要由初始化、账号管理、区块数据文件管理、交互终端（JavaScript）以及关键系统参数命令组成。初始化主要完成创世节点的配置工作，在指定创世文件后，该命令能够在指定的文件夹内创建创世区块；账号管理负责生成、导入、更新和展示区块链网络中的账户；区块数据文件管理主要对存储与本地的区块数据进行读取、导入、导出等操作；交互终端是boyanetool的重要命令，通过javescript环境的API接口来与区块链节点进行通信，完成区块信息查询与交易的签名、部署等；关键系统参数主要用来规制区块链网络工作节点的具体特性和行为。

要加入boyanetool网络，首先要初始化创世节点。在创世节点配置文件中配置好链ID，gaslimit,初始代币分配等，就可以进行初始化了。

```
boyanetool init --datadir data genesis.json
```

​		完成初始化后，我们就可以加入网络了。为了更顺利的加入网络，我们可以指定启动节点。节点运行的方式有3种：全节点、轻节点和快照模式。

```
boyanetool --datadir data --networkid 15 --gcmode full --bootnodes enode://6c213a1332c861e9b651c52f42da79b2efbc0b99b90101a15c1aec53afa6492a6df87494fe540702687f960b91a93cfb7a2d055081658769cf8cb1bd8dd5efdf@8.142.139.142:0?discport=30301
```

​为了能使节点对外提供服务，我们可以指定API地址、端口和具体功能。提供服务的方式有两种：http和ws。

```
boyanetool --http --http.port 8545 --http.addr 172.25.101.59 --http.api debug,net,eth,shh,web3,txpool,personal --ws --ws.port 8546 --ws.addr 172.25.101.59 --ws.api eth,net,web3,network,debug,txpool,personal
```

​当然，为了方便交易，或者挖矿，我们可以在节点启动的时候就对账户进行解锁。

```
boyanetool --allow-insecure-unlock --unlock 0x13b21840D8f478b18aA337D5248a115Ce065E1AE --password password --mine
```

​下面是boyanetool的详细帮助信息：

```
NAME:
   boyanetool - the boyanet command line interface

USAGE:
   boyanetool [options] [command] [command options] [arguments...]

COMMANDS:
   account                            Manage accounts
   attach                             Start an interactive JavaScript environment (connect to node)
   console                            Start an interactive JavaScript environment
   db                                 Low level database operations
   dump                               Dump a specific block from storage
   dumpconfig                         Show configuration values
   dumpgenesis                        Dumps genesis block JSON configuration to stdout
   export                             Export blockchain into file
   export-preimages                   Export the preimage database into an RLP stream
   import                             Import a blockchain file
   import-preimages                   Import the preimage database from an RLP stream
   init                               Bootstrap and initialize a new genesis block
   js                                 Execute the specified JavaScript files
   license                            Display license information
   removedb                           Remove blockchain and state databases
   snapshot                           A set of commands based on the snapshot
   version                            Print version numbers
   wallet                             Manage presale wallets
   help, h                            Shows a list of commands or help for one command

BOYANET OPTIONS:
  --config value                      TOML configuration file
  --datadir value                     Data directory for the databases and keystore
  --datadir.ancient value             Data directory for ancient chain segments (default = inside chaindata)
  --datadir.minfreedisk value         Minimum free disk space in MB, once reached triggers auto shut down (default = --cache.gc converted to MB, 0 = disabled)
  --keystore value                    Directory for the keystore (default = inside the datadir)
  --usb                               Enable monitoring and management of USB hardware wallets
  --pcscdpath value                   Path to the smartcard daemon (pcscd) socket file (default: "/run/pcscd/pcscd.comm")
  --networkid value                   Explicitly set network id (integer)(For testnets: use --ropsten, --rinkeby, --goerli instead) (default: 1)
  --syncmode value                    Blockchain sync mode ("snap", "full" or "light") (default: snap)
  --exitwhensynced                    Exits after block synchronisation completes
  --gcmode value                      Blockchain garbage collection mode ("full", "archive") (default: "full")
  --txlookuplimit value               Number of recent blocks to maintain transactions index for (default = about one year, 0 = entire chain) (default: 2350000)
  --identity value                    Custom node name
  --lightkdf                          Reduce key-derivation RAM & CPU usage at some expense of KDF strength


ACCOUNT OPTIONS:
  --unlock value                      Comma separated list of accounts to unlock
  --password value                    Password file to use for non-interactive password input
  --signer value                      External signer (url or path to ipc file)
  --allow-insecure-unlock             Allow insecure account unlocking when account-related RPCs are exposed by http

API AND CONSOLE OPTIONS:
  --ipcdisable                        Disable the IPC-RPC server
  --ipcpath value                     Filename for IPC socket/pipe within the datadir (explicit paths escape it)
  --http                              Enable the HTTP-RPC server
  --http.addr value                   HTTP-RPC server listening interface (default: "localhost")
  --http.port value                   HTTP-RPC server listening port (default: 8545)
  --http.api value                    API's offered over the HTTP-RPC interface
  --http.rpcprefix value              HTTP path path prefix on which JSON-RPC is served. Use '/' to serve on all paths.
  --http.corsdomain value             Comma separated list of domains from which to accept cross origin requests (browser enforced)
  --http.vhosts value                 Comma separated list of virtual hostnames from which to accept requests (server enforced). Accepts '*' wildcard. (default: "localhost")
  --ws                                Enable the WS-RPC server
  --ws.addr value                     WS-RPC server listening interface (default: "localhost")
  --ws.port value                     WS-RPC server listening port (default: 8546)
  --ws.api value                      API's offered over the WS-RPC interface
  --ws.rpcprefix value                HTTP path prefix on which JSON-RPC is served. Use '/' to serve on all paths.
  --ws.origins value                  Origins from which to accept websockets requests
  --authrpc.jwtsecret value           Path to a JWT secret to use for authenticated RPC endpoints
  --authrpc.addr value                Listening address for authenticated APIs (default: "localhost")
  --authrpc.port value                Listening port for authenticated APIs (default: 8551)
  --authrpc.vhosts value              Comma separated list of virtual hostnames from which to accept requests (server enforced). Accepts '*' wildcard. (default: "localhost")
  --graphql                           Enable GraphQL on the HTTP-RPC server. Note that GraphQL can only be started if an HTTP server is started as well.
  --graphql.corsdomain value          Comma separated list of domains from which to accept cross origin requests (browser enforced)
  --graphql.vhosts value              Comma separated list of virtual hostnames from which to accept requests (server enforced). Accepts '*' wildcard. (default: "localhost")
  --rpc.allow-unprotected-txs         Allow for unprotected (non EIP155 signed) transactions to be submitted via RPC
  --jspath loadScript                 JavaScript root path for loadScript (default: ".")
  --exec value                        Execute JavaScript statement
  --preload value                     Comma separated list of JavaScript files to preload into the console

NETWORKING OPTIONS:
  --bootnodes value                   Comma separated enode URLs for P2P discovery bootstrap
  --discovery.dns value               Sets DNS discovery entry points (use "" to disable DNS)
  --port value                        Network listening port (default: 30303)
  --maxpeers value                    Maximum number of network peers (network disabled if set to 0) (default: 50)
  --maxpendpeers value                Maximum number of pending connection attempts (defaults used if set to 0) (default: 0)
  --nat value                         NAT port mapping mechanism (any|none|upnp|pmp|extip:<IP>) (default: "any")
  --nodiscover                        Disables the peer discovery mechanism (manual peer addition)
  --v5disc                            Enables the experimental RLPx V5 (Topic Discovery) mechanism
  --netrestrict value                 Restricts network communication to the given IP networks (CIDR masks)
  --nodekey value                     P2P node key file
  --nodekeyhex value                  P2P node key as hex (for testing)

MINER OPTIONS:
  --mine                              Enable mining
  --miner.threads value               Number of CPU threads to use for mining (default: 0)
  --miner.notify value                Comma separated HTTP URL list to notify of new work packages
  --miner.notify.full                 Notify with pending block headers instead of work packages
  --miner.gasprice value              Minimum gas price for mining a transaction (default: 1000000000)
  --miner.gaslimit value              Target gas ceiling for mined blocks (default: 30000000)
  --miner.base value             Public address for block mining rewards (default = first account) (default: "0")
  --miner.extradata value             Block extra data set by the miner (default = client version)
  --miner.recommit value              Time interval to recreate the block being mined (default: 3s)
  --miner.noverify                    Disable remote sealing verification

MISC OPTIONS:
  --help, -h                                show help

```

