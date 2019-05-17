#coding=utf-8
"""
    功能：五角星的绘制
    版本：2.0
    日期：01/04/2019
    新增功能：加入循环操作
"""
import turtle

def tree(size):
    count = 1
    while count <= 5:
        turtle.forward(size)
        turtle.left(144)
        count = count + 1
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
    while size <= 200:

        tree(size)
        size = size + 50
    turtle.exitonclick()

if __name__ == '__main__':
    main()