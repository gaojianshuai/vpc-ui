#coding=utf-8
"""
    版本：4.0
    作者：高建帅
    功能：空气质量计算
    日期：09/04/2019
    新增功能：读取已经获取json(JavaScript Object Notation)数据文件,一种轻量级数据交换格式
    这个py缺少j文件
    新增功能：csv文件操作通用的简单的文件格式
    新增功能：判断文件是不是json或者csv格式
"""
import csv
import os
import json
def process_json_file(filepath):
    """
    解码json文件
    """
    # f = open(filepath, mode='r', encoding='utf-8')
    # #将json文件转换成python格式load
    # city_list = json.load(f)
    # print(city_list)
    with open(filepath, mode='r', encoding='utf-8') as f:
        city_list = json.load(f)
    print(city_list)

def process_csv_file(filepath):
    """
    解码csv文件
    """
    with open(filepath, mode='r', encoding='utf-8', newline='') as f:
        reader = csv.reader(f)
        for row in reader:
            print(', '.join(row))

def main():
    """
    主函数
    """
    filepath = input('请输入文件名称：')
    filename, file_ext = os.path.splitext(filepath)
    if file_ext == '.json':
        process_json_file()
    elif file_ext == '.csv':
        process_csv_file()
    else:
        print('不支持此格式文件;')
    city_list = process_json_file(filepath)
    city_list.sort(key=lambda city: city['aqi'])
    lines = []
    #获取列名
    lines.append(list(city_list[0].keys()))
    for city in city_list:
        lines.append(list(city.values()))
    f = open('aqi.csv', 'w', encoding='utf-8', newline='')
    writer = csv.writer(f)
    for line in lines:
        writer.writerow(line)
    f.close()
    print(city_list)
if __name__ == '__main__':
    main()