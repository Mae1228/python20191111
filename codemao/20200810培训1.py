from removebg import RemoveBg
import os


# # 编写第一条代码
# print('hello world')
# message=input('输入城市：')
# print('我来自',message)

# print(13/5)
# print(13//5)#向下取整

# for i in range(5):
#     zhi=int(input('请输入质数：'))
#     for i in range(2,(zhi//2)+1):
#         if zhi % i==0:
#             print(zhi, '不是质数')
#             break
#     else:
#         print(zhi, '是质数')

# from removebg import RemoveBg
# mbg = RemoveBg('6mwM1SedKSghhLnvGDt32nLZ','error.log')
# mbg.remove_background_from_img_file('A:\AAA115图片\微信\微信图片_20200723102702.jpg')


# # ord() chr() 老版本unnichr()  Unicode万国码
# print(ord('张'))#字符转换成ASCII
# print(chr(24352))#ASCII转换成字符
# # 不能够使用关键字(33)和内置函数名(BIF)
# # 关于进制转化的内置函数  2进制bin()   8进制boct()    10进制int()    16进制hex()
# import keyword
# print(keyword.kwlist)#关键字
# print(dir(__builtins__))#内置函数

# # 数据类型：数字类型：(整数int  浮点数float 布尔bool 复数complex)   序列(字符串str 列表list 元组tuple)  字典dict 集合set
# # 数字 随机数random
# import random
# print(random.randint(10,11))#随机整数，左右闭
# print(random.random())   #随机0~1之间的小数
# print(random.uniform(10,50))   #随机范围内的小数
# print(random.choice('codemao编程猫'))  #随机字符
# # 没有返回值的打印None
# l = [2, 3, 4, 6, 7, 9]
# print(l)
# random.shuffle(l)  # 随机打乱一个序列,打乱原来序列
# print(l)
# print(random.sample('codemao编程猫',3))   #随机抽样，以列表的类型打印出来
# print(random.randrange(10,50,5))   #随机取数，左闭右开
# # numpy模块中array数组，模块可以包含很多随机的内容

# item='codemao编程猫'
# print(list(item))
# print(tuple(item))
# print(set(item))
# item4={'code':'mao','zhongzhi':222}
# for i in item4:
#     print(i)
# for i in item4.keys():
#     print(i)
# for i in item4.values():
#     print(i)
# for i in item4.items():   #以元组类型输出键值对
#     print(i)
# for k,v in item4.items():
#     print(k,"-",v)
# for _,v in item4.items():   #_为占位符
#     print(v)
# for k,_ in item4.items():   #_为占位符
#     print(k)

# x,y,*z=range(1,10)
# print(x)
# print(y)
# print(*z)   #解包后是3 4 5 6 7 8 9等7个数值
# print(z)  #以列表类型打印输出
# print(divmod(20,6))   #tuple(整除，求余)
# t=(20,6)
# print(divmod(*t))   #  *拆包，_拆包

# # 九九乘法表
# for i in range(1,10):
#     for j in range(1,i+1):
# "         print('%dx%d=%d\t'%(i,j,i*j),end='') "
#     print()

# for i in range(1, 10):
#     print('*'*i)
# print('6'*3 + 'codemao')
# l = [['1'], ['1'], ['1']] * 3
# print(l)
# x = ['1'] + ['2', '3']
# print(x)
# print(x*3)

# # while 循环 多个计数器 while True: 永远循环
# num = 1
# t = 1
# tnum = 0
# while num <= 5:
#     t = t * num
#     tnum += t
#     num += 1  #复合运行中的一个赋值
# print(tnum)

# # 条件分支  单分支 if  双分支 if...else  多分支 if...elif(...)...(else)
# # 闰年计算器
# # 能被4整除且不能被100整除的年份，或者是能被400整除的年份叫做闰年
# y = int(input('请输入年份：'))
# if y%400 == 0:
#     print('世纪闰年')
# else:
#     if y%4 == 0:
#         if y%100 == 0:
#             #if y%400 == 0:
#                 #print('世纪闰年')
#             #else:
#                 print('平年')
#         else:
#             print('普通闰年')

# y = int(input('请输入年份：'))
# if (y%4 == 0 and y%100 != 0) or y%400 == 0:
#     print('闰年')
# else:
#     print('平年')

# # 运算符
# # 水仙花数：各位数上的数字的三次方的和就是这个数
# for i in range(100,1000):
#     ge=i%10
#     shi=i//10%10
#     bai=i//100
#     if i==ge**3+shi**3+bai**3:
#         print(i,'是水仙花数')

# # 字符串 列表
# # 切片 常用方法
# aList=[1,3,5,6,8]
# print(aList[3])
# # list[start:end:step]   range[start:end:step] range(1,3)
# print(aList[:2])
# print(aList[2:])
# # 只有一个数字的时候能够清晰的看到有几个元素
# # 当有start和end的时候，end-start就是切片的元素数量
# # 可以很清楚的将列表分为两部分
# print(aList[:4:-2])
# print(aList[:4:2])
# print(aList[::-2])

# str1='ffff ggg cfd vfxscv gbhnt'.split()#以列表类型拆分：字符串转换成列表
# print(str1)
# print('vfc,gfvd,vfccd,xx,bfe,scdx'.split(','))
# str2='-'.join(str1)#以字符串类型合并：列表转换成字符串
# print(str2)

# # 添加元素：列表 字典集合（可变序列）
# s1=['eedfc',5,6842,'gddxx233']
# s1.append('张')#在列表后面添加元素
# print(s1)
# s1.extend(['a','b225',555])#在列表后面添加新列表
# print(s1)
# s1.insert(2,'52315')
# print(s1)

# # 删除列表
# s2=['eedfc',5,6842,'gddxx233','vvv','ggvd','zhang']
# del s2[2]
# print(s2)
# print(s2.pop(-1))
# print(s2)
# s2.remove('vvv')
# print(s2)

# # 排序
# s3=[6,5,8,1,9,0,7,5,2,0]
# s3.sort()   #sortd()
# print(s3)
