#coding=utf-8
"""
    功能：模拟掷色子
    作者：高建帅
    日期：07/04/2019
    版本：3.0
    新增功能:模拟俩个筛子
    新增功能：可视化投掷俩个筛子结果

"""
import random
import matplotlib
import matplotlib.pyplot as plt

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
    #初始化点数列表
    roll_list = list(range(2,13))
    roll_dict = dict(zip(roll_list, result_list))
    #记录第一个筛子结果
    roll1_list = []
    roll2_list = []
    for i in range(total_times):
        roll1 = roll_dice()
        roll2 = roll_dice()

        roll1_list.append(roll1)
        roll2_list.append(roll2)
        for j in range(2,13):
            if (roll1 + roll2) == j:
                roll_dict[j] += 1
    for i, result in roll_dict.items():
        print('点数{}的次数：{}, 频率：{}'.format(i, result, result / total_times))
    #数据可视化
    x = range(1, total_times + 1)
    plt.scatter(x, roll1_list, c = 'green', alpha=0.5)
    plt.scatter(x, roll2_list, c = 'red', alpha=0.5)
    plt.show()

if __name__ == '__main__':
    main()