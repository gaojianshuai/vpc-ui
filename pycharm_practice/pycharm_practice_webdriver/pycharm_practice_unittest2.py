#encoding=utf-8
import unittest
import smtplib
#被测试类
class myclass(object):
    @classmethod
    def sum(cls, a, b):
        return a + b    #将俩个传入的参数相加操作
    @classmethod
    def sub(cls, a, b):
        return a - b    #将俩个传入的参数相减操作
class mytest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """初始化固件"""
        print('----setUpClass')
    @classmethod
    def tearDownClass(cls):
        """重构类固件"""
        print('----tearDownClass')
    #初始化工作
    def setUp(self):
        self.a = 5
        self.b = 2
        print('--setUp')
    #推出清理工作
    def tearDwon(self):
        print('--tearDown')
    #具体的用例一定要以test开头
    def testsum(self):
        #断言俩数之和的结果是否是7
        self.assertEqual(myclass.sum(self.a , self.b), 7, 'test sum fail')
    def testsub(self):
        # 断言俩数之和的结果是否是3
        self.assertEqual(myclass.sub(self.a , self.b), 3, 'test sub fail')
if __name__ == '__main__':
    unittest.main()