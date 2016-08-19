# 点球小游戏
'''
from random import choice
print('Choose one side to shoot:')
print('left,center,right')
you=input()
print('You kicked'+you)
direction=['left','center','right']
com=choice(direction)
print('Computer saved'+com)
if you!=com:
    print('Goal!')
else:
    print('Oops')
'''
from random import choice
score=[0,0]
direction=['left','center','right']

def kick():   #定义函数
    print('====You Kick!====')
    print('Choose one side to shoot:')
    print('left,center,right')
    you=input()
    print('You kicked'+you)#射门方向
    com=choice(direction)#电脑随机扑球方向
    print('Computer saved'+com)
    if you!=com:
        print('Goal!')
        score[0]+=1  #方向不同，你赢了，分数加1
        print('%d(you)-%d(com)\n'%(score[0],score[1]))
    else:
        print('Oops')

    print('====You Save!====')
    print('Choose one side to save')
    print('left,center,right')
    you=input()
    print('You saved'+you)#你扑球方向
    com=choice(direction)
    print('Computer kicked'+com)
    if you==com:
        print('Goal!')
    else:
        print('Oops')
        score[1]+=1
        print('%d(you)-%d(com)\n'%(score[0],score[1]))

#执行5局
for i in range(0,5):
    print('====Round %d===='%(i+1))
    kick()


#谁赢，平局再玩
while (score[0]==score[1]):
    i+=1
    print('====Round %d==='%(i+1))
    kick()

if score[0]>score[1]:
    print('You Win')
else:
    print('You Lose')
    

