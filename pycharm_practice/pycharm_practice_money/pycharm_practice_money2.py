
#conding=utf-8
"""
    版本：2.0
    功能：52周存钱
    作者：高建帅
    日期：03/04/2019
    新增功能：记录每周的存款树
"""
import math
def main():
    """
    主函数
    """
    money_per_week = 10             #每周存入的金额
    i = 1                           #记录周数
    increase_money = 10             #每周递增金额
    saving = 0                      #账户余额
    total_week = 52                 #总共的周数

    money_list = []                 #记录存款树

    while i <= total_week:
        #存钱操作
        #saving += money_per_week

        money_list.append(money_per_week)

        saving = math.fsum(money_list)
        #输出信息
        print('第几周{}, 存入{}元, 账户累计{}元'.format(i, money_per_week, saving))
        #更新一周的存钱信息
        money_per_week += increase_money
        i += 1

if __name__ == '__main__':
    main()
