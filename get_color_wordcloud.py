# -*- coding: utf-8 -*-
import pymysql
import time
import os
import matplotlib.pyplot as plt

print(os.getcwd())
db = pymysql.connect(
        host='localhost',
        user='root',
        passwd='xxxx',
        database='男运动鞋'
        )
cur = db.cursor()

cur.execute('select productSize from all_comments;')
all_size = cur.fetchall()
size = list()
for i in all_size:
    j = int(i[0])
    size.append(j)
    
print(size)

x = range(1,len(size)+1)  
y = size  
plt.figure()
plt.scatter(x,y,c='green')
plt.title('distribution about size of shoes')
plt.xlabel('man',color='b')
plt.ylabel('size of shoes',color='r')
plt.annotate('size',(1,42))
plt.legend('point')
plt.show()
plt.savefig('size.jpg')

import wordcloud
import jieba
cur.execute('select productColor from all_comments;')
all_color = cur.fetchall()
color = str()
for i in all_color:
    j = i[0]
    color = color +','+ j
print(type(color),color.count('/'))    
color = color.replace('/',',')    
print(color)
#mytext = ''.join(jieba.cut(color))
#print(mytext)
wc = wordcloud.WordCloud(
        collocations=False,
        font_path='simfang.ttf',
        background_color='black',
        max_words=5000,
        max_font_size=300,
        width=1200,
        height=600,
        margin=2,
        )
wc = wc.generate(text=color)
plt.imshow(wc)
plt.axis('off')
plt.show()
wc.to_file('wordcloud.png')

si = str()
for i in size:
    si = si + ',' + str(i)
    
si = si + ',' + 'black'    
print(si)
print(type(si)) 
   
wc2 = wordcloud.WordCloud(collocations=False).generate(si)
plt.imshow(wc2)
plt.show()
wc2.to_file('wc2.jpg')














