#打出实心菱形
'''
n=input()
n=int(n)
n1=int(n/2)
j1=0
for i in range (0,n1+1):
    j1=j1+1
    print(" "*(n1-i)+'*'*(2*j1-1))
for i in range (n1+1,n):
    j1=j1-1
    print(" "*(i-n1)+'*'*(2*j1-1))
 '''
# 打出空心菱形
n=input()
n=int(n)
n1=int(n/2)
j1=0
for i in range (0,n1+1):
    j1=j1+1
    if i==0:
        print(" "*(n1-i)+'*'*(2*j1-1))
    else:
        print(" "*(n1-i)+'*'+" "*(2*j1-3)+"*")
for i in range (n1+1,n):
    j1=j1-1
    if i==n-1:
        print(" "*(i-n1)+'*'*(2*j1-1))
    else:
        print(" "*(i-n1)+'*'+' '*(2*j1-3)+'*')
    

