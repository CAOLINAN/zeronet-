# coding=utf-8
import logging
import os
import sys
from collections import defaultdict



class PluginManager:
    def __init__(self):
        self.log = logging.getLogger("PluginManager")
        self.plugin_path = "plugins"  # Plugin directory
        self.plugins = defaultdict(list)  # Registered plugins (key: class name, value: list of plugins for class)
        self.subclass_order = {}  # Record the load order of the plugins, to keep it after reload
        self.pluggable = {}
        self.plugin_names = []  # Loaded plugin names
        # 会有三个方法通过装饰器加载进来，分别为
        # importPluginnedClasses(plugins/Bigfile/BigfilePlugin.py)
        # importPluginnedClasses(plugins/OptionalManager/OptionalManagerPlugin.py)
        # importErrors(plugins/AnnounceZero/AnnounceZeroPlugin.py)
        self.after_load = []  # Execute functions after loaded plugins

        sys.path.append(self.plugin_path)


    # -- Load / Unload --

    # Load all plugin
    def loadPlugins(self):
        # 加载plugins目录下所有模块
        for dir_name in sorted(os.listdir(self.plugin_path)):
            # if dir_name == "plugins/Mute":
            #     # 新建mutes.json文件
            #     print("""plugins/Mute...""")
            dir_path = os.path.join(self.plugin_path, dir_name)
            if dir_name.startswith("disabled"):
                continue  # Dont load if disabled
            if not os.path.isdir(dir_path):
                continue  # Dont load if not dir
            if dir_name.startswith("Debug") and not config.debug:
                continue  # Only load in debug mode if module name starts with Debug
            self.log.debug("Loading plugin: %s" % dir_name)
            try:
                __import__(dir_name)
            except Exception, err:
                self.log.error("Plugin %s load error: %s" % (dir_name, Debug.formatException(err)))
            if dir_name not in self.plugin_names:
                self.plugin_names.append(dir_name)
        # 全局搜索@PluginManager.afterLoad装饰器，全部执行
        for func in self.after_load:
            # 当前版本加载三个方法 importPluginnedClasses、importPluginnedClasses、importErrors
            # importPluginnedClasses 会加载默认数据库
            func()

    # Reload all plugins
    def reloadPlugins(self):
        self.plugins_before = self.plugins
        self.plugins = defaultdict(list)  # Reset registered plugins
        for module_name, module in sys.modules.items():
            if module and "__file__" in dir(module) and self.plugin_path in module.__file__:  # Module file within plugin_path
                if "allow_reload" in dir(module) and not module.allow_reload:  # Reload disabled
                    # Re-add non-reloadable plugins
                    for class_name, classes in self.plugins_before.iteritems():
                        for c in classes:
                            if c.__module__ != module.__name__:
                                continue
                            self.plugins[class_name].append(c)
                else:
                    try:
                        reload(module)
                    except Exception, err:
                        self.log.error("Plugin %s reload error: %s" % (module_name, Debug.formatException(err)))

        self.loadPlugins()  # Load new plugins

        # Change current classes in memory
        import gc
        patched = {}
        for class_name, classes in self.plugins.iteritems():
            classes = classes[:]  # Copy the current plugins
            classes.reverse()
            base_class = self.pluggable[class_name]  # Original class
            classes.append(base_class)  # Add the class itself to end of inherience line
            plugined_class = type(class_name, tuple(classes), dict())  # Create the plugined class
            for obj in gc.get_objects():
                if type(obj).__name__ == class_name:
                    obj.__class__ = plugined_class
                    patched[class_name] = patched.get(class_name, 0) + 1
        self.log.debug("Patched objects: %s" % patched)

        # Change classes in modules
        patched = {}
        for class_name, classes in self.plugins.iteritems():
            for module_name, module in sys.modules.iteritems():
                if class_name in dir(module):
                    if "__class__" not in dir(getattr(module, class_name)):  # Not a class
                        continue
                    base_class = self.pluggable[class_name]
                    classes = self.plugins[class_name][:]
                    classes.reverse()
                    classes.append(base_class)
                    plugined_class = type(class_name, tuple(classes), dict())
                    setattr(module, class_name, plugined_class)
                    patched[class_name] = patched.get(class_name, 0) + 1

        self.log.debug("Patched modules: %s" % patched)


plugin_manager = PluginManager()  # Singletone
# plugin_manager.plugin_path = "E:\ZeroNet-master\plugins"
# plugin_manager.loadPlugins()
# -- Decorators --

# Accept plugin to class decorator


def acceptPlugins(base_class):
    class_name = base_class.__name__ # 记录类名
    plugin_manager.pluggable[class_name] = base_class   # 加入可插拔字典 值为{类名：类}键值对
    if class_name in plugin_manager.plugins:  # Has plugins
        classes = plugin_manager.plugins[class_name][:]  # Copy the current plugins

        # Restore the subclass order after reload
        if class_name in plugin_manager.subclass_order:
            classes = sorted(
                classes,
                key=lambda key:
                    plugin_manager.subclass_order[class_name].index(str(key))
                    if str(key) in plugin_manager.subclass_order[class_name]
                    else 9999
            )
        plugin_manager.subclass_order[class_name] = map(str, classes)

        classes.reverse()
        classes.append(base_class)  # Add the class itself to end of inherience line
        plugined_class = type(class_name, tuple(classes), dict())  # Create the plugined class
        plugin_manager.log.debug("New class accepts plugins: %s (Loaded plugins: %s)" % (class_name, classes))
    else:  # No plugins just use the original
        plugined_class = base_class
    return plugined_class


# Register plugin to class name decorator
# 该装饰器将类注册到插件管理中，在插件管理实例的插件字典里注册，将该类的插件类添加到对应类中，一个类可以有多个插件类
def registerTo(class_name):
    plugin_manager.log.debug("New plugin registered to: %s" % class_name)
    if class_name not in plugin_manager.plugins: # 判断类名是否在插件管理字典中，没有则加入管理字典中，值为{类：[]}键值对
        plugin_manager.plugins[class_name] = []

    def classDecorator(self):
        plugin_manager.plugins[class_name].append(self) # 插件管理字典中类名值新增传入值
        return self
    return classDecorator


def afterLoad(func):
    plugin_manager.after_load.append(func) #插件管理加载完成后方法新增方法
    return func


# - Example usage -

if __name__ == "__main__":
    # @registerTo("Request")
    # class RequestPlugin(object):
    #     def test(self):
    #         print 'RequestPlugin test'
    #
    #     def actionMainPage(self, path):
    #         return "Hello {}!".format(path)
    #         # return "Hello MainPage!"
    #
    # @acceptPlugins
    # class Request(object):
    #
    #     def route(self, path):
    #         func = getattr(self, "action" + path, None)
    #         if func:
    #             return func(path)
    #         else:
    #             return "Can't route to", path
    #
    #     def test(self):
    #         print "Request test"
    #
    # # print Request().route("MainPage")
    # # print plugin_manager.plugins
    # ccc = plugin_manager.plugins['Request'][:]
    # print(ccc[0]())
    # # print (ccc[0]().actionMainPage('1'))
    # # print('-------------------------')
    # # print Request().actionMainPage('path')
    # print(ccc[0]().test())
    # print(Request().test())
    print(sys.path)
    print(os.getcwd())
    print(os.listdir(r"ttt"))
