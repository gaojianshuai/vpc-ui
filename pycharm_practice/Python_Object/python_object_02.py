#coding=utf-8

"""
    作者：高建帅
    日期：14/05/2019
    功能：类的继承（直接在类名后面的括号里填入要继承类的类名）
"""


class MyList(list):
    pass
#MyList继承了list类的所有功能
list2 = MyList()
list2.append(2)
list2.append(2)
list2.append(4)
list2.append(55)
print(list2)


# ***************************************
# 如果子类中定义与父类同名的方法或者属性，则会自动覆盖父类对应的方法和属性

import random as r
class Fish():
    def __init__(self):
        self.x = r.randint(0, 10)
        self.y = r.randint(0, 10)
    def move(self):
        self.x -= 1
        print("我的位置是:", self.x, self.y)
class Shark(Fish):
    def __init__(self):#子类重写了父类的方法，相当于子类的方法覆盖了父类的方法，则子类中没有父类中定义的方法和属性
        Fish.__init__(self)#调用未绑定的的父类方法，此时的self是子类对象，并不是父类对象
        self.hungry = True
    def eat(self):
        if self.hungry:
            print("吃货的梦想就是每天都能吃上山珍海味")

        else:
            self.hungry = False
            print("太撑了，吃不动啦！！！")
ff = Shark()
tt = Fish()
tt.move()
ff.eat()

