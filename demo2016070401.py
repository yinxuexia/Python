#学习正则表达式
'''
import re
text="Hi,I am Shirley Hilton.I am his wife."
m=re.findall(r'\b[Ii].*?e\b',text)#i开头 e结尾的
if m:
    print(m)
else:
    print('not match')

print('\bhi')
print(r'\bhi')
'''

#学习列表综合
import random
list1=[1,2,3,5,8,13,22]
list2=[i for i in list1 if i%2==0]
print(list2)


print(';'.join([str(i) for i in range(1,101) if i%2==0 and i%3==0 and i%5==0]))
