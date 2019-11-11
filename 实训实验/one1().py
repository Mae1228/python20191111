#单行注释
'''多行注释：3单引号或者3个双引号'''
"""
python简介：动态的面向对象的脚本语言（解释执行）
    1989年发布，自带库：系统曹操作sys，时间操作time，文件操作，
                        CGI服务器，网络，数据库操作
    完善第三方库：pygame,dyango,beautifulsoup......
    应用于大型的服务器：B/S模式项目开发  两大类（电商，资源）
    人工智能领域
    数据挖掘与分析
"""
'''python基础
缩进：python程序的作用域相当于{}
变量：程序中的最小单元
    数据类型：字符串str
              数值（int整型，float浮点）
              布尔bool
    多个数：列表list，元组，set集合，字典
'''
username='hello'
print(username,type(username))
age=18
print(age,type(age))
salary=8888.88
print(salary,type(salary))
iswork=True
print(iswork,type(iswork))

name_list=['你好','我好','他好']
print(name_list,type(name_list))
print(name_list[2])
# print(name_list[20])下标越界异常
# 获取列表中的值和对应的下标
for i in name_list:
    print(i,name_list.index(i))
# 练习：输入10个名字，存储起来，当输入打印时，输出所有名字
# sun=[]
# i=0
# while i<10:
#     name=input('输入你的名字')
#     sun.append(name)
#     i=i+1
# a=input('请输入指令：')
# if a=='打印':
#     for i in sun:
#         print(i,end=' ，')
#
# sun1=[]
# for i in range(0,11):
#     sun1.append(i)
#     print(i)
names=[]
for i in range(1,11):
    vv=input("请输入名字"+str(i))
    names.append(vv)
    if vv=='打印':
        print('名字分别是：',end='')
    for name in names:
        if names.index(name)==len(names)-1:
            print(name,end='\t')
        else:
            print(name,',',end='\t')
    break



