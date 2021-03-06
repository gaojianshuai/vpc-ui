#conding=utf-8
'''
    功能：输入某年某月某日，判断是一年中的第几天
    版本：3.0
    作者：高建帅
    日期：05/04/2019
    新增功能：元组改成列表
    新增功能：将月份化为不同的集合进行操作集合｛｝
'''

import datetime

def is_leap_year(year):
    is_leap = False
    if (year % 400 == 0) or ((year % 4 == 0) and (year % 100 != 0)):
        is_leap = True
    return is_leap

def main():


    input_date_str = input('请输入日期(yyyy/mm/dd):')

    input_date = datetime.datetime.strptime(input_date_str, '%Y/%m/%d')

    print(input_date)

    year = input_date.year
    month = input_date.month
    day = input_date.day
    # days = sum(day_in_month_tlist[: month - 1]) + day
    _30_day_month_set = {4, 6, 9, 11}
    _31_day_monty_set = {1, 3, 5, 7, 8, 10, 12}
    days = 0
    days += day
    for i in range(1, month):
        if i in _30_day_month_set:
            days += 30
        elif i in _31_day_monty_set:
            days += 31
        else:
            days += 28
    if is_leap_year(year) and i > 2:
        days += 1



    print ('这是第{}天'.format(days))



if __name__ == '__main__':
    main()