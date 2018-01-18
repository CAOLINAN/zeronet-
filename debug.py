# coding=utf-8
# @File  : test.py
# @Author: PuJi
# @Date  : 2018/1/18 0018
class Test():
    def pause(self, sentence):
        while True:
            if raw_input("sentence is {}? (1) > ".format(sentence)).lower() == "1":
                break
            else:
                print("Please, secure it now, you going to need it to modify your site!")
# 单例模式，方便中断执行判断
test = Test()
