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

## disabled-Bootstrapper

## disabled-Dnschain

## disabled-DonationMessage

## disabled-Multiuser

## disabled-StemPort

## disabled-UiPassword

## disabled-Zeroname-local

## FilePack

## MergeSite

## Mute

## Newsfeed

## OptionalManager

## PeerDb

## Sidebar

## Stats

## TranslateSite

## Trayicon

## Zeroname

