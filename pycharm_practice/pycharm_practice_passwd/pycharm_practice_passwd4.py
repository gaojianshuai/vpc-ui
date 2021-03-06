#coding=utf-8
"""
    功能：判断密码强弱
    作者：高建帅
    日期：06/04/2019
    版本：4.0
    新增功能：限制密码次数，循环终止break:跳出整个循环     continue:跳出本次循环，执行下一次循环
    新增功能：保存密码到文件中（操作文件（打开，读写，关闭））
    新增功能：读取文件
"""

def check_num_exist(passwd):
    """
    判断字符串中是否有数字
    """
    has_number = False
    for x in passwd:
        if x.isnumeric():
            has_number = True
            break
    return has_number
def check_alpha_exist(passwd):
    has_alpha = False
    for x in passwd:
        if x.isalpha():
            has_alpha = True
    return has_alpha

def main():

    # try_times = 5
    #
    # while try_times > 0:
    #     passwd = input('请输入密码：')
    #
    #     strength_level = 0
    #
    #     if len(passwd) >= 8:
    #         strength_level += 1
    #     else:
    #         print('密码长度至少八位')
    #     if check_num_exist(passwd):
    #         strength_level += 1
    #     else:
    #         print('密码要求包含数字')
    #     if check_alpha_exist(passwd):
    #         strength_level += 1
    #     else:
    #         print('密码要求包含字母')
    #
    #     f = open('password_3.0.txt', 'a')
    #     f.write('密码：{}, 强度：{}\n'.format(passwd, strength_level))
    #     f.close()
    #
    #     if strength_level == 3:
    #         print('密码强度合格')
    #
    #         break
    #     else:
    #         print('密码强度不合格')
    #         try_times -= 1
    #     print('*****************************')
    #
    # if try_times <= 0:
    #     print('尝试密码次数过多，输入失败')
    #读取文件
    f = open('password_3.0.txt', 'r')
    #第一种读取文件方法read()
    # content = f.read()
    # f.readline()
    # f.close()
    # print(content)
    #第二种读取文件方法readline()
    # line = f.readline()
    # print(line)
    # line = f.readline()
    # print(line)
    #第三种读取文件方式(返回是list)readlines()
    #line = f.readlines()
    for line in f.readlines():
        print(line)
    f.close()
if __name__ == '__main__':
    main()