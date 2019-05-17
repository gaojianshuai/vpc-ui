"""
    网络爬虫：爬电子书网站
    作者：高建帅
    日期：13/04/2019
    版本：1.0
"""
import requests
import re
import urllib3.request
import urllib
from bs4 import BeautifulSoup

def main():
    header = {
        'User - Agent': ' Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.109 Safari/537.36'}
    url = 'http://www.jingcaiyuedu.com/book/370439/list.html'
    req = requests.get(url, headers=header)
    #response = requests.get(noval_url, headers)
    response = urllib3.request.urlopen(req)
    response.encoding = 'utf-8'
    html = response.text
    print(html)
if __name__ == '__main__':
    main()