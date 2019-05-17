#coding=utf-8

class Turtle:
    #Python中的类名约定以大写字母开头
    #特征的描述称为属性，在代码层面来看其实就是变量
    color = 'green'
    weight = 10
    legs = 4
    shell = True
    mouth = '大嘴'

    #方法实际就是函数，通过调用这些函数来完成基本某些动作
    def climb(self):
        print("我正在努力的向前爬")
    def run(self):
        print("我正在飞快的向前跑")
    def bite(self):
        print("咬死你咬死你！！！")
    def eat(self):
        print("有的吃，真满足！")
    def sleep(self):
        print("困了，睡觉，晚安！")

tt = Turtle()
tt.climb()
tt.sleep()
tt.run()
tt.bite()
tt.eat()