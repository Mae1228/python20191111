'''
学员管理系统
1.	数据基本要求：姓名、年龄、成绩
2.	系统要求：
１）添加学生信息
２）显示所有学生的信息
３）删除学生信息
４）修改学生信息
５）按学生成绩高－低显示学生信息
６）按学生成绩低－高显示学生信息
７）按学生年龄高－低显示学生信息
８）按学生年龄低－高显示学生信息
退出：其他任意按键
'''
#学员管理系统 - c、java
#1.添加学员信息
#2.查询学员信息
#3.修改学员信息
#4.删除学员信息
#5.根据成绩高低进行排序
#6.根据成绩低高进行排序
#7.根据年龄高低进行排序
#8.根据年龄低高进行排序
#数据-列表、字典
#界面-控制台
#存放学员信息(使用二维列表进行学员信息存放)

#定义添加学员的函数
def add_student():
    age = int(input("学员年龄"))
    name = input("学员姓名")
    grade = int(input("学员成绩"))
    student = [age, name, grade]
    student_list.append(student)
    print("添加成功")

#查询全部学员
def select_all():
    print("********************学员信息列表*******************")
    # 遍历列表
    for x in range(0, len(student_list)):
        student = student_list[x]
        select_name = student[1]
        select_age = student[0]
        select_grade = student[2]
        print('序号：', x, '姓名：', select_name, '成绩', select_grade, '年龄', select_age)

#根据姓名进行查询
def select_byname():
    select_result = True
    select_name = input("请输入要查询学员的姓名：")
    for x in range(0,len(student_list)):
        student = student_list[x]
        if select_name == student[1]:
            select_result = False
            print('序号',x,'年龄',student[0],'姓名',student[1],'成绩',student[2])

    if select_result:
        print("未找到该学员")

#根据成绩进行查询
def select_bytel():
    select_result = True
    select_grade = input("请输入要查询学员的成绩：")
    for x in range(0, len(student_list)):
        student = student_list[x]
        if select_grade == student[2]:
            select_result = False
            print('序号', x, '年龄', student[0], '姓名', student[1], '成绩', student[2])

    if select_result:
        print("未找到该学员")

#根据年龄进行查询
def select_byid():
    select_result = True
    select_age = input("请输入要查询学员的年龄：")
    for x in range(0, len(student_list)):
        student = student_list[x]
        print(student)
        if select_age == student[0]:
            select_result = False
            print('序号', x, '年龄', student[0], '姓名', student[1], '成绩', student[2])

    if select_result:
        print("未找到该学员")

#修改学员信息
def update():
    if len(student_list) == 0:
        print("没有学员信息")
        return
    select_all()
    update_num = input("输入要修改的学员序号：")
    update_num = int(update_num)
    while update_num not in range(0,len(student_list)):
        update_num = int(input("请正确输入学员序号，学员序号为："))
    student = student_list[update_num]
    update_age = input("输入修改后的学员年龄(%s)"%student[0])
    update_name= input("输入修改后学员姓名(%s)"%student[1] )
    update_grade = input("输入修改后学员成绩(%s)"%student[2])
    student[0] = update_age
    student[1] = update_name
    student[2] = update_grade
    print("修改成功")

#删除学员
def del_student():
    print("1.全部删除")
    print("2.按序号删除")
    del_num = int(input("请选择要操作的序号："))
    while del_num not in range(0,3):
        del_num = int(input("请正确输入操作序号："))
    if del_num == 1:
        student_list.clear()
        print("全部清空")
    else:
        select_all()
        num = int(input("请输入要删除的学员序号"))
        student_list.pop(num)
        print("删除成功")

#5.根据成绩高低进行排序
def gradegao():
    select_all()
    s = []
    for x in range(0, len(student_list)):
        student = student_list[x]
        gradegao = student[2]
        s.append(gradegao)
    print('源数据：',s)
    s.sort()
    s.reverse()
    print('根据成绩高低进行排序：',s)

#6.根据成绩低高进行排序
def gradedi():
    select_all()
    s = []
    for x in range(0, len(student_list)):
        student = student_list[x]
        gradedi = student[2]
        s.append(gradedi)
    print('源数据：', s)
    s.sort()
    print('根据成绩低高进行排序：',s)

#7.根据年龄高低进行排序
def agegao():
    select_all()
    s = []
    for x in range(0, len(student_list)):
        student = student_list[x]
        agegao = student[0]
        s.append(agegao)
    print('源数据：', s)
    s.sort()
    s.reverse()
    print('根据年龄高低进行排序：',s)

#8.根据年龄低高进行排序
def agedi():
    select_all()
    s = []
    for x in range(0, len(student_list)):
        student = student_list[x]
        agedi = student[0]
        s.append(agedi)
    print('源数据：', s)
    s.sort()
    print('根据年龄低高进行排序：',s)

student_list = [[21,'Tom',80],[20,'Lily',90]]

while True:
    print("1.添加学员")
    print("2.修改学员")#通过序号进行修改
    print("3.查询学员")
    print("4.删除学员")#1.删除单个人2.删除全部
    print("5.根据成绩高低进行排序")
    print("6.根据成绩低高进行排序")
    print("7.根据年龄高低进行排序")
    print("8.根据年龄低高进行排序")
    print("0.退出程序")
    num = input("请进行操作选择")
    num = int(num)
    if num == 1:
        add_student()
    elif num == 2:
        update()
    elif num == 3:
        print("1.查询全部学员")
        print("2.根据年龄进行查询")
        print("3.根据姓名进行查询")#不考虑姓名重复
        print("4.根据成绩进行查询")
        select_num = input("请输入操作序号：")
        select_num = int(select_num)
        #用户输入检测，当用户输入正确，才进行流程控制。不正确，在循环中一直运行
        while select_num not in range(1,5):
            select_num = int(input("请正确输出操作："))
        #1.查询全部学员
        if select_num == 1:
            select_all()
        #2.根据年龄进行查询
        elif select_num == 2:
            select_byid()
        #3.根据姓名进行查询
        elif select_num == 3:
            select_byname()
        #4.根据成绩进行查询
        elif select_num == 4:
            select_bytel()
    elif num == 4:
       del_student()
    elif num == 5:
        gradegao()
    elif num == 6:
        gradedi()
    elif num == 7:
        agegao()
    elif num == 8:
        agedi()
    elif num == 0:
        print("程序退出")
        break
    else :
        print("请正确选择")
