

import web
import mysql.connector

urls=('/','index','/movie/(\d+)','movie')
render=web.template.render('templates/')

db1=mysql.connector.connect(host='localhost',port ='3306',db='MovieSite', user='root',password='090416')
db=db1.cursor()

class index:
    def GET(self):
        db1=mysql.connector.connect(host='localhost',port ='3306',db='MovieSite', user='root',password='090416')
        db=db1.cursor()
        db.execute("SET NAMES 'utf8'")
        db.execute('select * from movie')
        movies=db.fetchall()
        db.close()
        db1.close()
        return render.index2016072601(movies)

class movie:
    def GET(self,movie_id0):
        movie_id=str(movie_id0)
        db1=mysql.connector.connect(host='localhost',port ='3306',db='MovieSite', user='root',password='090416')
        db=db1.cursor()
        db.execute("SET NAMES 'utf8'")
        db.execute('select * from movie where id='+movie_id)
        movie1=db.fetchall()
        db.close()
        db1.close()
        return render.index2016072602(movie1)


if __name__=="__main__":
    app=web.application(urls,globals())
    app.run()
