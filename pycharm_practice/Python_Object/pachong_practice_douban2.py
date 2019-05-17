#coding=utf-8
"""
    作者：高建帅
    功能：
    新增功能：
    日期：2019/5/16 23:22
"""

from bs4 import BeautifulSoup
import requests
import os
import time


def get_html(url):

    # 获取所有页面
    #url = "http://jandan.net/ooxx/"
    headers = {
        "User - Agent": "Mozilla / 5.0(WindowsNT6.1;Win64;x64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 74.0.3724.8Safari / 537.36"
    }
    resp = requests.get(url, headers=headers)
    # print(resp.text)
    #代理，免费得代理智能使用一会可能就没了，自行更换
    proxies = {'http': '111.23.10.27:8080'}
    try:
        #requests库得get请求
        resp = requests.get(url, headers=headers)
    except:
        #如果请求受阻，则使用代理
        resp = requests.get(url, headers=headers, proxies=proxies)
    return resp
def all_page():
    #获取所有页面
    base_url = "http://jandan.net/ooxx/"
    headers = {
        "User - Agent": "Mozilla / 5.0(WindowsNT6.1;Win64;x64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 74.0.3724.8Safari / 537.36"
    }
    #resp = requests.get(url=base_url, headers=headers)
    # print(resp.text)
    soup = BeautifulSoup(get_html(base_url).text, 'lxml')
    allpage = soup.find('span', class_='current-comment-page').get_text()[1:-1]
    urllist = []
    for page in range(1, int(allpage)+1):
        allurl = base_url + 'page-' + str(page)
        urllist.append(allurl)
    print(urllist)
    return urllist

#创建文件夹得函数，并保存到C盘
    # os.path.exists(name)判断是否存在路径
    # os.path.join(path, name)连接目录与文件名
def mkdir(path):
    isExists= os.path.exists(os.path.join("D:\jiandan", path))
    if not isExists:
        print('makedir', path)
        #创建目录
        os.makedirs(os.path.join("D:\jiandan", path))
        #切换进入该目录
        os.chdir(os.path.join("D:\jiandan", path))
        return True
    else:
        print(path, 'already exist')
        return False
#获取图片地址调用download来下载
def get_img():
    #调用函数获取所有页面
    for url in all_page():
        path = url.split('-')[-1]
        #创建文件夹函数
        mkdir(path)
        #请求函数获取html源码
        html = get_html(url).text
        # 使用lxml解析器，也可以使用html.parser
        soup = BeautifulSoup(html, 'lxml')
        allimgs = soup.select('div.text > p > img')
        download(allimgs)
    print('ok')

# 保存图片函数，传入的参数是一页所有图片url集合
def download(list):
    for img in list:
        urls = img['src']
        # 判断url是否完整
        if urls[0:5] == 'http:':
            img_url = urls

        else:
            img_url = 'http:' + urls
        filename = img_url.split('/')[-1]
        with open(filename, 'wb') as f:
        # 直接过滤掉保存失败的图片，不终止程序
            try:
                f.write(get_html(img_url).content)
                print('Sucessful image:',filename)
            except:
                print('Failed:', filename)

if __name__=='__main__':
    #计时
    t1 = time.time()
    #调用函数
    get_img()
    print(time.time() - t1)