def menu():
    print('*********************')
    print('1.FCFS先来先服务')
    print('2.SJF短作业区间')
    print('3.RR分时系统设计')
    print('*********************')

sum=int(input('请输入进程的数量'))
i=0
namelist=[]
sizelist=[]
while i<sum:
    name=input('请输入进程名字')
    size=int(input('请输入进程cpu区间时间'))
    namelist.append(name)
    sizelist.append(size)
    i=i+1
print('进程名：',namelist)
print('CPU区间时间：',sizelist)
sun=0
x=0
while x<sum-1:
    sun=sizelist[x]*(sum-1-x)+sun
    x=x+1
print('FCFS先来先服务周转时间总和',sun)
sun=sun/sum
print('FCFS先来先服务平均周转时间：',sun)

sizelist.sort()
print(sizelist)
sun1=0
x1=0
while x1<sum-1:
    sun1=sizelist[x1]*(sum-1-x1)+sun1
    x1=x1+1
print('SJF短作业区间周转时间总和',sun1)
sun1=sun1/sum
print('SJF短作业区间平均周转时间：',sun1)
'''
sun2=int(input('请输入时间片'))
x2=0
aftersizelist=[]
while x2<sum:
    if sun2<sizelist[x2]:
        namex2=namelist[x2]
        namelist.append(namex2)
        sizex2=sizelist[x2]-sun2
        sizelist.append(sizex2)
        aftersizelist.append(sun2)
        print(namelist)
        print(sizelist)
        print(aftersizelist)
    else:
        aftersizelist.append(sizelist[x2])
        print(aftersizelist)
        del namelist[x2]
        print(namelist)
        del sizelist[x2]
        print(sizelist)
    x2=x2+1
    
def main():
    menu()
    a = eval(input("请输入要执行的序号: "))
    if a == 1:
        FCFS()
    elif a == 2:
        SJF()
    elif a == 3:
        RR()
    else：
        exit()
'''