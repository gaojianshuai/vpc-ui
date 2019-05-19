#coding=utf-8
"""
    作者：高建帅
    功能：
    新增功能：
    日期：2019/5/19 19:45
"""

import requests
import re
import time, os, sys
from urllib.request import urlretrieve
from lxml import etree

def download():

    url = 'https://www.qisuu.la/soft/sort01/'
    headers = {
        "User - Agent": "Mozilla / 5.0(WindowsNT6.1;Win64;x64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 74.0.3724.8Safari / 537.36"
    }
    html = requests.get(url, 'lxml').text
    html = etree.HTML(html)
    # print(html)
    start_url = 'https://www.qisuu.la'
    text_id = html.xpath('/html/body/div[4]/div[2]/div/ul/li/a/@href')
    test_descprition = html.xpath('/html/body/div[4]/div[2]/div/ul/li/a/text()')
    # print(test_descprition)
    text_list = []
    for id in text_id:

        new_url = start_url + id
        # id_list = re.findall(r"\d+", str(text_list))
        # number = new_url.split()
        number = re.findall("\d+", new_url)[0]
        first_number = number[0:2]

        # print(namelist)
        start_download_url = 'https://dzs.qisuu.la/' + str(first_number) + '/' + str(number) + '/'
        for name in test_descprition:
            namelist = re.findall("《(.*)》", name)[0]
            # print(namelist)
            # urlretrieve()
            final_download = start_download_url + namelist + '.txt'
            print(final_download)


download()

