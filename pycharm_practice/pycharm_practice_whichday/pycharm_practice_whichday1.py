#conding=utf-8
'''
    功能：输入某年某月某日，判断是一年中的第几天
    版本：1.0
    作者：高建帅
    日期：05/04/2019
'''

import datetime

def main():


    input_date_str = input('请输入日期(yyyy/mm/dd):')

    input_date = datetime.datetime.strptime(input_date_str, '%Y/%m/%d')

    print(input_date)

    year = input_date.year
    month = input_date.month
    day = input_date.day

    day_in_month_tup = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
    print(day_in_month_tup[: month - 1])
    days = sum(day_in_month_tup[: month - 1]) + day

    if (year % 400 == 0) or ((year % 4 == 0) and (year % 100 != 0)):

        if month > 2:
            days += 1
    print ('这是第{}天'.format(days))



if __name__ == '__main__':
    main()