# 输出菲波纳契数列,1 1 2 3 5 8 13 21 34....
a1=1
b1=1
c=input()
c=int(c)
print(a1)
print(b1)
for i in range(0,c):
    a2=a1+b1
    print(a2)
    b1=a1
    a1=a2
    
    
    
    
