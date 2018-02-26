Feb 23, 2018
修复msgpack版本引发的bug
	msgpack改为0.4.4至0.5.5的版本
修复大文件下载按钮bug
	端口由3335修改为3337，其余部分修改了前端代码

端口修改由3329修改为3335
	
合并侧边栏和包装器代码
	修改前端代码
增强安全性，在代理服务器上不允许NOSANDBOX权限，因为会泄露cookie
	修改plugins/disabled-Multiuser/MultiuserPlugin.py文件
		新增方法动作权限添加，主要针对websocket接口
确保多用户插件兼容包装器修改的部分
	修改plugins/disabled-Multiuser/MultiuserPlugin.py
		主要将wrapper的提示方法修改为zeroframe框架提示方法
确保证书选择兼容包装器修改的部分
	修改src/Ui/UiWebsocket.py
		将wrapper的方法改为zeroframe的方法
新的NOSANDBOX权限可以移除iframe沙盒限制
	修改src/Ui/UiRequest.py
		权限验证中判断NOSANDBOX权限
	修改src/Ui/UiWebsocket.py
		权限验证中判断NOSANDBOX权限
如果打开器存在就停止页面加载
	修改src/Ui/template/wrapper.html
		前端代码
如果站点已经存在则不用验证权限
	修改src/Ui/media/Wrapper.coffee
		前端代码
移动handleMessage分离方法
	修改src/Ui/media/Wrapper.coffee
		前端代码
包装器添加cmd方法
	修改src/Ui/media/Wrapper.coffee
		前端代码
删除记录注入的HTML
	修改src/Ui/media/Wrapper.coffee
		前端代码
验证鼠标和键盘事件以避免通知提示中的非用户验证
	修改src/Ui/media/Wrapper.coffee
		前端代码
移除代理请求和返回站点的部分代码
	修改src/Ui/media/Wrapper.coffee
		前端代码
允许设置get参数来重新加载
	修改src/Ui/media/Wrapper.coffee
		前端代码
一直到Feb 21, 2018
	所有都是修改前端代码，剩余依次提交信息为
		在信息中允许使用小标签
		在页面加载的过程中重命名包装器
		在加载iframe之前移除包装器对象以增强安全性
		创建一个受限制的zeroframe包装器
		修复侧边栏缺失了地球bug
		将侧边栏对象保存为本地对象

Feb 20, 2018
修复网站归档下载测试
	修改src/Test/TestSiteDownload.py
		在站点发布之后睡眠0.1秒再等待下载

Feb 18, 2018
添加0.6.2的更改日志
	修改CHANGELOG.md
		新增
			新插件：AnnounceLocal可使ZeroNet在本地网络上无需互联网连接。
			允许dbQuey和userGetSettings在具有Cors权限的不同站点上使用`as` API命令
			新的配置选项：`--log_level`以减少日志冗长和IO负载
			首选连接到tracker中最近的节点
			未来将使端口为1的节点为不可达节点来适配端口为0的tracker
		更改
			不要保留上周没有修改的网站的连接
			将不可靠的追踪器更改为新的追踪器
			在查找一个可选文件中最多发送10个findhash请求（15sec）
			在证书选择对话框中将默认选项由“站点唯一”更改为“无证书”。
			如果不在调试模式下，不要打印警告
			简单统一tracker日志格式
			如果站点有节点的话，只能从sites.json中恢复网站
			本地节点间的消息并不意味着互联网连接
			删除`--debug_gevent`并默认打开Gevent块日志
		修复
			将连接数限制在512用来避免达到windows的1024上限
			当日志记录外部操作系统套接字错误时抛出异常
			不要在PEX上发送私人（本地）IP
			不要在always模式下连接到本地IP
			在文件流启动时从msgpack解包器正确恢复数据
			使用Windows删除站点时删除符号链接的数据目录
			在发布之前取消重复的节点
			不存在的文件(标记为？)大文件信息
端口修改由3328修改为3329

允许广播失败
	修改plugins/AnnounceLocal/BroadcastServer.py
		捕获socket连接中出现的异常，异常添加到警告日志中
将Unique to site重命名为无证书
	修改src/Ui/UiWebsocket.py
		证书选择默认值由unique to site 更改为无证书

Feb 13, 2018
修改CLI中站点下载，站点公布，站点缺失文件命令
	修改src/Config.py
		端口由3327修改为3328
	修改src/Connection/ConnectionServer.py
		新增handleMessage方法
	修改src/main.py
		站点公布中新增全局变量文件服务器，打开本地端口1234
		站点下载中将连接服务器更改为文件服务器，打开本地端口1234
		站点缺失文件中将连接服务器更改为文件服务器，打开本地端口1234
添加新的msgpack的版本兼容性
	修改src/Config.py
		端口由3326修改为3327
	修改src/Connection/Connection.py
		修改解包方法，判断是否含有新版本方法否则就用旧版本方法
运行插件测试直到运行失败
	修改.travis.yml
		单元测试新增-x参数
修改端口由3323修改为3326
格式化
	修改src/Worker/WorkerManager.py
		修改一些日志的格式
一轮中最多有10个findhash
	修改src/Worker/WorkerManager.py
		节点选取前10
只测试没有在工作的节点
	修改src/Worker/WorkerManager.py
		peers_try选取未在workers中的
为端口检查添加缺少的导入
	修改src/File/FileRequest.py
		导入socket

Feb 13, 2018
增加本地节点超时
	修改plugins/AnnounceLocal/AnnounceLocalPlugin.py
		超时时间由10分钟设置为20分钟

Feb 12, 2018
只读我们需要的东西
	修改src/Connection/Connection.py
		每次接收取64*1024与read_bytes中的最小值的字节数
正确地从解包器中恢复额外的数据
	修改src/Connection/Connection.py
		检查解包器时候还有数据残留在内存中

Feb 11, 2018
合并提交的分支
	合并俄语的帮助文档
修复bigfile下载到不存在的目录
	修改src/Config.py
		端口由3321修改为3323
	修改plugins/Bigfile/BigfilePlugin.py
		若文件夹不存在则创建文件夹
合并pr
	合并俄语的帮助文档

Feb 10, 2018
修改端口端口由3319修改为3321
Tor连接错误和uPnP打通错误并不重要
	修改src/File/FileServer.py
		日志级别由错误更改为警告
	修改src/Tor/TorManager.py
		日志级别由错误更改为警告
可配置文件的日志级别
	修改src/Config.py
		新增日志级别
	修改src/main.py
		根据配置的日志级别设置日志等级
修改端口端口由3318修改为3319
有些tracker不接受端口0，所以发送端口1作为不可连接
	修改src/Site/Site.py
		如果节点端口为1的话，那么修改为0
只从UDP tracker中解析字典结果
	修改src/Site/Site.py
		向节点公布站点时判断响应是否为字典结果，否则一律任务无响应
请求时添加剩余的字节来提高tracker的兼容性
	修改src/Site/Site.py
		tracker公布时将num_want值由50修改为num_want，并添加新参数left，值为431102370
在更新模式下请求更少的节点
	修改src/Site/Site.py
		如果为更新模式则num_want为10，否则为30
如果不在调试模式下时就不显示警告信息
	修改src/main.py
		添加日志的警告等级值
添加tracker
	修改src/Config.py
		新增一些tracker
转到更可靠的tracker中
	修改src/Config.py
		修改一些tracker
不记录BroadcastServer关闭socket连接
	修改plugins/AnnounceLocal/BroadcastServer.py文件
		判断是否在运行再抛出异常
修复公布的时间限制
	修改plugins/AnnounceLocal/AnnounceLocalPlugin.py
		限时时间更改为5分钟	
修改端口端口由3313修改为33198
开启本地tracker用来测试
	修改plugins/AnnounceLocal/Test/TestAnnounce.py
		单元测试内容
测试时默认不开启广播broadcast服务
	修改plugins/AnnounceLocal/Test/conftest.py
		单元测试内容
广播服务器关机时显示更详细的内容
	修改plugins/AnnounceLocal/BroadcastServer.py
		关闭时显示端口信息
如果服务关闭的话不做响应
	修改plugins/AnnounceLocal/BroadcastServer.py
		如果未运行则跳出
当绑定失败时处理
	修改plugins/AnnounceLocal/BroadcastServer.py
		添加binded标记判断是否绑定成功，绑定成功则运行
允许UDP端口重复利用
	修改plugins/AnnounceLocal/BroadcastServer.py
向未知节点发送请求时延以允许响应首先到达
	修改plugins/AnnounceLocal/AnnounceLocalPlugin.py
		记录时间，原始discover函数通过gevent异步调用

Feb 9, 2018
删除本地广播绑定到IP以确保测试在linux中通过
	修改src/Config.py
		修改端口端口由3312修改为3313
	修改plugins/AnnounceLocal/BroadcastServer.py
		修改调试信息
	修改plugins/AnnounceLocal/Test/TestAnnounce.py
		删除监听的IP
添加AnnounceLocal的自动化测试
	修改.travis.yml
		添加单元测试
更改版本信息
	修改src/Config.py
		版本由0.6.1更改为0.6.2
		端口由3234更改为3312
为cli参数帮助添加metavar
	修改plugins/AnnounceLocal/AnnounceLocalPlugin.py
		--broadcast_port帮助参数中添加metavar='port'
统一本地公布日志
	修改plugins/AnnounceLocal/AnnounceLocalPlugin.py		
		修改日志格式
没有本地的公布时修复公布问题
	修改plugins/AnnounceLocal/AnnounceLocalPlugin.py
		新增判断是否存在本地公布
恢复0.6.2版本
	修改src/Config.py
		修改版本号0.6.2改为0.6.1
		端口由3310更改为3234
	修改src/Ui/UiWebsocket.py
		self.admin_commands添加serverShowdirectory
	修改src/Ui/media/Wrapper.coffee
		websocket的URL更改
	修改src/Ui/media/all.js
		websocket的URL更改
	修改src/User/User.py
		删除generateAuthAddress方法
		getSiteData中删除generateAuthAddress的调用，方法合并到getSiteData中
	修改src/Worker/Worker.py
		删除部分代码
0.6.2版本
	做的操作在后来全部恢复
为声望添加评论
	修改plugins/PeerDb/PeerDbPlugin.py
		添加了注释。。
AnnounceLocal 插件
	新增plugins/AnnounceLocal/AnnounceLocalPlugin.py
		本地公布插件
	新增plugins/AnnounceLocal/BroadcastServer.py
		广播服务
	新增plugins/AnnounceLocal/Test/TestAnnounce.py
		单元测试
	新增plugins/AnnounceLocal/Test/conftest.py
		单元测试
	新增plugins/AnnounceLocal/Test/pytest.ini
		单元测试



Oct 17, 2017
添加请求权限的细节
	修改src/Config.py
		端口由3112更改为3114
	修改plugins/MergerSite/MergerSitePlugin.py
		新增actionPermissionDetails方法
	修改src/Ui/UiWebsocket.py
		新增actionPermissionDetails方法
	修改src/Ui/media/Wrapper.coffee
		前端代码
	修改src/Ui/media/all.js
		前端代码
添加0.6.0的更改日志
	修改CHANGELOG.md
		新增
			新插件：大文件支持
			自动固定大文件下载
			启用TCP_NODELAY以支持套接字
			actionOptionalFileList API命令参数列出未下载的文件或仅包含大文件
			serverShowdirectory API命令参数，以允许在OS文件浏览器中显示站点的目录
			fileNeed API命令初始化可选文件下载
			wrapperGetAjaxKey API命令为AJAX请求请求nonce
			数据库文件支持Json.gz
			P2P端口检查（感谢grez911）
			`--download_optional auto`参数为新添加的站点启用自动可选文件下载
			/ Stats上的大文件和协议命令请求的统计信息
			允许基于auth_address设置用户限制
		更改
			更积极和频繁的连接超时检查
			对大于512KB的文件使用msgpack上下文文件流
			允许可选文件工作者超过工作者限制
			自动重定向到nonce_error上的包装
			在可选文件删除时发送websocket事件
			优化sites.json保存
			默认启用速度更快的基于C的msgpack打包器
			对Bootstrapper插件SQL查询的主要优化
			不要在重新启动时重置坏文件计数器，以便更容易放弃无法访问的文件
			传入连接限制从1000更改为500，以避免在Windows上达到套接字限制
			更改了tracker boot.zeronet.io域名，因为zeronet.io在某些国家被禁止
		修复
			用户目录中的子目录
		ZeroNet 0.5.7 (2017-07-19)
		新增
			新插件：CORS向其他网站的内容请求读取权限(跨域访问)

Oct 18, 2017
更新中文帮助文档
	修改README-zh-cn.md
		python修改为python2
合并pr

Oct 21, 2017
报告GeoLite2下载的进度
	修改plugins/Sidebar/SidebarPlugin.py
		notification命令修改为progress。
		计算进度
		下载失败增加提示
	修改src/Ui/media/Notifications.coffee
		前端代码
	修改src/Ui/media/all.js
		前端代码
修复使用Tor时的网站违规问题
	修改src/Site/Site.py
		新增tor网络连接正常判断
每个站点6个连接	
	修改src/Site/Site.py
		needConnections默认连接数由4更改为6
修改端口端口由3114修改为3120
合并pr(中文文档修复)

Oct 22, 2017
添加有关cli签名错误的更多详细信息
	修改src/main.py
		异常时显示更多异常信息
自动忽略数据库文件
	修改src/Config.py
		修改端口端口由3120修改为3122
	修改src/Content/ContentManager.py
		添加判断分支
	修改src/Site/SiteStorage.py
		添加获取数据库的方法
Oct 26, 2017
在bigfile上传后重新载入content.json信息
	修改plugins/Bigfile/BigfilePlugin.py
		getFileInfo中新增参数new_file=True
		方法结束前重新加载content.json
调用UiWebsocket动作的返回值的响应函数
	修改src/Ui/UiWebsocket.py
		判断结果，做出回应
对于慢任务总是打开工作者
	修改src/Worker/WorkerManager.py
		更改打开工作者函数位置
从content.json位置中剥离文件信息
	修改src/Content/ContentManager.py
		拆分函数
让大文件上传初始化兼容合并站点
	修改plugins/Bigfile/BigfilePlugin.py
		响应修改为返回
	修改plugins/MergerSite/MergerSitePlugin.py
		合并方法
		新增actionBigfileUploadInit
端口由3122更改为3125
修复fileInfo测试
	修改src/Test/TestContent.py
DbQuery：没有and的where还应该是where
	修改src/Db/DbQuery.py
		新增判断条件
Newsfeed：在where时添加括号
	修改plugins/Newsfeed/NewsfeedPlugin.py
		查询条件添加括号

Jan 25, 2018
0.6.1版本修改日志
	修改CHANGELOG.md
		新增
			新插件：图表
			收集并显示有关您对ZeroNet网络贡献的图表
			允许列表作为sql查询中的参数替换。 （感谢imachug）
			Newsfeed查询时间统计信息（点击“来自ZeroHello的X.Xs中的XX站点”
			新的UiWebsocket API命令：用于将命令作为其他站点运行
			针对大文件的ajax轮询
			按类型和网站地址过滤Feed
			FileNeed，Bigfile上传命令与合并站点兼容
			在端口打开/改变状态改变时发送事件
			关于权限请求的更多描述
		更改
			减少边栏geoip数据库缓存的内存使用量
			将不可靠的tracker更改为tracker
			如果跨域已经授权则不显示跨域相关问题
			重建合并网站时避免UI阻塞
			在签名时跳过列出被忽略的目录
			在多用户模式下，在添加新证书而不是第一次访问时显示种子欢迎消息
			在多个网络接口上打开更快的异步端口
			允许JavaScript模式
			只有在鼠标按钮被按下的情况下，才会缩放侧边栏
		修复
			打开端口检查错误报告（感谢imachug）
			超出范围的大文件请求
			不要在gevent greenlets上发生两次错误
			新闻提要跳过没有数据库的网站
			采用多个参数的新闻传递查询
			使用UNION和UNION ALL进行新闻提交查询
			修复站点大于10MB的站点克隆
			同时请求来自不同站点的文件时，不可靠的Websocket连接


