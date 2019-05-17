#coding=utf-8
"""
    功能：模拟掷色子
    作者：高建帅
    日期：07/04/2019
    版本：1.0
    新增功能：获取每个元素胡索引和value
"""
import random

def roll_dice():
    """
    模拟掷色子
    """
    roll = random.randint(1, 6)
    return roll
def main():
    total_times = 100
    #初始化列表 [0, 0, 0, 0, 0, 0,]
    result_list = [0] * 6

    for i in range(total_times):
        roll = roll_dice()
        for j in range(1,7):
            if roll == j:
                result_list[j - 1] += 1
    for i, result in enumerate(result_list):
        print('点数{}的次数：{}, 频率：{}'.format(i + 1, result, result / total_times))


if __name__ == '__main__':
    main()