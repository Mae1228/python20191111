import random
import copy

a = [[random.randint(0, 1) for j in range(1, 9)] for i in range(1, 9)]
a1 = copy.deepcopy(a)

def y():
    size = int(input('请输入进程的内存大小：'))
    s = size // 1024
    if size % 1024 == 0:
        s += 0
    else:
        s += 1
    sun = []
    for i in range(len(a)):
        for j in range(len(a)):
            if a[i][j] == 0:
                if s != 0:
                    s -= 1
                    a[i][j] = 1
                    sun1 = i * 8 + j
                    sun.append(sun1)
    print('页表：', sun)
    print('位示图：', a)
    s = size // 1024
    if size % 1024 == 0:
        print('内存块数：', s)
    else:
        s += 1
        print('内存块数：', s)
    var = input("请输入十六进制的逻辑地址：")
    b = oct(int(var, 16))
    w = int(b[2:])
    if w <= size:
        print('十进制的逻辑地址：', w)
        w0 = w // 1024
        print('页号：', w0)
        w1 = w % 1024
        print('页内偏移地址：', w1)
        w2 = sun[w0]
        print('物理块号：', w2)
        w3 = w2 * 1024 + w1
        print('物理地址：', w3)
    else:
        print('输入错误')
    print()
    main()

def n():
    for i in range(len(a)):
        for j in range(len(a)):
            if a[i][j] != a1[i][j]:
                a[i][j] = a1[i][j]
    print('位示图反向回填“0”：',a)
    print()
    main()

def main():
    running = int(input('是否要运行进程：\n1：运行\n2：不运行\n0：退出'))
    if running == 1:
        y()
    elif running == 2:
        n()
    elif running == 0:
        exit()
main()
'''
var=input("请输入十六进制的逻辑地址：")
b=bin(int(var,16))
print('二进制的逻辑地址：',b[2:])
w = b[2:s]
print('二进制的页号：',w)
w0 = b[s:18]
print('二进制的页内地址：',w0)
b1 = oct(int(w,2))
w1 = int(b1[2:])
print('页号化为十进制：',w1)
w2 = sun[w1]
print('页号化为十进制时，其对应的物理块号：',w2)
b2 = bin(int(w2))
w3 = b2[2:]
print('物理块号转换为二进制：',w3)
w4 = w3+w0
print('二进制的物理地址：',w4)
b4 = hex(int(w4,2))
print('十六进制的物理地址：',b4[2:])
'''