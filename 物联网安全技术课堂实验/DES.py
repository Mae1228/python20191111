#coding=gbk
s0=input('������64λ�����ģ�')
s=s0.split(' ')
s1=[]
l=[]
r=[]
for i in s:
    s1.append(i)
i=0
while i<len(s):
    if i<len(s)//2:
        l.append(s[i])
    else:
        r.append(s[i])
    i+=1
print('����s1��',s1)
print('�󲿷�����l��',l)
print('�Ҳ�������r��',r)

M = []
for i in range(0, len(r),4):
    M.append(r[i:i+4])
print(M)

n=int(input('n'))#lie
m=int(input('m'))#hang
a=[[0]*n]*m
for i in range(m):
    a[i]=input().split(' ')
    for j in range(n):
        a[i][j]=int(a[i][j])
print(a)
while 1:
    i=int(input('i'))
    j=int(input('j'))
    print(a[i][j])
