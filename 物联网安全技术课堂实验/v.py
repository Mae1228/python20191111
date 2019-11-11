#coding=gbk
import string
def main():
    p0 = input("请输入明文p：")  # datasecurity
    k0 = input("请输入密钥k：")  # best
    p = p0.lower()
    k = k0.lower()
    m = []
    for i in string.ascii_lowercase:
        m.append(i)
    print(m)
    p1 = []
    for i in p:
        p1.append(i)
    print(p1)
    k1 = []
    i = 0
    while i < len(p) + len(k):
        j = 0
        for j in k:
            k1.append(j)
        i += len(k)
    print(k1)
    p2=xiabiao(p1,m)
    k2=xiabiao(k1,m)
    s=jiami(p2,k2)
    e=shangbiao(s,m)
    e1=xiabiao(e,m)
    s1=jiemi(p2,k2,e1)
    p3=shangbiao(s1,m)
    yanzheng(p3,p1)

def xiabiao(p1,m):
    j = 0
    p2 = []
    while j < len(p1):
        i = 0
        while i < len(m):
            if m[i] == p1[j]:
                p2.append(i)
                break
            i = i + 1
        j = j + 1
    print('明文在原始字母表的下表p2：', p2)
    return p2

def shangbiao(s,m):
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
    print('密文e：', e)
    return e


def jiami(p2,k2):
    i = 0
    j = 0
    s = []
    while i < len(p2):
        while j < len(k2):
            if i == j:
                sum = 0
                sum = p2[i] + k2[j]
                if sum > 25:
                    sum = sum - 26
                    s.append(sum)
                    break
                else:
                    s.append(sum)
                    break
            j += 1
        i += 1
    print('明文加上密钥在原始字母表的下表s：', s)
    return s

def jiemi(p2,k2,e1):
    i = 0
    j = 0
    s1 = []
    while i < len(p2):
        while j < len(e1):
            if i == j:
                sum = 0
                sum = e1[j] - k2[i]
                if sum < 0:
                    sum = sum + 26
                    s1.append(sum)
                    break
                else:
                    s1.append(sum)
                    break
            j += 1
        i += 1
    print('明文在原始字母表的下标s1：', s1)
    return s1

def yanzheng(p3,p1):
    if p3 == p1:
        print('转换密文正确')
    else:
        print('转换密文错误')
main()