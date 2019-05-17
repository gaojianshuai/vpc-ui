#coding=utf-8
"""
    功能：模拟掷色子
    作者：高建帅
    日期：07/04/2019
    版本：4.0
    新增功能:模拟俩个筛子
    新增功能：可视化投掷俩个筛子结果
    新增功能：直方图

"""
import random
import matplotlib.pyplot as plt
#解决中文显示报错问题
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
def roll_dice():
    """
    模拟掷色子
    """
    roll = random.randint(1, 6)
    return roll
def main():
    total_times = 100
    #初始化列表 [0, 0, 0, 0, 0, 0,]
    result_list = [0] * 11

    #记录第一个筛子结果
    roll_list = []
    for i in range(total_times):
        roll1 = roll_dice()
        roll2 = roll_dice()

        roll_list.append(roll1 + roll2)

    #数据可视化
    plt.hist(roll_list, bins=range(2, 14), edgecolor='black', normed=1, linewidth=2)
    plt.title('筛子点数统计')
    plt.xlabel('点数之和统计')
    plt.ylabel('频率')
    plt.show()
if __name__ == '__main__':
    main()