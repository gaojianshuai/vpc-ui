
#conding=utf-8
"""
    版本：4.0
    功能：52周存钱
    作者：高建帅
    日期：03/04/2019
    新增功能：记录每周的存款树
    新增功能：使用for循环
    新增功能：灵活设置每周存钱数，增加的存款树以及存款周数
"""
import math
"""
全局变量和局部变量：全局变量就是在所有函数外，对于任何函数都可用。
而局部变量只能在函数内部！！
"""
saving = 0                      #账户余额
def save_money_in_n_week(money_per_week, increase_money, total_week):
    money_list = []  # 记录存款树
    global saving
    for i in range(total_week):
        # 存钱操作
        # saving += money_per_week

        money_list.append(money_per_week)

        saving = math.fsum(money_list)
        # 输出信息
        print('第几周{}, 存入{}元, 账户累计{}元'.format(i + 1, money_per_week, saving))
        # 更新一周的存钱信息
        money_per_week += increase_money
    print('函数内的saving:',saving)

def main():
    """
    主函数
    """
    money_per_week = float(input('每周存入胡金额：'))             #每周存入的金额
    #i = 1                           #记录周数
    increase_money = int(input('请输入每周的递增金额：'))             #每周递增金额

    total_week = int(input('存款总周数：'))                 #总共的周数

    save_money_in_n_week(money_per_week, increase_money, total_week)
    print('函数外的saving:',saving)

if __name__ == '__main__':
    main()
