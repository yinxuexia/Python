#下载影片图片，并存放在本地供使用,页面上直接显示自身服务器的图片
import urllib.request
import mysql.connector
import time

def get_poster(id,url):
    headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.94 Safari/537.36'}
    req=urllib.request.Request(url,headers=headers)
    response=urllib.request.urlopen(req)
    pic=response.read()
    file_name=('e:/results/Python/static/poster/%d.jpg'%id)
    f=open(file_name,"wb")
    f.write(pic)
    f.close


db1=mysql.connector.connect(host='localhost',port ='3306',db='MovieSite', user='root',password='090416')
db=db1.cursor()
db.execute("SET NAMES 'utf8'")
db.execute('select * from movie_api')
movies=db.fetchall()
count=0
for movie in movies:
    get_poster(movie[0], movie[5])
    count+=1
    print(count,movie[1])
    time.sleep(2)

db.close()
db1.close()

