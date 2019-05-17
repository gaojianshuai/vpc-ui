#coding=utf-8
"""
    功能：判断密码强弱
    作者：高建帅
    日期：07/04/2019
    版本：6.0
    新增功能：限制密码次数，循环终止break:跳出整个循环     continue:跳出本次循环，执行下一次循环
    新增功能：保存密码到文件中（操作文件（打开，读写，关闭））
    新增功能：读取文件
    新增功能：将相关方法封装成一个整体（面向对象编程OOP）定义一个passwd工具类
    新增功能：定义一个文件操作工具类
"""

class PasswdTool:
    """
    密码工具类
    """
    def __init__(self, passwd):
        self.passwd = passwd
        self.strength_level = 0

    def process_passwd(self):
        if len(self.passwd) >= 8:
            self.strength_level += 1
        else:
            print('密码长度至少八位')
        if self.check_num_exist():
            self.strength_level += 1
        else:
            print('密码要求包含数字')
        if self.check_alpha_exist():
            self.strength_level += 1
        else:
            print('密码要求包含字母')
    #类的方法
    def check_num_exist(self):
        """
        判断字符串中是否有数字
        """
        has_number = False
        for x in self.passwd:
            if x.isnumeric():
                has_number = True
                break
        return has_number

    def check_alpha_exist(self):
        has_alpha = False
        for x in self.passwd:
            if x.isalpha():
                has_alpha = True
        return has_alpha

class FileTool:
    """
    定义文件工具类
    """
    def __init__(self, filepath):
        self.filepath = filepath
    def write_to_file(self, line):
        f = open(self.filepath, 'a')
        f.write(line)
        f.close()

    def read_to_file(self, filepath):
        f = open(self.filepath, 'r')
        lines = f.readlines()
        f.close()
        return lines

def main():

    try_times = 5
    filepath = 'passwd6.0.txt'
    # 实例化文件工具对象
    file_tool = FileTool(filepath)
    while try_times > 0:
        passwd = input('请输入密码：')
        #实例化密码工具对象
        passwd_tool = PasswdTool(passwd)
        passwd_tool.process_passwd()
        strength_level = 0


        line = '密码：{}, 强度：{}\n'.format(passwd, passwd_tool.strength_level)
        file_tool.write_to_file(line)
        #写文件
        f = open('password_5.0.txt', 'a')
        f.write('密码：{}, 强度：{}\n'.format(passwd, passwd_tool.strength_level))
        f.close()

        if passwd_tool.strength_level == 3:
            print('密码强度合格')

            break
        else:
            print('密码强度不合格')
            try_times -= 1
        print('*****************************')

    if try_times <= 0:
        print('尝试密码次数过多，输入失败')
    #读操作
    lines = file_tool.read_to_file(filepath)
    print (lines)
if __name__ == '__main__':
    main()