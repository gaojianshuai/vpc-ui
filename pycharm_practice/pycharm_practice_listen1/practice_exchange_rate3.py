'''
    功能：汇率计算
    版本：2.0
    日期：31/3/2019
    增加功能：将汇率兑换成功能封装成函数
'''
#coding=utf-8
def convert_currency(im, er):
    out = im * er
    return out
currency_str_value = input('请输入货币金额(退出程序请输入Q)：')

dollar_to_rmb = 6.77
unit = currency_str_value [-3:]
if unit == 'CNY':
    exchange_rate = 1 / dollar_to_rmb
elif unit == 'USD':
    exchange_rate = dollar_to_rmb
else:
    exchange_rate = -1
    print('该版本属于内测版本，暂不支持此功能，见谅！！！')

if exchange_rate != -1:
    in_money = eval(currency_str_value[:-3])
    #调用函数
    out_money = convert_currency(in_money, exchange_rate)
    print('准换后胡金额：',out_money)
else:
    print('暂不支持该货币！！！')