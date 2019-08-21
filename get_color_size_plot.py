import os 
import time
import requests
import lxml.etree
import re
from multiprocessing import Pool
import json
import random

print(os.getcwd())
color = list()
size = list()

def read_add(i):
    with open('{}.txt'.format(i),'r+',encoding='gbk') as f:
        for line in f:
            l = json.loads(line)
            size.append(int(l['size']))
            
def write_size():
    with open('size.txt','w+',encoding='utf-8') as f:
        json.dump(size,f)                
if __name__ == '__main__':
    for page in range(1,100):
        filesize = os.path.getsize('{}.txt'.format(page))
        print(page,filesize)
        if  filesize > 100:
            read_add(page)
        else:
            continue
    write_size()
    
    x = list()
    y = list()
    print(min(size),max(size),len(size))
    for i in range(min(size),max(size)+1):
        x.append(i)
        y.append(size.count(i))
        print(i,size.count(i))
        
    
    import matplotlib.pyplot as plt
    plt.figure()
    plt.bar(x,y)
    
    '''
    print(x,y)
    plt.subplot(122)
    si =[i/sum(y) for i in y]
    print(si)
    plt.pie(si)
    '''    
    
    
    
    
    
    