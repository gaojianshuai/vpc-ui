#coding=utf-8
"""
    作者：高建帅
    功能：
    新增功能：
    日期：2019/5/16 22:00
"""
from bs4 import BeautifulSoup
import requests


if __name__=='__main__':
    url = "http://www.jingcaiyuedu.com/novel/bDAfQ.html"
    headers = {
        "User - Agent": "Mozilla / 5.0(WindowsNT6.1;Win64;x64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 74.0.3724.8Safari / 537.36"
    }
    req = requests.get(url=url, headers=headers)
    req.encoding = 'utf-8'
    html = req.text
    # print(html)
    soup = BeautifulSoup(html, 'lxml')
    print(soup.prettify())
    # target_url = soup.find_all(class_='col-md-3')
    # print(target_url)
    # list_url = []
    # for x in target_url:
    #     list_url.append(x.img.get('alt') + '=' + x.get('href'))
    # print(list_url)