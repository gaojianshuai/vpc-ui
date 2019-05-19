#coding=utf-8
"""
    作者：高建帅
    功能：
    新增功能：
    日期：2019/5/18 12:21
"""

class Cat:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print('{}爱吃鱼'.format(self.name))

t = Cat('gaojianshuai')
t.eat()
