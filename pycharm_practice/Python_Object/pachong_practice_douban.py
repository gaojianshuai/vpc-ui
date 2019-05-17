#coding=utf-8
"""
    作者：高建帅
    功能：
    新增功能：
    日期：2019/5/16 23:22
"""

from bs4 import BeautifulSoup
import requests

url = 'https://book.douban.com/top250?start=0'
response = requests.get(url)
#print(response.text)
soup = BeautifulSoup(response.text, 'lxml')
#find_all()方法
#class是python得关键词，所以要加下划线_
divall = soup.find_all('div', class_='p12')
for i in divall:
    names = i.find('a')['title']
    print('find_all():', names)

#find方法
divall2 = soup.find('div', class_='p12')
names2 = divall2.find('a')['title']
print('find():', names2)
