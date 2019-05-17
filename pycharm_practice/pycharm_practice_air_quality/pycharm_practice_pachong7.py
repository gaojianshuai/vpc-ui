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

#如果不加上下面的这行出现会出现urllib2.HTTPError: HTTP Error 403: Forbidden错误
    #主要是由于该网站禁止爬虫导致的，可以在请求加上头信息，伪装成浏览器访问User-Agent,具体的信息可以通过火狐的FireBug插件查询
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.109 Safari/537.36'}
    chaper_url = 'http://www.jingcaiyuedu.com/book/370439/list.html'
    req = urllib.request.Request(url=chaper_url, headers=headers)
    urllib.request.urlopen(req).read()