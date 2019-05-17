#coding=utf-8
import unittest
import random

class TestSequenceFunctions(unittest.TestCase):
    def setUpClass(self):
    #初始化一个递增实力
        self.seq = range(10)
    def runTest(self):
        #从序列seq中随机抽取一个元素
        element = random.choice(self.seq)
        #验证随机抽取得元素确实在列表中

        self.assertTrue(element in self.seq)
        print(element)






if __name__ == '__main__':
    unittest.main()