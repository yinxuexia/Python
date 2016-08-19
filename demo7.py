#打开文件
'''
f=open('data.txt')
data=f.readline()
print(data)
f.close()
'''
#从data文件中读内容，写到data1中
'''
f=open("data.txt")
data=f.read()
data1=open('data1.txt','w')
data1.write(data)
f.close()
data1.close()
'''

#从控制台输入内容，存入文件中
'''
print('请输入内容')
a=input()
data=open('data1.txt','w')
data.write(a)
data.close()
'''

#统计学生的总分数（交一次作业得一次分，不交没有分数）

f=open('data2.txt')
lines=f.readlines()
f.close()
results=[]
for line in lines:
    data=line.split()
    sum=0
    score=0
    for score in data[1:]:
        sum+=int(score)
    result=str('%s\t:%d\n'%(data[0],sum))
    print(result)
    results.append(result)
output=open('data3.txt','w')
output.writelines(results)
output.close() #少写了（）,导致无报错，但写入文件为空，原因是数据还存在缓冲区内，若不关闭文件
 
    
