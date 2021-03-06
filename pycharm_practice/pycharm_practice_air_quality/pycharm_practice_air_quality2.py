#coding=utf-8
"""
    版本：2.0
    作者：高建帅
    功能：空气质量计算
    日期：09/04/2019
    新增功能：读取已经获取json(JavaScript Object Notation)数据文件,一种轻量级数据交换格式
    这个py缺少j文件
"""
import json

def process_json_file(filepath):
    """
    解码json文件
    """
    f = open(filepath, mode='r', encoding='utf-8')
    #将json文件转换成python格式load
    city_list = json.load(f)
    print(city_list)
def main():
    """
    主函数
    """
    filepath = input('请输入json文件名称：')
    city_list = process_json_file(filepath)
    city_list.sort(key=lambda city: city['aqi'])
    top5_list = city_list[:5]
    f = open('top5_aqi.json', mode='w', encoding='utf-8')
    json.dump(top5_list, f, ensure_ascii=False)
    f.close()
    print(city_list)
if __name__ == '__main__':
    main()