# 从别的资源取数据拿来用
# -*- coding:utf-8 -*-
import urllib.request
import web
from json import *
import time
import web
import mysql.connector

movie_ids=[]
for index in range(0,250,50):
    #如果不加上下面的这行出现会出现urllib2.HTTPError: HTTP Error 403: Forbidden错误
    #主要是由于该网站禁止爬虫导致的，可以在请求加上头信息，伪装成浏览器访问User-Agent
    headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.94 Safari/537.36'}
    req=urllib.request.Request('http://api.douban.com/v2/movie/top250?start=%d&count=50' %index,headers=headers)
    response=urllib.request.urlopen(req)
    #得到读取的数据信息，并且是json格式
    data=response.read()


    #将json格式转换成dict对象：
    #下面加这行，不加会TypeError: can't use a string pattern on a bytes-like object
    data=data.decode('utf8')
    data_dict=JSONDecoder().decode(data)

    #dict类型的结果中，subjects对应的是影片的List
    movie250=data_dict['subjects']

    #取到250个电影的id
    for movie in movie250:
        movie_ids.append(movie['id'])

    time.sleep(3)#避免连续请求太快，每次停留3秒钟

db1=mysql.connector.connect(host='localhost',port ='3306',db='moviesite', user='root',password='090416',charset="utf8")
db=db1.cursor()
   
def add_movie(data):
    movie=data
    param=(int(movie['id']),movie['title'],movie["original_title"],movie['alt'],movie['rating']['average'],\
movie['images']['large'],','.join([d['name'] for d in movie['directors']]),\
','.join([c['name'] for c in movie['casts']]),int(movie['year']),\
','.join(movie['genres']),movie['countries'][0],movie['summary'])
    #说明sql语句用''而%d和%s用""是因为有可能param中值中有'符号，不然会报错
    db.execute('insert into movie_api(id,title,origin,url,rating,image,directors,casts,year,genres,countries,summary) VALUES("%d","%s", "%s", "%s", "%s", "%s", "%s", "%s", "%d", "%s", "%s", "%s")' %param)

count=0
for mid in movie_ids:
    try:
        
        headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.94 Safari/537.36'}
        req=urllib.request.Request('http://api.douban.com/v2/movie/subject/%s' % mid,headers=headers)
        response=urllib.request.urlopen(req)
        #得到读取的数据信息，并且是json格式
        data=response.read()
        data=data.decode('utf8')
        data1=JSONDecoder().decode(data)
        add_movie(data1)
    except:
        print("not find")
    count+=1
    print(count)
    time.sleep(3)
    
db1.commit()
db.close()
db1.close()


    
