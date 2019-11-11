#coding=gbk,,
import random
def main():
    ip = [58, 50, 42, 34, 26, 18, 10, 2,
          60, 52, 44, 36, 28, 20, 12, 4,
          62, 54, 46, 38, 30, 22, 14, 6,
          64, 56, 48, 40, 32, 24, 16, 8,
          57, 49, 41, 33, 25, 17, 9, 1,
          59, 51, 43, 35, 27, 19, 11, 3,
          61, 53, 45, 37, 29, 21, 13, 5,
          63, 55, 47, 39, 31, 23, 15, 7]
    e = [32, 1, 2, 3, 4, 5,
         4, 5, 6, 7, 8, 9,
         8, 9, 10, 11, 12, 13,
         12, 13, 14, 15, 16, 17,
         16, 17, 18, 19, 20, 21,
         20, 21, 22, 23, 24, 25,
         24, 25, 26, 27, 28, 29,
         28, 29, 30, 31, 32, 1]
    m = [random.randint(0, 1) for j in range(1, 65)]
    cd = [57, 49, 41, 33, 25, 17, 9,
          1, 58, 50, 42, 34, 26, 18,
          10, 2, 59, 51, 43, 35, 27,
          19, 11, 3, 60, 52, 44, 36,
          63, 55, 47, 39, 31, 33, 15,
          7, 62, 54, 46, 38, 30, 22,
          14, 6, 61, 53, 45, 37, 29,
          21, 13, 5, 28, 20, 12, 4]
    count = [1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1]
    z2 = [14, 17, 11, 24, 1, 5,
          3, 28, 15, 6, 21, 10,
          23, 19, 12, 4, 26, 8,
          16, 7, 27, 20, 13, 2,
          41, 52, 31, 37, 47, 55,
          30, 40, 51, 45, 33, 48,
          44, 49, 39, 56, 34, 53,
          46, 42, 50, 36, 29, 32]
    k = [random.randint(0, 1) for j in range(1, 65)]
    s = [14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7,
         0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8,
         4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0,
         15, 12, 8, 2, 4, 9, 1, 17, 5, 11, 3, 14, 10, 0, 6, 13]
    zhi2 = [16, 7, 20, 21,
            29, 12, 28, 17,
            1, 15, 23, 26,
            5, 18, 31, 10,
            2, 8, 24, 14,
            32, 27, 3, 9,
            19, 13, 30, 6,
            22, 11, 4, 25]
    ip1 = [40, 8, 48, 16, 56, 24, 64, 32,
           39, 7, 47, 15, 55, 23, 63, 31,
           38, 6, 46, 14, 54, 22, 62, 30,
           37, 5, 45, 13, 53, 21, 61, 29,
           36, 4, 44, 12, 52, 20, 60, 28,
           35, 3, 43, 11, 51, 19, 59, 27,
           34, 2, 42, 10, 50, 18, 58, 26,
           33, 1, 41, 9, 49, 17, 57, 25]
    ipl=fenzhuleft(ip)
    ipr=fenzhuright(ip)
    l0 = fenzhuleft(m)
    r0 = fenzhuright(m)
    l1 = huoqu(ipl, m)
    c=fenzhuleft(cd)
    d=fenzhuright(cd)
    n=0
    while n<len(count):

        print('次数',n+1)
        r = huoqu(e, r0)
        kl=f_sl(c)
        kr=f_sl(d)
        c1=yiwei_l(kl,count[n])
        d1=yiwei_l(kr,count[n])
        hb=l_r_hebing(c1,d1)
        f_hb=s_y(hb)
        x=huoqu(z2,f_hb)
        x1=huoqu(x,k)
        y=yihuo(r,x1)
        m2=six_eight(y,6)
        s1=six_eight(s,16)
        tl=xiabiao_l(m2)
        tr=xiabiao_r(m2)
        print(list(zip(tr, tl)))
        t=xiabaio_value(s1,tl,tr)
        t2=value_se(t)
        b=huoqu(zhi2,t2)
        v=yihuo(b,l0)
        n+=1
    r1 = huoqu(ipr,m)
    value=l_r_hebing(r1,v)
    huoqu(ip1,value)

    '''
         c=fenzhuleft(cd)
    d=fenzhuright(cd)
    kl=f_sl(c)
    kr=f_sr(d)
    k0=[]
    n=0
    while n<len(count):
        for i in count:
            wl=yiwei_l(kl,i)
            wr=yiwei_r(kr,i)
            w = wl + wr
            k0.append(w)
        n+=1
    print(k0)
        '''



def fenzhuleft(ip):
    i = 0
    l = []
    while i < len(ip):
        if i < len(ip) // 2:
            l.append(ip[i])
        i+=1
    print('左部分明文l：', l)
    return l

def fenzhuright(ip):
    i = 0
    r = []
    while i < len(ip):
        if i >= len(ip) // 2:
            r.append(ip[i])
        i += 1
    print('右部分明文r：', r)
    return r

def huoqu(e,m):#获取01值
    i = 0
    m1 = []
    while i < len(e):
        s = m[e[i] - 1]
        m1.append(s)
        i += 1
    print('m1', m1)
    return m1

def f_sl(c):#分成二维数组
    kl = []
    for i in range(0, len(c), 7):
        kl.append(c[i:i + 7])
    print(kl)
    return kl
'''
def f_sr(d):#
    kr = []
    for i in range(0, len(d), 7):
        kr.append(d[i:i + 7])
    print(kr)
    return kr
'''
def yiwei_l(kl,k):#左移
    wl = []
    for i in kl:
        ss = i[k:] + i[:k]
        wl.append(ss)
    print('wl', wl)
    return wl
'''
def yiwei_r(kr,k):
    wr = []
    for i in kr:
        ss = i[k:] + i[:k]
        wr.append(ss)
    print('wr', wr)
    return wr
'''
def s_y(w):
    from tkinter import _flatten
    ww = list(_flatten(w))
    print(ww)
    return ww

def l_r_hebing(wl,wr):
    w = wl + wr
    print(w)
    print(len(w))
    return w

def yihuo(m1,x1):
    i = 0
    y = []
    while i < len(m1):
        j = 0
        while j < len(x1):
            if i == j:
                s = m1[i] ^ x1[j]
                y.append(s)
            j += 1
        i += 1
    # (m1 and (not x1) ) or ( (not m1) and x1)
    print('y', y)
    print(len(y))
    return y

def six_eight(y,j):
    m2 = []
    for i in range(0, len(y), j):
        m2.append(y[i:i + j])
    print('m2', m2)
    print(len(m2))
    return m2

def xiabiao_l(m2):
    i = 0
    tl = []
    while i < 8:
        l = m2[i][1] * 8 + m2[i][2] * 4 + m2[i][3] * 2 + m2[i][4] * 1
        tl.append(l)
        i += 1
    print(tl)
    return tl

def xiabiao_r(m2):
    i = 0
    tr = []
    while i < 8:
        r = m2[i][0] * 2 + m2[i][5] * 1
        tr.append(r)
        i += 1
    print(tr)
    return tr

def xiabaio_value(s1,tl,tr):
    t = []
    i = 0
    while i < len(tr):
        j = 0
        while j < len(tl):
            if i == j:
                tt = s1[tr[i]][tl[j]]
                t.append(tt)
                break
            j += 1
        i += 1
    print(t)
    return t

def value_se(t):
    t1 = []
    for i in t:
        s = bin(i)
        s1 = s[2:]
        if len(s1) == 4:
            t1.append(s1)
        else:
            while 1:
                s1 = '0' + s1
                if len(s1) == 4:
                    t1.append(s1)
                    break

    print(t1)
    t2 = []
    for i in t1:
        for j in i:
            t2.append(int(j))
    print('t2', t2)
    print(len(t2))
    return t2

main()