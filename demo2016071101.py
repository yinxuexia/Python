# 学习函数的参数传递
'''
def printAll(**kargs):
    for k in kargs:
        print(k,':',kargs[k])

printAll(a=1,b=2,c=3)
printAll(x=3,y=5)
'''
'''
#学习lambda
sum=lambda a,b:a+b
print(sum(1,5))
'''

'''
#学习map
def double_func(x):
    return x*2
l_1=[1,2,3]
l_2=map(double_func,l_1)
print(list(l_2))
'''

#学习reduce
from functools import reduce

lst=range(1,101)
def add(x,y):
    return x+y
print(reduce(add,lst))
