# 练习：人机对战做一个猜拳游戏：石头，剪刀，布
# 第i轮 游戏开始：开始猜拳
# 机器随机
# 比较
# 谁胜
# 玩三轮，两局到两局胜，最终显示胜利结果，显示双方成绩（**得分，**胜）
# 不服再战？
# 服了，结束
# 不服，继续，又来三轮

import random
jiqi=('石头','剪刀','布')
flag=True
while flag==True:
    n=1
    w=0
    l=0
    while n<=3 and w<2 and l<2:
        i=input('第'+str(n)+'轮')
        j=random.randint(0,2)
        print(jiqi[j])
        if i==jiqi[j]:
            print('平局')
            n-=1
        elif i=='石头' and jiqi[j]=='剪刀' or i=='剪刀' and jiqi[j]=='布' or i=='布' and jiqi[j]=='石头':
            print('win')
            w+=1
        else:
            l+=1
            print('fail')
        n+=1
    f=input('继续挑战？ Y/N')
    if f=='N':
        flag=False