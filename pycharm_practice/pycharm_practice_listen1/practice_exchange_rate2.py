'''
    功能：汇率计算
    版本：1.0
    日期：31/3/2019
'''
#coding=utf-8

currency_str_value = input('请输入货币金额(退出程序请输入Q)：')


dollar_to_rmb = 6.77

unit = currency_str_value [-3:]

i = 0
while currency_str_value != 'Q':

    i = i + 1

    print('循环次数是：',i)
    if unit == 'CNY':
        currency_rmb_value = currency_str_value[:-3]

        currency_int_rmb_value = eval(currency_rmb_value)

        value_dollar = currency_int_rmb_value / dollar_to_rmb

        print('你所输入的人民币可兑换美元：',value_dollar)

    elif unit == 'USD':
    # currency_str_value = input('请输入货币金额：')

        currency_usd_value = currency_str_value[:-3]

        currency_int_usd_value = eval(currency_usd_value)

    # dollar_to_rmb = 6.771


        value_rmb = currency_int_usd_value * dollar_to_rmb

        print('你所输入的美元可兑换人民币：',value_rmb)

    else:
        print('该版本属于内测版本，暂不支持此功能，见谅！！！')
    print('**********************************************')
    currency_str_value = input('请输入货币金额(退出程序请输入Q)：')

print('该程序已退出，祝您使用愉快！！')