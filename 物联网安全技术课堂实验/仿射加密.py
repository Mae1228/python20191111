#coding=gbk
import string
k=input('请输入密钥：')#7,3
s0=input('请输入明文：')#china
s=s0.lower()
f=26
k1=int(k[0])
k2=int(k[2])
#m=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
m=[]
for i in string.ascii_lowercase:
    m.append(i)
print('原始字母表m：',m)
s1=[]
for i in s:
    s1.append(i)
print('明文s1：', s1)

j=0
ms=[]
while j<len(s1):
    i = 0
    while i<len(m):
        if m[i]==s1[j]:
            ii=k1*i+k2
            ms.append(ii)
            break
        i=i+1
    j=j+1
print('明文在原始字母表的下表ms：',ms)#17, 52, 59, 94, 3

ms1=[]
for i in ms:
    i1=i%f
    ms1.append(i1)
print('密文在原始字母表的下表ms1',ms1)#17, 0, 7, 16, 3

x=0
e=[]
while x<len(ms1):
    y=0
    while y<len(m):
        if ms1[x]==y:
            e.append(m[y])
            break
        y=y+1
    x=x+1
print('密文e：',e)#rahqd

q=[]
c=[]
c.append(f)
c.append(k1)
while 1:
    q3=c[-2]//c[-1]
    c3=c[-2]%c[-1]
    q.append(q3)
    c.append(c3)
    if c3==1:
        break
print('q：',q)
print('加上f和a的c：',c)

b=[0,1]
i=0
while i<len(q):
    b2=(-1)*b[i+1]*q[i]+b[i]
    b.append(b2)
    i+=1
print('加上b-1和b0的b：',b)#0, 1, -3, 4, -11

if (k1*b[-1])%f==1:
    print('a的逆正确：',b[-1])
else:
    print('a的逆错误')

i=1
print(b[-1])
while i<=abs(b[-1]):
    if b[-1]<0:
        c=i*f+b[-1]
        if c>0:
            mod=c
            #print(c)
            break
    else:
        mod=f%b[-1]
    i=i+1
print('k2的逆对f求mod：',mod)

jm=[]
for i in ms1:
    ij=(mod*(i-k2))%f
    if ij<0:
        #ij1=f%(-ij)
        i = 1
        while i <= abs(b[-1]):
            c = i * f + b[-1]
            if c > 0:
                ij1 = c
                break
            i = i + 1
        jm.append(ij1)
    else:
        jm.append(ij)
print('解密：明文在原始字母表的下表jm：',jm)#2, 7, 8, 13, 0

x=0
ms2=[]
while x<len(jm):
    y=0
    while y<len(m):
        if jm[x]==y:
            ms2.append(m[y])
            break
        y+=1
    x+=1
print('解密：明文ms2：',ms2)#china
if ms2==s1:
    print('转换密文正确')
else:
    print('转换密文错误')