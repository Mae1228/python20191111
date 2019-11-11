#!/usr/bin/python
# -*- coding: UTF-8 -*-
#coding=gbk
import copy
import random

zhi = []
def panduan(n):
    if str(n).isdigit() and n>1:
        for i in range(2,n-1):
            if n%i==0:
                return False
        return zhi.append(n)
    else:
        print(n,'变量有误，请输入大于1的整数。')
k=int(input('请输入在k范围：'))
for i in range(k):
    panduan(i)
print('素数zhi：',zhi)
#在素数列表中随机生成一个数，例如:p和q
def zhishu():
    from random import choice
    p=choice(zhi)
    return p
while 1:
    p=zhishu()
    q=zhishu()
    if p==q:
        p=zhishu()
        q=zhishu()
    else:
        break
print('p和q：',p,q)
n = p * q
y_n = (p - 1) * (q - 1)
print('n：',n)
print('y_n：',y_n)
y=copy.deepcopy(y_n)
# print('y：',y)

z=[]
while y_n!=1:
    j=0
    while j<len(zhi):
        if y_n%zhi[j]==0:
            y_n=y_n//zhi[j]
            z.append(zhi[j])
            break
        j+=1
print('y_n由什么素数组成z：',z)
z1=[]
for i in z:
    if i not in z1:
        z1.append(i)
print('z去重后的z1：',z1)
azhi=[]
for i in zhi:
    if i not in z1:
        azhi.append(i)
print('在zhi中删除z1的素数azhi：',azhi)
from random import choice
e=choice(azhi)
print('公钥：',e)

qq=[]
c=[]
c.append(y)
c.append(e)
while 1:
    q3=c[-2]//c[-1]
    c3=c[-2]%c[-1]
    qq.append(q3)
    c.append(c3)
    if c3==1:
        break
print('q：',qq)
print('加上f和a的c：',c)

b=[0,1]
i=0
while i<len(qq):
    b2=(-1)*b[i+1]*qq[i]+b[i]
    b.append(b2)
    i+=1
print('加上b-1和b0的b：',b)#0, 1, -3, 4, -11

i=1
print('公钥的逆：',b[-1])
while i<=abs(b[-1]):
    if b[-1]<0:
        c=i*y+b[-1]
        if c>0:
            d=c
            #print(c)
            break
    else:
        d=y%b[-1]
    i=i+1
print('d：',d)
m=random.randint(1,50)
print('明文m：',m)

c=m**e%n
print('c：',c)
#解密
m2=c**d%n
# print('m2：',m2)
if m==m2:
    print('正确')
else:
    print('错误')