#coding=utf-8
"""
    版本：6.0
    作者：高建帅
    功能：空气质量计算
    日期：10/04/2019
    新增功能：网络爬虫获取实时信息
    新增功能：将数据保存到csv文件中
    版本：6.0
"""
import requests
import csv
import pandas as pd
def main():
    """
    主函数
    """
    aqi_data = pd.read_csv('china_city_aqi.csv')
    print('基本信息：')
    print(aqi_data.info())

    print('数据预览：')
    print(aqi_data.head())
    #基本统计
    print('AQI最大值：', aqi_data['AQI'].max())
    print('AQI最大值：', aqi_data['AQI'].min())
    print('AQI最大值：', aqi_data['AQI'].mean())

    #全中国top10

    top10_cities = aqi_data.sort_values(by=['AQI']).head(10)
    print('空气质量最好的城市：')
    print(top10_cities)

    #bottom10
    bottom10_cities = aqi_data.sort_values(by=['AQI'], ascending=False).head(10)
    print('空气质量最差的城市：')
    print(bottom10_cities)

    #保存成csv
    top10_cities.to_csv('top10_aqi.csv', index=False)
    bottom10_cities.to_csv('bottom10_aqi.csv', index=False)
if __name__ == '__main__':
    main()