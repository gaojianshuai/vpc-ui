#coding=utf-8
"""
    功能：五角星的绘制
    版本：2.0
    日期：01/04/2019
    新增功能：加入循环操作
    新增功能：使用迭代函数绘制
"""
import turtle

def tree(size):
    count = 1
    while count <= 5:
        turtle.forward(size)
        turtle.left(144)
        count = count + 1
    #五角星绘制完，更新参数

def tree_diedai(size):
    #迭代绘制五角星
    count = 1
    while count <= 5:
        turtle.forward(size)
        turtle.left(144)
        count = count + 1
    size = size + 30
    if size<=200:
        tree_diedai(size)

def main():
    """
    主函数
    """
    turtle.penup()
    turtle.backward(200)
    turtle.pendown()
    turtle.pensize(3)
    turtle.pencolor('red')
    size = 50
    tree_diedai(size)
    turtle.exitonclick()

if __name__ == '__main__':
    main()