#开始使用数据库


import web
import mysql.connector

urls=('/','index')

render=web.template.render('templates/')
class index:
    def GET(self):
        db1=mysql.connector.connect(host='localhost',port ='3306',db='MovieSite', user='root',password='090416')
        db=db1.cursor()
        db.execute("SET NAMES 'utf8'")
        db.execute('select title,years,country,abstract from movie')
        movies=db.fetchall()
        db.close
        db1.close
        return render.index2016072101(movies)

if __name__=="__main__":
    app=web.application(urls,globals())
    app.run()
