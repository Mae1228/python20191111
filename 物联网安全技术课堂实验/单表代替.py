#coding=gbk
import string
def main():
    k0=input('请输入密钥k：')#spectacular
    s0=input('请输入明文s：')#china
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
    print('明文s1：',s1)
    c=[]
    for i in k:
        c.append(i)
    for i in m:
        c.append(i)
    c1=[]
    for i in c:
        if i not in c1:
            c1.append(i)
    print('原始字母表m：',m)
    print('代替字母表c1：',c1)
    jiami(s1,m,c1)


def jiami(s1,m,c1):
    j=0
    ms=[]
    while j<len(s1):
        i = 0
        while i<len(m):
            if m[i]==s1[j]:
                ms.append(i)
                break
            i=i+1
        j=j+1
    print('明文在原始字母表的下表ms：',ms)
    x=0
    e=[]
    while x<len(ms):
        y=0
        while y<len(c1):
            if ms[x]==y:
                e.append(c1[y])
                break
            y=y+1
        x=x+1
    print('密文e：',e)
    jiemi(e,m,c1,s1)

def jiemi(e,m,c1,s1):#验证
    j = 0
    ms1 = []
    while j < len(e):
        i = 0
        while i < len(c1):
            if c1[i] == e[j]:
                ms1.append(i)
                break
            i = i + 1
        j = j + 1
    print('密文在代替字母表的下表ms1：', ms1)
    x = 0
    e1 = []
    while x < len(ms1):
        y = 0
        while y < len(m):
            if ms1[x] == y:
                e1.append(m[y])
                break
            y = y + 1
        x = x + 1
    print('明文e1：', e1)
    if e1 == s1:
        print('转换密文正确')
    else:
        print('转换密文错误')
main()