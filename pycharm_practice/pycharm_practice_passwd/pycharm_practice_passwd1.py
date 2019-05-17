#coding=utf-8
"""
    功能：判断密码强弱
    作者：高建帅
    日期：06/04/2019
    版本：1.0
"""

def check_num_exist(passwd):
    """
    判断字符串中是否有数字
    """
    for x in passwd:
        if x.isnumeric():
            return True
    return False
def check_alpha_exist(passwd):
    for x in passwd:
        if x.isalpha():
            return True
    return False

def main():

    passwd = input('请输入密码：')

    strength_level = 0

    if len(passwd) >= 8:
        strength_level += 1
    else:
        print('密码长度至少八位')
    if check_num_exist(passwd):
        strength_level += 1
    else:
        print('密码要求包含数字')
    if check_alpha_exist(passwd):
        strength_level += 1
    else:
        print('密码要求包含字母')
    if strength_level == 3:
        print('密码强度合格')
    else:
        print('密码强度不合格')
if __name__ == '__main__':
    main()