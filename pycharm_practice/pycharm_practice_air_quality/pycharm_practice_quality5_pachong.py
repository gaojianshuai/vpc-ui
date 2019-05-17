#coding=utf-8
"""
    版本：4.0
    作者：高建帅
    功能：空气质量计算
    日期：10/04/2019
    新增功能：网络爬虫获取实时信息
    版本：5.0
"""
import requests
def get_html_text(url):
    """
    返回url的文本
    """
    r = requests.get(url, timeout=30)
    print(r.status_code)
    return r.text

def main():
    """
    主函数
    """
    city_pinyin = input('请输入城市拼音：')
    url = 'http://www.pm25.in/' + city_pinyin
    url_text = get_html_text(url)

    aqi_div = '''
    <div class="span12 data">
        <div class="span1">
          <div class="value">
            '''
    index = url_text.find(aqi_div)
    begin_index = len(aqi_div) + index
    end_index = begin_index + 2
    aqi_val = url_text[begin_index: end_index]
    print('空气质量为：{}'.format(aqi_val))


if __name__ == '__main__':
    main()