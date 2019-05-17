#coding=utf-8
"""
    版本：2.0
    产品：bmr
    功能：计算人体指标
    作者：高建帅
    新增功能：循环
    日期：02/04/2019
    新增功能：一次性输入所有信息
    新增功能：添加单位
"""

def main():

    y_or_no = input('是否退出程序(y/n)?')
    while y_or_no != 'y':
        # 性别
        # gender = input('性别：')
        # print(type(gender))
        # 身高
        # height = float(input('身高（cm）：'))
        # print(type(height))
        # 体重
        # weight = float(input('体重：'))
        # print(type(weight))
        # 年龄
        # age = int(input('年龄：'))
        # print(type(age))
        print('请输入以下信息，用空格分格')
        input_str = input('性别 身高 体重 年龄：')
        input_str_list = input_str.split(' ')
        gender = input_str_list[0]
        height = float(input_str_list[1])
        weight = float(input_str_list[2])
        age = int(input_str_list[3])


        if gender == '男':
            bmr = (13.7 * weight) + (5.0 * height) - (6.8 * age) + 66
        elif gender == '女':
            bmr = (9.6 * weight) + (1.8 * height) - (age * 4.7) + 655
        else:
            bmr = -1
        if bmr != -1:
            print('您的性别: {}, 体重： {}公斤, 身高： {}厘米, 年龄: {}岁'.format(gender, weight, height, age))
            print('基础代谢率：{}大咖'.format(bmr))
        else:
            print('暂不支持此功能')
        print('********************************')
        y_or_no = input('是否退出程序(y/n)?')
if __name__ == '__main__':
    main()
