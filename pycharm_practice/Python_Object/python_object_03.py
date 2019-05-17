#coding=utf-8

"""
    作者：高建帅
    日期：14/05/2019
    功能：类的继承（直接在类名后面的括号里填入要继承类的类名）
    新增功能：使用super函数直接调用父类使用的方法
"""

import random as r
class Fish():
    def __init__(self):
        self.x = r.randint(0, 10)
        self.y = r.randint(0, 10)
    def move(self):
        self.x -= 1
        print("我的位置是:", self.x, self.y)
class Shark(Fish):
    def __init__(self):
        super().__init__()#使用super函数直接调用父类的方法
        #self.hungry = True
        self.hungry = False
    def eat(self):
        if self.hungry:
            print("吃货的梦想就是每天都能吃上山珍海味")
        else:

            print("太撑了，吃不动啦！！！")

ff = Shark()
tt = Fish()
tt.move()
ff.eat()