#coding=utf-8
"""
    作者：高建帅
    功能：
    新增功能：
    日期：2019/5/19 17:01
"""

import requests
from lxml import etree
import re
import time
#下载得方法
from urllib.request import urlretrieve

def Download(url):
    url = 'http://www.pearvideo.com/category_9'
    html = requests.get(url, 'lxml').text
    html = etree.HTML(html)
    # print(html)
    start_url = 'http://www.pearvideo.com'
    #获取视频后缀id
    video_id = html.xpath('//div[@class="vervideo-bd"]/a/@href')
    # print(video_id)
    video_url = []
    for id in video_id:
        # print(id)
        #拼接完整url
        new_url = start_url + '/' + id
        video_url.append(new_url)
        # print(video_url)

    for playurl in video_url:
        # print(playurl)
        html = requests.get(playurl).text
        # print(html)
        #正则匹配,匹配所有
        req = 'srcUrl="(.*?)"'
        # req = re.compile(req)
        #视频真正播放地址  list
        purl = re.findall(req, html)
        # print(purl)
        #获取标题名字
        req = '<h1 class="video-tt">(.*?)</h1>'
        pname = re.findall(req, html)
        print("正在下载视频：%s"%pname)
        #下载得url   下载得地址也是目录
        urlretrieve(purl[0], 'video/%s.mp4'%pname[0])

def downloadmore():
    n = 0
    #动态加载
    while True:
        if n > 60:
            return
        else:
            url = 'http://www.pearvideo.com/category_loading.jsp?reqType=5&categoryId=9&start=%d'%n
            n = n + 12
            time.sleep(5)
            Download(url)

downloadmore()

# http://www.pearvideo.com/category_loading.jsp?reqType=5&categoryId=9&start=24&mrd=0.0996742905809862&filterIds=1556075,1556064,1556133,1555869,\
# 1555830,1555767,1555807,1555771,1555604,1555567,1555541,1555478,1555499,1555260
# http://www.pearvideo.com/category_loading.jsp?reqType=5&categoryId=9&start=36&mrd=0.9312429331616181&filterIds=1556075,1556064,1556133,1555188,\
# 1555053,1554935,1554931,1554852,1554723,1554691,1554457,1554466,1554374,1554344,1554198
# http://www.pearvideo.com/category_loading.jsp?reqType=5&categoryId=9&start=48&mrd=0.6905603740183717&filterIds=1556075,1556064,1556133,1554083,\
# 1553988,1553981,1553892,1553871,1553800,1553693,1553680,1553633,1553574,1553506,1553347



