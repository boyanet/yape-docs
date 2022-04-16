YAPE区块链隐私计算框架
===================================

YAPE是面向区块链的数据安全共享和隐私计算的密码学框架，通过YAPE框架，区块链系统和应用的开发者可以实现基于区块链的流通过程中“数据可用不可见”的安全解决方案。YAPE框架采用安全多方计算、秘密分享、同态加密、零知识证明等密码学方案，基于YAPE框架的解决方案相对于基于联邦学习、可信执行环境等技术的方案，具有可证明安全的更高安全性，也具有不依赖特定型号的TEE硬件的广泛的适用性。

YAPE是一个进行安全数据共享、隐私信息数据交易和计算的通用平台，大幅降低区块链数据安全应用开发的商业门槛和技术门槛，使掌握Solidity智能合约和主流通用编程语言的开发者可以快速开发“数据可用不可见”的安全解决方案。

YAPE隐私执行框架主要包括EVM预编译合约、面向典型安全场景的可扩展密码组件合约、隐私数据交易市场合约、链下通用隐私执行环境和应用端SDK等组件构成。框架目前已经集成在博雅链测试网络中。



.. note::

   YAPE框架中的部分关键功能依赖于博雅链EVM虚拟机执行环境，开发者和用户需要检查YAPE框架的版本和EVM虚拟机的版本兼容性，具体参考 `[YAPE版本号] <https://yape.readthedocs.io>`_ 

.. container:: row 
   
   .. container:: card-holder
      
      .. container:: card rocket

         .. raw:: html

            <br>
            <h style="font-size: 22px;">快速开始</h>
            <br><br>
         
         - `关于博雅链公共测试网络 <./start/bon.html>`_
         - `通过Yallet客户端创建账户 <./blockchain_wallet/Yallet.html>`_
         - `开发第一个区块链应用 <./start/first_bc_app.html>`_
         - `通过YAPE框架开发一个数据安全应用 <./start/yape_app.html>`_


   .. container:: card-holder-bigger

         .. container:: tools 
         
            .. raw:: html
         
               <div class="tools-holder">
                  <br>
                  <h style="font-size: 18px;"><b><a href="./blockchain_wallet/Yallet.html">区块链浏览器</a></b></h>
                  <br><br>
                  <p>博雅链BON测试网络提供了区块链浏览器，即供用户浏览与查询区块链所有信息的Web应用。获得许可的用户也可以通过连接Yallet客户端向区块链中写入数据。</p>
               </div>
               <img src="./media/qukuailianliulanqi.jpg" class="card-holder" >
               <div style="clear:both"></div>

         .. raw:: html

            <hr>

         .. container:: tools 

            .. raw:: html
         
               <div class="tools-holder">
                  <br>
                  <h style="font-size: 18px;"><b><a href="./blockchain_wallet/Yallet.html">Yallet轻节点客户端</a></b></h>
                  <br><br>
                  <p>此处应有描述</p>
               </div>
               <img src="此处应有截图.png" class="card-holder" >
               <div style="clear:both"></div>

         .. raw:: html

            <hr>

         .. container:: tools 
         
            .. raw:: html
         
               <div class="tools-holder">
                  <br>
                  <h style="font-size: 18px;"><b><a href="./blockchain_wallet/Yallet.html">全节点客户端</a></b></h>
                  <br><br>
                  <p>全节点客户端是命令行工具。补充描述信息及界面截图</p>
               </div>
               <img src="此处应有截图.png" class="card-holder" >
               <div style="clear:both"></div>
               <br><br>

         .. raw:: html

            <hr>
            


.. toctree::
   :maxdepth: 2
   :caption: 入门
   :hidden:

   start/bon.md
   start/first_bc_app.md
   start/yape_app.md
   
.. toctree::
   :maxdepth: 2
   :caption: 区块链钱包
   :hidden:

   blockchain_wallet/Yallet.md
   blockchain_wallet/cmd_wallet.md
   
.. toctree::
   :maxdepth: 2
   :caption: 隐私执行环境
   :hidden:

   private_execute_environmnet.md
   cipher_structure/mpc.md
   cipher_structure/psi.md
   cipher_structure/zkp.md
   cipher_structure/vc.md
   cipher_structure/he.md
   cipher_structure/fe.md
   cipher_structure/rs.md
   cipher_structure/bs.md
   cipher_structure/pre.md
   cipher_structure/cs.md
   cipher_structure/sm2.md
   cipher_structure/sm3.md
   cipher_structure/sm9.md

.. toctree::
   :maxdepth: 2
   :caption: 安全服务
   :hidden:
   
   blockchain_service/private_identity_management.md
   blockchain_service/privacy_data_audition.md
   blockchain_service/changeable_blockchain.md

   API/private_identity_management.md

   
   
   
