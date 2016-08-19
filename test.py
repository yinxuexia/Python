#往数据库中插入多条数据

import mysql.connector

db1=mysql.connector.connect(host='localhost',port ='3306',db='moviesite', user='root',password='090416')
db=db1.cursor()
temp=[]
for i in range(1,5):
    years=1994+i
    temp.append(years)

print(temp)
sql='insert into movie(years) VALUES(%d)'
db.executemany(sql,temp)

db1.commit()
db.close()
db1.close()

