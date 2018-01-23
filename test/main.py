# coding=utf-8
# @File  : main.py
# @Author: PuJi
# @Date  : 2018/1/3 0003

# import path_init
# from Crypt import CryptBitcoin
# # from Crpt import CryptHash
#
#
# privatekey = CryptBitcoin.newPrivatekey()
# address = CryptBitcoin.privatekeyToAddress(privatekey)
# print(privatekey)
# print (address)
class DB():
    def __init__(self, dbpath, name):
        self.dbpath = dbpath
        self.name = name

class NewDB(DB):
    def __init__(self, path, name):
        DB.__init__(self, path, name)
        print(self.dbpath)

a = NewDB("r",1)


