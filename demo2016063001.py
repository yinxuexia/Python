# 查看天气预报
import urllib
import json
web=urllib.urlopen('http://www.baidu.com')
content=web.read()
print(content)
