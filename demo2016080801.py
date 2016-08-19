#展示影片信息界面
import web
import mysql.connector

urls=(
    '/','index',
    '/movie/(.*)','movie',
    '/cast/(.*)','cast',)

render=web.template.render('templates/')

def py_mysql(sql):
    db1=mysql.connector.connect(host='localhost',port ='3306',db='MovieSite', user='root',password='090416',charset='utf8')
    db=db1.cursor()
    db.execute("SET NAMES 'utf8'")
    db.execute(sql)
    movies=db.fetchall()
    db.close()
    db1.close()
    return movies
    

class index:
    def GET(self):
        sql='select * from movie_api'
        movies=py_mysql(sql)
        return render.index2016080201(movies)

    def POST(self): #对index文件中的post请求做相应的处理
        data=web.input() #取键入的表单的值
        condition=r'title like "%'+data.title+r'%"' #r'是为了防止python默认对字符串中%的转移
        sql='select * from movie_api where '+condition
        movies=py_mysql(sql)
        return render.index2016080201(movies)

#根据取到的Id查看电影详情
class movie:
    def GET(self,movie_id0):
        movie_id=str(movie_id0)
        sql='select * from movie_api where id='+movie_id
        movie1=py_mysql(sql)
        return render.movie_api2016080801(movie1)

#通过主演名查询电影展示其演过的电影
class cast:
    def GET(self,cast_name):
        cast_name=cast_name.encode('utf8')
        cast_name=str(cast_name)
        print(cast_name)
        condition=r'casts like "%'+cast_name+r'%"'
        sql='select * from movie_api where '+condition
        print(sql)
        movies=py_mysql(sql)
        return render.index2016080201(movies)

if __name__=="__main__":
    app=web.application(urls,globals())
    app.run()
