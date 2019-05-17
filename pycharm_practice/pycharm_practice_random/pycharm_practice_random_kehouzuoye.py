#coding=utf-8
"""
    功能：模拟掷色子
    作者：高建帅
    日期：07/04/2019
    版本：5.0
    新增功能:模拟俩个筛子
    新增功能：可视化投掷俩个筛子结果
    新增功能：直方图
    新增功能：科学计算
    课后作业：投掷三个筛子

"""
import random
import matplotlib.pyplot as plt
import numpy
import numpy as np

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
    total_times = 10000
    #初始化列表 [0, 0, 0, 0, 0, 0,]
    #result_list = [0] * 11
    roll1_arr = np.random.randint(1, 7, size=total_times)
    roll2_arr = np.random.randint(1, 7, size=total_times)
    roll3_arr = np.random.randint(1, 7, size=total_times)
    result_arr = roll2_arr + roll1_arr + roll3_arr
    hist, bins = np.histogram(result_arr, bins=range(3, 21))
    print(hist)
    print(bins)
    #数据可视化
    tick_labels = ['3点', '4点', '5点',
                   '6点', '7点', '8点', '9点',
                   '10点', '11点', '12点', '13点', '14点', '15点', '16点'
                   , '17点', '18点']
    tick_pos = np.arange(3, 21) + 0.5
    plt.xticks(tick_pos, tick_labels)
    plt.hist(result_arr, bins=range(3, 21), edgecolor='black', normed=1, linewidth=2, rwidth=0.5)
    plt.title('筛子点数统计')
    plt.xlabel('点数之和统计')
    plt.ylabel('频率')
    plt.show()

if __name__ == '__main__':
    main()