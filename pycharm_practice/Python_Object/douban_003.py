#coding=utf-8
"""
    作者：高建帅
    功能：
    新增功能：
    日期：2019/5/17 0:06
"""

import requests
import os,time
from fake_useragent import UserAgent
#创建用户认证
from multiprocessing import Process
ua = UserAgent(verify_ssl=False)

def Downloader(url, path):
    """视频下载"""
    headers = {
        "User-Agent": ua.random
    }
    #开始下载事件
    start = time.time()
    #模拟用户请求下载地址
    response = requests.get(url, headers=headers, stream=True)
    #每次下载数据大小
    chunk_size = 1024
    #数据得总大小
    #content_size = int(resonse.headers['Content-Length'])
    #判断请求成功才下载
    if response.status_code ==200:
        print('[文件大小：{}mb]'.format(chunk_size / 1024))
        #w 文件存在就写入,不存在就创建，b 是二进制读写操作
        with open(path, 'wb') as file:
            for data in response.iter_content(chunk_size=chunk_size):
                file.write(data)
                size = size + len(data)
                print('[下载进度]:{}{}%'.format('>' * int(size * 50), float(size * 100)),end='')
    end = time.time()
    print('视频下载完成！用时:{}'.format(end - start))


def The_URL(page):
    url = 'http://api.vc.bilibili.com/board/v1/ranking/top?page_size=10&next_offset={}&tag=%E4%BB%8A%E6%97%A5%E7%83%AD%E9%97%A8&platform=pc'.format(page)
    headers = {
        "User-Agent": ua.random
    }
    resp = requests.get(url, headers=headers).json()
    item = resp.get('data').get('items')
    print(item)
    for i in item:
        ite = i.get('item')
        #视频标题
        Vedio_name = ite.get('description')
        # print(Vedio_name)
        # #发布事件
        # Release_time = ite.get('upload_time')
        # print(Release_time)
        #视频得下载地址
        Vedio_download_like = ite.get('video_playurl')
        try:
            Downloader(Vedio_download_like, path='{}.mp4'.format(Vedio_name))
        except Exception as e:
            print(e.args)

        #print(Vedio_download_like)
        # #视频观看地址
        # Vedio_see_like = ite.get('share_url')
        # print(Vedio_see_like)
        # The_author_name = i.get('user').get('name')
        # print(The_author_name)
# for i in range(100):
#     i = i * 10 + 1
#     The_URL(i)

if __name__ == '__main__':
    #创建一个进程
    t1 = Process(target=The_URL, args=(int,))
    #启动进程
    t1.start()
    t1.join()