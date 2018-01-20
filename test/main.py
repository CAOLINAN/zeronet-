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
import requests,json
data = {
    "test":[{ "BTC": "Bithumb"},{"BTC": "Coinone"}],
    "testss":"dasdasdsad"
}
print(requests.post(url='http://127.0.0.1:43110/',data=json.dumps(data)).text)



