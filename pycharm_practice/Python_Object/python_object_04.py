#coding=utf-8

"""
    作者：高建帅
    日期：14/05/2019
    功能：类的继承（直接在类名后面的括号里填入要继承类的类名）
    新增功能：多重继承不太合适，所以用组合
"""

#现在要求定义一个类，叫水池，水池里要有乌龟和鱼（组合）
#定义鱼类
class Fish:
    def __init__(self, x):
        self.num = x#在类中定义num的属性
#定义乌龟类
class Turtle:
    def __init__(self, y):
        self.num = y#在类中定义num的属性
#定义水池类

class Pool:
    def __init__(self, x, y):
        self.fish = Fish(x)#在水池中定义fish的属性，值为Fish的实例化
        self.turtle = Turtle(y)
    def print_num(self):
        print("水池里一共有 %d 只乌龟, %d条鱼" % (self.turtle.num, self.fish.num))

tt = Pool(20, 25)
tt.print_num()

