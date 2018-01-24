# coding=utf-8
# @File  : test.py
# @Author: PuJi
# @Date  : 2017/12/27 0027
import socket
import json
import sys
import os
import array

s = ['E:\\ZeroNet-master', 'C:\\WINDOWS\\SYSTEM32\\python27.zip', 'E:\\ZeroNet-master\\env\\DLLs', 'E:\\ZeroNet-master\\env\\lib', 'E:\\ZeroNet-master\\env\\lib\\plat-win', 'E:\\ZeroNet-master\\env\\lib\\lib-tk', 'E:\\ZeroNet-master\\env\\Scripts', 'C:\\Python27\\Lib', 'C:\\Python27\\DLLs', 'C:\\Python27\\Lib\\lib-tk', 'E:\\ZeroNet-master\\env', 'E:\\ZeroNet-master\\env\\lib\\site-packages']
b = ['E:\\ZeroNet-master\\src', 'E:\\ZeroNet-master\\src/lib', 'E:\\ZeroNet-master', 'C:\\WINDOWS\\SYSTEM32\\python27.zip', 'E:\\ZeroNet-master\\env\\DLLs', 'E:\\ZeroNet-master\\env\\lib', 'E:\\ZeroNet-master\\env\\lib\\plat-win', 'E:\\ZeroNet-master\\env\\lib\\lib-tk', 'E:\\ZeroNet-master\\env\\Scripts', 'C:\\Python27\\Lib', 'C:\\Python27\\DLLs', 'C:\\Python27\\Lib\\lib-tk', 'E:\\ZeroNet-master\\env', 'E:\\ZeroNet-master\\env\\lib\\site-packages', 'plugins']

if __name__ == '__main__':
    for t in b:
        if t not in s:
            print(t)

    print("-----------------------------------")

    for t in s:
        if t not in b:
            print(t)