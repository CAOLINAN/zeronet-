# @File  : path_init.py
# @Author: PuJi
# @Date  : 2018/1/4 0004

import os,sys
app_dir = 'E:\ZeroNet-master'
sys.path.insert(0, os.path.join(app_dir, "src/lib"))  # External liblary directory
sys.path.insert(0, os.path.join(app_dir, "src"))  # Imports relative to src

from Config import config
config.parse(silent=True)