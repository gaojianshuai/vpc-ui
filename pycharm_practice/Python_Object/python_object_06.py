#coding=utf-8

"""
    作者：高建帅
    日期：14/05/2019
    功能：类的继承（直接在类名后面的括号里填入要继承类的类名）
    新增功能：网络爬虫-----小甲鱼
"""
# -*- coding:UTF-8 -*-
from bs4 import BeautifulSoup
import requests

if __name__=='__main__':
    url = 'http://www.shuaia.net/index.html'
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
    }
    req = requests.get(url=url, headers=headers)
    req.encoding = 'utf-8'
    html = req.text
    bf = BeautifulSoup(html, 'lxml')
    targets_url = bf.find_all(class_='item-img')
    list_url = []
    for each in targets_url:
        list_url.append(each.img.get('alt') + '=' + each.get('href'))
    print(list_url)