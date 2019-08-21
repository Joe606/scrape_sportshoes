# -*- coding: utf-8 -*-
"""
从爬取的json数据中提取几个关键点：
用户     "id""content""creationTime""productColor""productSize"
用户评价
购买鞋子颜色
鞋子尺码
"""
import os 
import time
import requests
import lxml.etree
import re
from multiprocessing import Pool
import json
import random

def read_file(page):
    with open('shoes{}.txt'.format(page),'r+',encoding='utf-8') as f:
        x = json.load(f)
        print(type(x))  #json文件的数据本质就是字符串
        #print(x)
        
        for k in x.keys():
            print(k)
        fw = open('99pages coverage/{}.txt'.format(page),'w+',)
        three_elements = dict()
        for i in range(0,len(x['comments'])):
            comment = x['comments'][i] 
            print('用户ID:',comment['id'],
              '鞋子颜色：',comment['productColor'],
              '鞋子尺码：',comment['productSize'])
            three_elements['id'] = comment['id']
            three_elements['color'] = comment['productColor']
            three_elements['size'] = comment['productSize']
            three_elements['content'] = comment['content']
            
            json.dump(three_elements,fw,ensure_ascii=False) #确保中文保存
            fw.write('\n')

if __name__ == '__main__':
    for page in range(1,100):
        filesize = os.path.getsize('shoes{}.txt'.format(page))
        print(page,filesize)
        if  filesize > 100:
            read_file(page)
        else:
            with open('99pages coverage/{}.txt'.format(page),'w') as f:
                f.write('dddd')
            continue
            
        
        
        
        
        
        
        
        
        