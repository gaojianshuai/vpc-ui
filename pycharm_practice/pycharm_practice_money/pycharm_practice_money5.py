
#conding=utf-8
"""
    版本：5.0
    功能：52周存钱
    作者：高建帅
    日期：03/04/2019
    新增功能：记录每周的存款树
    新增功能：使用for循环
    新增功能：灵活设置每周存钱数，增加的存款树以及存款周数
    新增功能：根据用户输入胡执法犯法，判断是一年中的第几周，然后输入相应胡存款金额
"""
import math
"""
全局变量和局部变量：全局变量就是在所有函数外，对于任何函数都可用。
而局部变量只能在函数内部！！
"""
import datetime
def save_money_in_n_week(money_per_week, increase_money, total_week):
    money_list = []  # 记录存款树
    saved_money_list = []       #每周的账户累计
    saving = 0                      #账户余额
    for i in range(total_week):
        # 存钱操作
        # saving += money_per_week

        money_list.append(money_per_week)
        saving = math.fsum(money_list)
        saved_money_list.append(saving)
        # 输出信息
        print('第几周{}, 存入{}元, 账户累计{}元'.format(i + 1, money_per_week, saving))
        # 更新一周的存钱信息
        money_per_week += increase_money
    return saved_money_list
    print('函数内的saving:',saving)

def main():
    """
    主函数
    """
    money_per_week = float(input('每周存入胡金额：'))             #每周存入的金额
    #i = 1                           #记录周数
    increase_money = int(input('请输入每周的递增金额：'))             #每周递增金额

    total_week = int(input('存款总周数：'))                 #总共的周数

    saved_money_list = save_money_in_n_week(money_per_week, increase_money, total_week)
    week_num = int(input('请输入第几周：'))

    input_date_str = input('请输入日期(yyyy/mm/dd):')
    input_date = datetime.datetime.strptime(input_date_str, '%Y/%m/%d')
    week_num = datetime.datetime.isocalendar(input_date)[1]

    print('第{}周胡存款数: {}元'.format(week_num, saved_money_list[week_num - 1]))
    print('存款的周数：', week_num)

if __name__ == '__main__':
    main()
