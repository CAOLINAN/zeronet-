# function:
## main
主方法，开启文件服务器和Ui服务器。接入zeronet网络浏览其中资源

## siteCreate
站点创建，生成hello的index.html文件，产生私钥，需要手动保存，不会自动保存在users.json文件中。

## siteSign
站点签名，根据当前文件夹下的文件计算  保存json文件，

## siteVerify
站点确认

## dbRebuild
数据库重建

## dbQuery
数据库查询

## siteAnnounce
站点公布

## siteDownload
站点下载

## siteNeedFile
下载站点缺失文件

## sitePublish
站点发布

## cryptPrivatekeyToAddress
私钥生成地址

## cryptSign
消息签名

## cryptVerify
消息确认

## peerPing
节点ping，检查节点是否存活

## peerGetFile
从节点中获取文件

## peerCmd
节点命令操作

## getConfig
打印配置信息

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

