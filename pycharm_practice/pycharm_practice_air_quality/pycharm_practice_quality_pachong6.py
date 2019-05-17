#coding=utf-8
"""
    版本：6.0
    作者：高建帅
    功能：空气质量计算
    日期：10/04/2019
    新增功能：网络爬虫获取实时信息
    新增功能：将数据保存到csv文件中
    版本：7.0
    新增功能：数据清洗
"""
import requests
import csv
import matplotlib.pyplot as plt
import pandas as pd
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
def main():
    """
    主函数
    """
    aqi_data = pd.read_csv('china_city_aqi.csv')
    print('基本信息：')
    print(aqi_data.info())

    print('数据预览：')
    print(aqi_data.head())

    #数据清洗
    #只保留大于0的AQI数据
    filter_condition = aqi_data['AQI'] > 0
    clean_aqi_data = aqi_data[filter_condition]
    #基本统计
    print('AQI最大值：', clean_aqi_data['AQI'].max())
    print('AQI最小值：', clean_aqi_data['AQI'].min())
    print('AQI最大值：', clean_aqi_data['AQI'].mean())

    #全中国top10

    top50_cities = clean_aqi_data.sort_values(by=['AQI']).head(50)
    print('空气质量最好的城市：')
    print(top50_cities)
    top50_cities = clean_aqi_data.sort_values(by=['AQI']).head(50)
    top50_cities.plot(kind='bar', x='City', y='AQI', title='空气质量最好的五十个城市',
                      figsize=(20, 10))
    plt.savefig('top_aqi_bar.png')
    plt.show()
if __name__ == '__main__':
    main()