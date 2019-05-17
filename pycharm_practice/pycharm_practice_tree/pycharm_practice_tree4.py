#coding=utf-8
"""
    功能：五角星的绘制
    版本：1.0
    日期：01/04/2019
    新增功能：利用递归绘制分形树
"""
import turtle

def drow_branch(branch_length):
    """
    绘制分形树函数
    :return:
    """
    #绘制右侧树枝
    if branch_length > 5:
        turtle.forward(branch_length)
        turtle.right(20)
        drow_branch(branch_length - 15)


        #绘制左侧树枝
        turtle.left(40)
        drow_branch(branch_length - 15)


        #但会之前胡树枝
        turtle.right(20)
        turtle.backward(branch_length)

def main():
    """
    主函数
    """
    turtle.left(90)
    turtle.penup()
    turtle.color('brown')
    turtle.backward(150)
    turtle.pendown()
    drow_branch(100)

    turtle.exitonclick()

if __name__ == '__main__':
    main()