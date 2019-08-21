how# -*- coding: utf-8 -*-
import pymysql
import time
import json
import os

#create a table callled all_comments
def new_table():
    sql = '''
    create table all_comments
    (num int(10) auto_increment not null primary key,id text,content text,score text,productColor text,productSize text);  
    '''
    cur.execute(sql)
    db.commit()
    
        
#load data in a text file into the new table in database
def read_to_database():
    i = 0
    for c in y:
        i += 1
        sql = '''insert into all_comments
        (id,content,score,productColor,productSize) values
        ('%s','%s','%s','%s','%s');'''  %(c['id'],c['content'],c['score'],c['productColor'],c['productSize'])
        print(sql) 
        cur.execute(sql)
        db.commit()
        print(i)
                        
if __name__ == '__main__':
    db = pymysql.connect(host='localhost',user='root',passwd='208294',database='男运动鞋')
    cur = db.cursor()
    
    print(os.getcwd())
    new_table()
    for j in range(1,100):
        f = open('shoes{}.txt'.format(j),'r+',encoding='utf-8')
        x = json.load(f)
        y = x['comments']
        print(type(y))
        
        read_to_database()
    
    cur.close()
    db.closer()



























    
    