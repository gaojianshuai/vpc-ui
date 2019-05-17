#coding=utf-8
"""
    版本：5.0
    作者：高建帅
    功能：空气质量计算
    日期：10/04/2019
    新增功能：网络爬虫获取实时信息
    新增功能：获取所有城市胡api
    版本：6.0
"""
import requests
from bs4 import BeautifulSoup
def get_city_aqi(city_pinyin):
    """
    返回城市的AQI
    """
    url = 'http://www.pm25.in/' + city_pinyin
    r = requests.get(url, timeout=30)
    soup = BeautifulSoup(r.text, 'lxml')
    div_list = soup.find_all('div', {'class' : 'span1'}) #('div', {'class' : 'span1'})
    city_aqi = []
    for i in range(8):
        div_content = div_list[i]
        caption = div_content.find('div', {'class': 'caption'}).text.strip()
        value = div_content.find('div', {'class': 'value'}).text.strip()
        city_aqi.append((caption, value))
    return city_aqi
def get_all_cities():
    """
    获取所有城市
    """
    url = 'http://www.pm25.in/'
    city_list = []
    r = requests.get(url, timeout=30)
    soup = BeautifulSoup(r.text, 'lxml')
    city_div = soup.find_all('div', {'class': 'bottom'})[1]
    city_link_list = city_div.find_all('a')
    for city_link in city_link_list:
        city_name = city_link.text
        city_pinyin = city_link['href'][1:]
        city_list.append((city_name, city_pinyin))
    return city_list

def main():
    """
    主函数
    """
    city_list = get_all_cities()
    for city in city_list:
        city_name = city[0]
        city_pinyin = city[1]
        city_aqi = get_city_aqi(city_pinyin)
        print(city_name, city_aqi)

    # aqi_div = '''
    # <div class="span12 data">
    #     <div class="span1">
    #       <div class="value">
    #         '''
    # index = url_text.find(aqi_div)
    # begin_index = len(aqi_div) + index
    # end_index = begin_index + 2
    # aqi_val = url_text[begin_index: end_index]
    # print('空气质量为：{}'.format(aqi_val))


if __name__ == '__main__':
    main()