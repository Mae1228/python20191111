#coding=gbk
import string
p0=input("����������p��")#datasecurity
k0=input("��������Կk��")#best
p=p0.lower()
k=k0.lower()

#m=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
m=[]
for i in string.ascii_lowercase:
    m.append(i)
print('ԭʼ��ĸ��m��',m)
p1=[]
for i in p:
    p1.append(i)
print('����p1��',p1)
k1=[]
i=0
while i<len(p)+len(k):
    j=0
    for j in k:
        k1.append(j)
    i+=len(k)
print('��Կk1��',k1)

j=0
p2=[]
while j<len(p1):
    i = 0
    while i<len(m):
        if m[i]==p1[j]:
            p2.append(i)
            break
        i=i+1
    j=j+1
print('������ԭʼ��ĸ����±�p2��',p2)
j=0
k2=[]
while j<len(k1):
    i = 0
    while i<len(m):
        if m[i]==k1[j]:
            k2.append(i)
            break
        i=i+1
    j=j+1
print('��Կ��ԭʼ��ĸ����±�k2��',k2)

i=0
j=0
s=[]
while i <len(p2):
    while j <len(k2):
        if i==j:
            sum=0
            sum=p2[i]+k2[j]
            if sum>25:
                sum=sum-26
                s.append(sum)
                break
            else:
                s.append(sum)
                break
        j+=1
    i+=1
print('���ļ�����Կ��ԭʼ��ĸ����±�s��',s)

x = 0
e = []
while x < len(s):
    y = 0
    while y < len(m):
        if s[x] == y:
            e.append(m[y])
            break
        y = y + 1
    x = x + 1
print('����e��', e)

j=0
e1=[]
while j<len(e):
    i = 0
    while i<len(m):
        if m[i]==e[j]:
            e1.append(i)
            break
        i=i+1
    j=j+1
print('������ԭʼ��ĸ����±�e1��',e1)

i=0
j=0
s1=[]
while i <len(p2):
    while j <len(e1):
        if i==j:
            sum=0
            sum=e1[j]-k2[i]
            if sum<0:
                sum=sum+26
                s1.append(sum)
                break
            else:
                s1.append(sum)
                break
        j+=1
    i+=1
print('������ԭʼ��ĸ����±�s1��',s1)

x = 0
p3 = []
while x < len(s1):
    y = 0
    while y < len(m):
        if s1[x] == y:
            p3.append(m[y])
            break
        y = y + 1
    x = x + 1
print('����p3��', p3)
if p3==p1:
    print('ת��������ȷ')
else:
    print('ת�����Ĵ���')
