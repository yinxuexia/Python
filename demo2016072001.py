# 开始使用web.py
'''
import web
urls=('/','index') #指定网站url的匹配规则，左边是正则表达式，右边是对应处理函数的名称

movies=[{'title':'Forrest gump','year':'1994'},{'title':'Love','year':'1997'}]

class index:
    def GET(self):
        page=''
        for m in movies:
            page+='%s(%s)\n'%(m['title'],m['year'])
        return(page)

if __name__=="__main__":
    app=web.application(urls,globals())
    app.run()
'''
import web

urls=('/','index')

render=web.template.render('templates/')
movies=[{'title':'Forrest gump','year':'1994'},{'title':'Love','year':'1997'}]
class index:
    def GET(self):
        return render.index(movies)

if __name__=="__main__":
    app=web.application(urls,globals())
    app.run()









    
