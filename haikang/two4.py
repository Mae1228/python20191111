#字典：元素由键值对组成
dd={'name':'张三','age':18,'iswork':False}
print(dd,type(dd))
#获取张三
print(dd['name'])
#获取所有键
for i in dd:
    print(i)
#获取值
for i in dd:
    print(dd[i])
#获取键和值
print(dd.items())
for i,j in dd.items():
    print(i,j)
for i in dd:
    print(i,dd[i])

#练习：输入10个学生信息（姓名，学号，成绩）
# 输入打印时输出所有学生信息
#输入查询时，提示请输入学生学号，查询成绩（xx的成绩是--，学号不正确）

# dict=[]
# for i in range(10):
#     name=input('请输入学生姓名')
#     number=int(input('请输入学生学号'))
#     sorce=int(input('请输入学生成绩'))
#     i={'name':name,'number':number,'sorce':sorce}
#     dict.append(i)
#
#
# while 1:
#     b = input('------打印 or 查询 or 退出------')
#     if b == 'dayin':
#         for i in dict:
#             for j, k in i.items():
#                 print(j, k)
#             print('--------------')
#     if b=='chaxun':
#         a=int(input('请输入查询的学号'))
#         ss=None
#         for i in dict:
#             if a==i['number']:
#                 ss=i['sorce']
#         if ss:
#             print('学号为'+str(a)+'的学生的成绩是：'+str(ss))
#         else:
#             print('该学号不存在')
#     if b=='tuichu':
#         print('退出程序')
#         break
students=[]
for i in range(3):
    print('请输入第'+str(i+1)+'学生信息')
    stu={}
    stu['name']=input('姓名：')
    stu['id']=int(input('学号：'))
    stu['score']=float(input('成绩：'))
    students.append(stu)

while 1:
    op=input('请输入你的操作')
    if op=='打印':
        for stu in  students:
            for i,j in stu.items():
                print(i,' : ',j,end='\t')
            print()
    if op=='查询':
        num=int(input('请输入学号'))
        # for stu in students:
        #     if stu['id']==num:
        #         print(stu['name']+'的成绩是'+str(stu['score']))
        #         f=True
        #         break
        # if f==False:
        #     print('学号不存在')
        for stu in students:
            if stu['id']==num:
                print(stu['name']+'的成绩是'+str(stu['score']))
                break
        else:
            print('学号不存在')
    if op=='退出':
        print('退出程序')
        break
#练习：人机对战做一个猜拳游戏：石头，剪刀，布
# 第i轮 游戏开始：开始猜拳
# 机器随机
# 比较
# 谁胜
# 玩三轮，两局到两局胜，最终显示胜利结果，显示双方成绩（**得分，**胜）
# 不服再战？
# 服了，结束
# 不服，继续，又来三轮
import random

while 1:
    fu = int(input('1：游戏开始 or 不服再战？2：不服；3：服了'))
    if fu==1 or fu==2:
        i = 0
        flagjq = 0
        flagr = 0
        while i < 3:
            you = int(input('请输入你的决定   3=石头，2=剪刀，1=布'))
            ran = random.randint(1, 3)  # 3=石头，2=剪刀，1=布
            print(ran)
            if ran - you == 2:
                print('机器胜利')
                flagjq += 1
                flagr += 0
            elif ran - you == -2:
                print('人胜利')
                flagjq += 0
                flagr += 1
            else:
                if ran == you:
                    print('平局')
                    flagjq += 0
                    flagr += 0
                if ran > you:
                    print('机器胜利')
                    flagjq += 1
                    flagr += 0
                if ran < you:
                    print('人胜利')
                    flagjq += 0
                    flagr += 1
            i+=1
        if flagjq >= 2:
            print('比赛结束，机器人胜利')
        elif flagr >= 2:
            print('比赛结束，人胜利')
        elif flagr == flagjq:
            print('比赛结束，平局')
    elif fu == 3:
        print('总比赛结束')
        break
    else:
        print('输入错误')




