#coding=utf-8
"""
    版本：1.0
    产品：bmr
    功能：计算人体指标
    作者：高建帅
    日期：02/04/2019
"""

def main():
    #性别
    gender = '男'
    #身高
    height = 180
    #体重
    weight = 80
    #年龄
    age = 25
    if gender == '男':
        bmr = (13.7 * weight) + (5.0 * height) - (6.8 * age) + 66
    elif gender == '女':
        bmr = (9.6 * weight) + (1.8 * height) - (age * 4.7) + 655
    else:
        bmr = -1
    if bmr != -1:
        print('基础代谢率(大咖)：', bmr)
    else:
        print('暂不支持此功能')


if __name__ == '__main__':
    main()
