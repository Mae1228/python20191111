#coding=gbk,,
import random
ip=[58,50,42,34,26,18,10,2,
    60,52,44,36,28,20,12,4,
    62,54,46,38,30,22,14,6,
    64,56,48,40,32,24,16,8,
    57,49,41,33,25,17,9,1,
    59,51,43,35,27,19,11,3,
    61,53,45,37,29,21,13,5,
    63,55,47,39,31,23,15,7]
i=0
l=[]
r=[]
while i<len(ip):
    if i<len(ip)//2:
        l.append(ip[i])
    else:
        r.append(ip[i])
    i+=1
print('�󲿷�����l��',l)
print('�Ҳ�������r��',r)
#��64λ��01�ֳ�����������
m=[random.randint(0, 1) for j in range(1, 65)]
print(m)
print(len(m))
i=0
ml1=[]
mr1=[]
while i<len(m):
    if i<len(m)//2:
        ml1.append(m[i])
    else:
        mr1.append(m[i])
    i+=1
print('��ߵ�01ֵml1��',ml1)
print('�ұߵ�01ֵmr1��',mr1)
#�Ҳ��ֵĻ�ȡ48λ��01����E��չ
e=[32,1,2,3,4,5,
   4,5,6,7,8,9,
   8,9,10,11,12,13,
   12,13,14,15,16,17,
   16,17,18,19,20,21,
   20,21,22,23,24,25,
   24,25,26,27,28,29,
   28,29,30,31,32,1]
i=0
m1=[]
while i<len(e):
    s=ml1[e[i]-1]
    m1.append(s)
    i+=1
print('��ߵ���չ48λ01ֵm1',m1)
i=0
mr=[]
while i<len(e):
    s=mr1[e[i]-1]
    mr.append(s)
    i+=1
print('�ұߵ���չ48λ01ֵmr',mr)
#��Կ
cd=[57,49,41,33,25,17,9,
    1,58,50,42,34,26,18,
    10,2,59,51,43,35,27,
    19,11,3,60,52,44,36,
    63,55,47,39,31,33,15,
    7,62,54,46,38,30,22,
    14,6,61,53,45,37,29,
    21,13,5,28,20,12,4]
i=0
c=[]
d=[]
while i<len(cd):
    if i<len(cd)//2:
        c.append(cd[i])
    else:
        d.append(cd[i])
    i+=1
print('�󲿷���Կc��',c)
print('�Ҳ�����Կd��',d)
#��һά�б��ɶ�ά�б�
kl = []
for i in range(0, len(c),7):
    kl.append(c[i:i+7])
print('�󲿷���Կ��ɶ�άkl',kl)
kr = []
for i in range(0, len(d),7):
    kr.append(d[i:i+7])
print('�Ҳ�����Կ��ɶ�άkr',kr)
#ʹ�������ߵĶ�ά��Կѭ������
count=[1,1,2,2,2,2,2,2,1,2,2,2,2,2,2,1]
print(len(count))
wl=[]
for i in kl:
    ss = i[1:] + i[:1]
    wl.append(ss)
print('�󲿷���Կ����wl',wl)
wr=[]
for i in kr:
    ss = i[1:] + i[:1]
    wr.append(ss)
print('�Ҳ�����Կ����wr',wr)
w=wl+wr
print('���Ҷ�ά���ֺϲ�w',w)
#�Ѷ�ά�б���һά�б�
from tkinter import _flatten
ww=list(_flatten(w))
print('�Ѻϲ��Ķ�ά���һάww',ww)

z2=[14,17,11,24,1,5,
    3,28,15,6,21,10,
    23,19,12,4,26,8,
    16,7,27,20,13,2,
    41,52,31,37,47,55,
    30,40,51,45,33,48,
    44,49,39,56,34,53,
    46,42,50,36,29,32]
i=0
x=[]
while i<len(z2):
    s=ww[z2[i]-1]
    x.append(s)
    i+=1
print('���һά�ϲ�x',x)

k=[random.randint(0, 1) for j in range(1, 65)]
print('64λ��Կ01ֵk',k)
i=0
x1=[]
while i<len(x):
    s=k[x[i]-1]
    x1.append(s)
    i+=1
print('���48λ��01ֵ������Կx1',x1)
#���
i=0
y=[]
while i<len(m1):
    j = 0
    while j<len(x1):
        if i==j:
            s=m1[i]^x1[j]
            y.append(s)
        j+=1
    i+=1
#(m1 and (not x1) ) or ( (not m1) and x1)
print('��չE����Կ���y',y)
#��48λ��01���ֳ�8�飬ÿ��6λ01��
m2 = []
for i in range(0, len(y),6):
    m2.append(y[i:i+6])
print('���6*8�Ķ�ά����m2',m2)


#��S�зֳ�4�飬ÿ��16λ
s=[14,4,13,1,2,15,11,8,3,10,6,12,5,9,0,7,
   0,15,7,4,14,2,13,1,10,6,12,11,9,5,3,8,
   4,1,14,8,13,6,2,11,15,12,9,7,3,10,5,0,
   15,12,8,2,4,9,1,17,5,11,3,14,10,0,6,13]
s1 = []
for i in range(0, len(s),16):
    s1.append(s[i:i+16])
print('4*16��S�ж�άs1',s1)

i=0
tr=[]
tl=[]
while i<8:
    r=m2[i][0]*2+m2[i][5]*1
    l=m2[i][1]*8+m2[i][2]*4+m2[i][3]*2+m2[i][4]*1
    tr.append(r)
    tl.append(l)
    i+=1
print('��S�е���tr',tr)
print('��S�е���tl',tl)
print('8����S�е��±�',list(zip(tr,tl)))
#����������S�����ҳ�ֵ
t=[]
i=0
while i<len(tr):
    j=0
    while j<len(tl):
        if i==j:
            tt=s1[tr[i]][tl[j]]
            t.append(tt)
            break
        j+=1
    i+=1
print('�ҳ���S�е�ֵt',t)
#��S�����ҳ���ֵת��4λ�Ķ�����
t1=[]
for i in t:
    s=bin(i)
    s1=s[2:]
    if len(s1) == 4:
        t1.append(s1)
    else:
        while 1:
            s1='0'+s1
            if len(s1)==4:
                t1.append(s1)
                break
print(t1)
t2=[]
for i in t1:
    for j in i:
        t2.append(int(j))
print('���ɶ����ƣ�32λ01ֵt2',t2)

zhi2=[16,7,20,21,
   29,12,28,17,
   1,15,23,26,
   5,18,31,10,
   2,8,24,14,
   32,27,3,9,
   19,13,30,6,
   22,11,4,25]
i=0
b=[]
while i<len(zhi2):
    s=t2[zhi2[i]-1]
    b.append(s)
    i+=1
print('P�任���32λ01ֵb',b)

#ip-1
ip1=[40,8,48,16,56,24,64,32,
     39,7,47,15,55,23,63,31,
     38,6,46,14,54,22,62,30,
     37,5,45,13,53,21,61,29,
     36,4,44,12,52,20,60,28,
     35,3,43,11,51,19,59,27,
     34,2,42,10,50,18,58,26,
     33,1,41,9,49,17,57,25]





