# function:
## main
主方法，开启文件服务器和Ui服务器。接入zeronet网络浏览其中资源

## siteCreate
站点创建，生成hello的index.html文件，产生私钥，需要手动保存，不会自动保存在users.json文件中。

## siteSign
站点签名，根据当前文件夹下的文件计算哈希值，保存json文件，

## siteVerify
站点确认，验证当前文件夹下的所有文件是否匹配json文件中的哈希值

## dbRebuild
数据库重建，重新构建动态站点的数据库文件，更新sql缓存。

## dbQuery
数据库查询，查询动态站点的数据库，根据sql返回结果。

## siteAnnounce
站点公布，向tracker和已连接的节点公布站点。

## siteDownload
站点下载,下载该站点的所有文件。

## siteNeedFile
下载站点缺失文件，根据传入的参数查询对应文件是否存在，不存在则下载。

## sitePublish
站点发布，主动向节点更新站点文件。向连接的节点发送update命令。

## cryptPrivatekeyToAddress
私钥生成地址，根据输入的私钥生成地址。

## cryptSign
消息签名，对消息进行加密，返回加密后的值。

## cryptVerify
加密确认，使用地址和符号验证数据，返回对错。

## peerPing
节点ping，向节点发送ping请求。

## peerGetFile
从节点中获取文件，根据文件大小定义不同的文件块(5M以上每次最大读取1M数据，以内每次最大读取512KB数据)，根据设置向节点发送streamFile或者getFile请求

## peerCmd
节点命令操作。向节点发送命令请求。

## getConfig
打印配置信息。获取当前的一些设置信息。

# plugin:
## Announcelocal
公布本地.UDP广播端口以便节点被发现。				
## AnnounceZero

## Bigfile
大文件拆分

## Chart
图表信息，记录对zeronet的贡献

## Cors
跨域问题，权限验证

## CryptMessage
消息签名。

## disabled-Bootstrapper
启动器设置，洋葱网络一些节点设置。

## disabled-Dnschain
DNS链的域名解析。

## disabled-DonationMessage
捐赠地址设置。

## disabled-Multiuser
多用户设置。

## disabled-StemPort
stem端口设置信息。进入暗网。

## disabled-UiPassword
关闭保存Cookie，包含用户名密码登录等相关问题的操作

## disabled-Zeroname-local
关闭代理服务的相关操作。

## FilePack
文件打包，对文件进行压缩解压等操作。

## MergeSite
合并站点，合并站点需要的一些操作。

## Mute
静音。设置站点黑名单。

## Newsfeed
关注新闻。设置用户关注的一些操作。

## OptionalManager
可选管理器。创建可选文件数据库，记录文件大小等状态。记录一些请求的日志。进行可选文件的限制。

## PeerDb
节点数据库，将连接的节点信息保存在数据库中。

## Sidebar
侧边栏，侧边栏的一些功能，包括站点限制、站点缺失文件、WebGL显示等。

## Stats
统计信息，涵盖站点大小、站点停留时间、CPU使用情况、连接情况、缓存情况等。

## TranslateSite
翻译站点

## Trayicon
图标操作，通知栏显示图标，进行软件的一些操作、

## Zeroname
加载域名系统，域名解析
