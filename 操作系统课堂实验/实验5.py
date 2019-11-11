sum=int(input('请输入进程的数量'))
zhoutime=[]
dzhoutime=[]
severt=[]
i=0
startlasttime=0
while i<sum:
    starttime = int(input('请输入进程的开始时间'))
    endtime = int(input('请输入进程的结束时间'))
    severttime=int(input('请输入进程的服务时间'))
    sun=endtime-starttime
    print('该进程的周转时间',sun)
    zhoutime.append(sun)
    dsun=sun/severttime
    print('该进程的带权周转时间',dsun)
    dzhoutime.append(dsun)
    if startlasttime<starttime:
        startlasttime = starttime
        i+=1
    else:
        print('该进程的开始时间不大于上一个进程的开始时间')
print(zhoutime)
print(dzhoutime)
zhousun=0
for x in zhoutime:
    zhousun=zhousun+x
print('FCFS先来先服务周转时间总和',zhousun)
zhousun1=zhousun/sum
print('FCFS先来先服务平均周转时间',zhousun1)
dzhousun=0
for dx in dzhoutime:
    dzhousun=dzhousun+dx
print('FCFS先来先服务带权周转总时间',dzhousun)
dzhousun1=dzhousun/sum
print('FCFS先来先服务平均带权周转时间',dzhousun1)
zhoutime.sort()
print(zhoutime)
#3 1 9 4 2 8 3 3 7 2
zhousun2=0
for x2 in zhoutime:
    zhousun2=zhousun2+x2
print('SJF短作业区间周转时间总和',zhousun2)
zhousun22=zhousun2/sum
print('SJF短作业区间平均周转时间',zhousun22)
dzhousun2=0
for dx2 in dzhoutime:
    dzhousun2=dzhousun2+dx2
print('SJF短作业区间带权周转时间总和',dzhousun)
dzhousun22=dzhousun2/sum
print('SJF短作业区间平均带权周转时间',dzhousun22)