#coding=gbk
import string
def main():
    k0=input('��������Կk��')#spectacular
    s0=input('����������s��')#china
    k=k0.lower()
    s=s0.lower()
    #m=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    m = []
    for i in string.ascii_lowercase:
        m.append(i)
    print(m)
    s1=[]
    for i in s:
        s1.append(i)
    print('����s1��',s1)
    c=[]
    for i in k:
        c.append(i)
    for i in m:
        c.append(i)
    c1=[]
    for i in c:
        if i not in c1:
            c1.append(i)
    print('ԭʼ��ĸ��m��',m)
    print('������ĸ��c1��',c1)
    ms=xiabiao(s1,m)
    e=shangbaio(ms,c1)
    ms1=xiabiao(e,c1)
    e1=shangbaio(ms1,m)
    yanzheng(e1,s1)

def xiabiao(s1,m):
    j=0
    ms = []
    while j < len(s1):
        i = 0
        while i < len(m):
            if m[i] == s1[j]:
                ms.append(i)
                break
            i = i + 1
        j = j + 1
    print('������ԭʼ��ĸ����±�ms��', ms)
    return ms

def shangbaio(ms,c1):
    x = 0
    e = []
    while x < len(ms):
        y = 0
        while y < len(c1):
            if ms[x] == y:
                e.append(c1[y])
                break
            y = y + 1
        x = x + 1
    print('����e��', e)
    return e

def yanzheng(e1,s1):
    if e1 == s1:
        print('ת��������ȷ')
    else:
        print('ת�����Ĵ���')

main()