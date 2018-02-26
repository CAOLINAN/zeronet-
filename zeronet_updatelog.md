添加0.3.4的更改日志
	修改CHANGELOG.md
		AES，ECIES API功能支持
		API中的PushState和ReplaceState url操作支持
		多用户本地存储

添加0.3.5的更改日志
	修改CHANGELOG.md
		带有.onion隐藏服务的Full Tor支持
		使用ZeroNet协议的Bootstrap
		修复Gevent 1.0.2兼容性

添加0.3.6的更改日志
	修改CHANGELOG.md
		新ZeroHello
		新闻源功能
		安全修复

添加0.3.7的更改日志
	修改CHANGELOG.md
		补丁命令通过仅传输更改的行来减少带宽使用
		其他CPU /内存优化

添加0.4.0的更改日志
	修改CHANGELOG.md
		合并网站
		用户文件归档
		允许将自定义字段存储在json表中

添加0.4.1的更改日志
	修改CHANGELOG.md
		显着加快启动时间
		减少内存使用量

添加0.5.0的更改日志
	修改CHANGELOG.md
		限制和管理可选文件
		API命令注册/下载/删除可选文件

添加0.5.2的更改日志
	修改CHANGELOG.md
		多语言界面和网站翻译支持

添加0.5.2的更改日志
	修改CHANGELOG.md
		用户静音

添加0.5.3的更改日志
	修改CHANGELOG.md
		Tar.gz和zip压缩静态内容支持

添加0.5.4的更改日志
	修改CHANGELOG.md
		Major Tor：总是进行模式改进
		重要的安全修复
		更新依赖关系
		更好的内容分发

添加0.5.5的更改日志
	修改CHANGELOG.md
		删除时的网站黑名单选项
		更新克隆网站的源代码
		用于加快网站内容显示的新优先级算法
		传出套接字绑定选项

添加0.5.6的更改日志
	修改CHANGELOG.md
		新增
			源代码升级期间的代理旁路
			使用DNS重新绑定的XSS漏洞
			开放端口检查
			独立的update.py参数解析
			uPnP在启动时崩溃
			CoffeeScript 1.12.6兼容性
			多值参数解析
			从包含特殊字符的目录运行时出现数据库错误
			网站锁定违例记录
		更改
			certSelect API的回调命令
			更紧凑的json列表格式
		修复
			删除过时的auth_key_sha512和签名格式
			改进西班牙语翻译

Jul 30, 2017
添加0.5.7的更改日志
	修改CHANGELOG.md
		新增
			新插件：CORS用来向其他网站的内容请求读取权限
			新API命令：userSetSettings/userGetSettings将用户的设置存储在users.json中
			如果文件大小与请求文件不匹配，不进行文件下载
			使用/raw/前缀来使JavaScript和包装较少文件进行访问([示例](http://127.0.0.1:43110/raw/1AsRLpuRxr3pb9p3TKoMXPSWHzh6i7fMGi/en.tar.gz/index.html))
			-- 命令行的静态模式禁止日志输出
		更改
			对于sign/验证等错误进行更好的错误日志记录
			对sign和验证过程进行更多测试
			把OpenSSL更新到v1.0.2l
			将压缩文件限制为6MB以避免zip/tar.gz炸弹
			在文件名中允许空格，[]，（）字符
			禁用跨站点资源加载以提高隐私。
			下载直接访问的Pdf / Svg / Swf文件，而不是显示它们以避免在SVG文件中使用JS中的包装器退出。 [Beardog108报道]
			禁止潜在的不安全正则表达式以避免ReDoS [MuxZeroNet报告]
		修复
			运行Windows发行版exe时检测数据目录[Plasmmer报告]
			Android 6+下的OpenSSL加载
			没有连接服务器启动时退出时出错

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
			将不可靠的tracker更改
			如果跨域已经授权则不显示跨域相关问题
			重建合并网站时避免UI阻塞
			在签名时跳过列出被忽略的目录
			在多用户模式下，在添加新证书而不是第一次访问时显示种子欢迎消息
			在多个网络接口上更快地打开异步端口
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
			当同时请求来自不同站点的文件时，Websocket连接不能到达
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

