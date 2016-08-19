#猜数字游戏
'''
from random import randint
num=randint(1,100)
bingo=False
print('Guess what i think')

while bingo==False:
    answer=input("请输入")
    answer=int(answer)
    if answer<num:
        print("too small!")
    if answer>num:
        print('too big')
    if answer==num:
        print('BINGO!')
        bingo=True
'''

#统计总游戏次数、最快猜出的轮数和猜过的总轮数
from random import randint

#开始玩之前，先输入名字
name=input('请输入用户名：')

f=open('game-demo1.txt')
lines=f.readlines()
f.close()

scores={}
for line in lines:
    s=line.split()
    scores[s[0]]=s[1:]#将每一行的第一个作为键，其余作为值
score=scores.get(name)
print(score)
if score is None:#没有找到该用户分记录
    score=[0,0,0]#初始化一个
    
game_times=int(score[0])
min_times=int(score[1])
total_times=int(score[2])
times=0

#计算游戏的平均轮数
if game_times==0:
    avg_times=0
elif game_times==1:
    avg_times=total_times 
else:
    avg_times=float(total_times)/game_times
#玩之前输出其之前的记录
print('%s,你已经玩了%d次，最少%d轮猜到答案，平均%.2f轮猜到答案'%(name,
    game_times,min_times,avg_times))   


num=randint(1,100)
bingo=False
print('Guess what i think')
while bingo==False:
    times+=1
    answer=input("请输入\n")
    answer=int(answer)
    if answer<num:
        print("too small!")
    if answer>num:
        print('too big')
    if answer==num:
        print('BINGO!')
        bingo=True

if game_times==0 or min_times>times:
    min_times=times                 
total_times+=times
game_times+=1

#把成绩更新到对应玩家的数据中
scores[name]=[str(game_times) ,str(min_times) ,str(total_times)]
result=''
for n in scores:#将n作为键name来处理
    l=n+' '+' '.join(scores[n])+'\n'
    result+=l
      
f=open('game-demo1.txt','w')
f.write(result)
f.close()
