import web
import mysql.connector

urls=('/','index','/movie/(\d+)','movie')
render=web.template.render('templates/')


class index:
    def GET(self):
        db1=mysql.connector.connect(host='localhost',port ='3306',db='MovieSite', user='root',password='090416')
        db=db1.cursor()
        db.execute("SET NAMES 'utf8'")
        db.execute('select * from movie_api')
        movies=db.fetchall()
        db.close()
        db1.close()
        return render.index2016080201(movies)

    def POST(self): #对index文件中的post请求做相应的处理
        data=web.input() #取键入的表单的值
        condition=r'title like "%'+data.title+r'%"' #r'是为了防止python默认对字符串中%的转移
        db1=mysql.connector.connect(host='localhost',port ='3306',db='MovieSite', user='root',password='090416')
        db=db1.cursor()
        db.execute('select * from movie_api where '+condition)
        movies=db.fetchall()
        db.close()
        db1.close()
        return render.index2016080201(movies)

class movie:
    def GET(self,movie_id0):
        movie_id=str(movie_id0)
        db1=mysql.connector.connect(host='localhost',port ='3306',db='MovieSite', user='root',password='090416')
        db=db1.cursor()
        db.execute("SET NAMES 'utf8'")
        db.execute('select * from movie_api where id='+movie_id)
        movie1=db.fetchall()
        db.close()
        db1.close()
        return render.movie_api2016080202(movie1)


if __name__=="__main__":
    app=web.application(urls,globals())
    app.run()
