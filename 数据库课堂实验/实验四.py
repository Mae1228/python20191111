import os
import re


# 建立数据库表结构的功能(create table)
def create():
    tablename = str[13:str.find("(")]
    table = str[str.find("(") + 1:len(str) - 1]
    tablefile = tablename + '.txt'

    # 如果表不存在则创建
    if os.path.exists(tablefile) == 0:
        # 将表写入数据字典
        f = open("table.txt", "a+")
        f.write("\n表名：" + tablename + "\n属性：" + table)
        f.close()
        # 创建表并写入属性
        f = open(tablefile, 'w')
        f.write("\n" + table)
        f.close()
        print("表已创建成功！")
    else:
        print("表已存在，创建失败！")


# 删除表的功能(drop table)
def drop():
    tablename = str[11:len(str)]
    tablefile = tablename + '.txt'
    if os.path.exists(tablefile):
        # 删除数据字典中表相关信息
        with open("table.txt", "r") as f:
            lines = f.readlines()
        with open("table.txt", "w") as f_w:
            a = 1  # 标志位(为了连续删除两行)
            for line in lines:
                if line.strip() == "表名：" + tablename:
                    a = 0
                    continue
                if a == 0:
                    a = 1
                    continue
                f_w.write(line)
        os.remove(tablefile)
        print("表已删除！")
    else:
        print("表不存在，删除失败！")


# 输入数据库记录的功能(insert into)
def insert():
    tablename = str[12:str.find("(")]
    tabletxt = re.split('[\']', str[str.find("(") + 1:len(str) - 1])
    tabletxtstr = "".join(list(tabletxt))
    tablefile = tablename + '.txt'
    if os.path.exists(tablefile):
        with open("table.txt", "r") as f:
            lines = f.readlines()
            # with open("table.txt", "w") as f_w:
            a = 0
            for line in lines:
                if line.strip() == "表名：" + tablename:
                    a = 1
                    continue
                if a == 1:
                    c = line.count(',')
                    #   print(c)
                    break
        if tabletxtstr.count(',') != c:
            print("插入属性数量不匹配！")
        # 如果表存在则插入
        else:
            f = open(tablefile, "a+")
            f.write("\n" + tabletxtstr)
            f.close()
            print("信息添加成功！")
    else:
        print("表不存在，信息添加失败！")


# 显示数据库结构和内容(以表格形式显示)(select * from 关系名)
def select():
    tablename = str[14:len(str)]
    tablefile = tablename + '.txt'
    f = open(tablefile).read()
    print(f)


# 删除数据库记录的功能(delete)
def delete():
    tablename = str[7:str.find("(")]
    tablefile = tablename + '.txt'
    deletetxt = re.split('[\']', str[str.find("(") + 1:str.find(")")])
    deletetxtstr = "".join(list(deletetxt))
    a = 0
    if os.path.exists(tablefile):
        with open(tablefile, "r") as f:
            lines = f.readlines()
        with open(tablefile, "w") as f_w:
            for line in lines:
                if line.strip() == deletetxtstr:
                    a = 1
                    continue
                f_w.write(line)
        if a == 0:
            print("数据不存在删除失败！")
        else:
            print("数据删除成功！")
    else:
        print("表不存在，信息删除失败！")


# 修改数据库记录的功能(update)
def update():
    tablename = str[7:str.find("set") - 1]
    tablefile = tablename + '.txt'
    beforeupdate = re.split('[\']', str[str.find("set") + 4:str.find("to") - 1])
    beforeupdatestr = "".join(list(beforeupdate))
    afterupdate = re.split('[\']', str[str.find("to") + 3:len(str)])
    afterupdatestr = "".join(list(afterupdate))
    a = 0
    if os.path.exists(tablefile):
        with open(tablefile, "r") as f:
            lines = f.readlines()
        with open(tablefile, "w") as f_w:
            for line in lines:
                if line.strip() == beforeupdatestr:
                    a = 1
                    f_w.write(afterupdatestr + '\n')
                    continue
                f_w.write(line)
        if a == 0:
            print("数据不存在修改失败！")
        else:
            print("数据修改成功！")
    else:
        print("表不存在，信息修改失败！")


# 在已有的关系中添加属性的功能(alter table……add)
def altertableAdd():
    altertablename = str[12:str.find("add") - 1]
    altertablefile = altertablename + '.txt'
    addtable = str[str.find("add") + 4:len(str)]
    if os.path.exists(altertablefile):
        # 添加数据字典中属性
        with open("table.txt", "r") as f:
            lines = f.readlines()
        with open("table.txt", "w") as f_w:
            a = 0
            for line in lines:
                if line.strip() == "表名：" + altertablename:
                    a = 1
                    f_w.write(line)
                    continue
                if a == 1:
                    f_w.write(line.strip("\n") + ',' + addtable + '\n')
                    a = 0
                    continue
                f_w.write(line)
        print("属性已添加！")
        # 添加表中的属性
        with open(altertablefile, "r") as f:
            lines = f.readlines()
        with open(altertablefile, "w") as f_w:
            a = 0
            for line in lines:
                if a == 1:
                    f_w.write(line.strip("\n") + ',' + addtable + '\n')
                    a = a + 1
                    continue
                f_w.write(line)
                if a < 3:
                    a = a + 1
    else:
        print("表不存在，添加属性失败！")


# 从已有的关系中删除属性的功能(alter table……drop)
def altertableDrop():
    altertablename = str[12:str.find("drop") - 1]
    altertablefile = altertablename + '.txt'
    droptable = str[str.find("drop") + 5:len(str)]
    # print(droptable)
    if os.path.exists(altertablefile):
        # 删除数据字典中属性
        with open("table.txt", "r") as f:
            lines = f.readlines()
        with open("table.txt", "w") as f_w:
            a = 0
            for line in lines:
                if line.strip() == "表名：" + altertablename:
                    a = 1
                    f_w.write(line)
                    continue
                if a == 1:
                    #    f_w.write(line+','+droptable+'\n')
                    line = line[3:len(line)]
                    line = line.split(',')
                    #   print(line)
                    for i in range(len(line) - 1):
                        print(line[i])
                        if line[i].find(droptable) != -1:
                            #    print("删除")
                            del line[i]
                            flag = i
                    line = ",".join(line)
                    attribute = line  # 记录删除后的属性行
                    f_w.write("属性:" + line + '\n')
                    a = 0
                    continue
                f_w.write(line)
        print("属性已删除！")
        # 删除表中的属性
        a = 0
        with open(altertablefile, "r") as f:
            lines = f.readlines()
        with open(altertablefile, "w") as f_w:
            for line in lines:
                if a == 0:
                    f_w.write(line)
                    a = 1
                    continue
                if a == 1:
                    f_w.write(attribute + '\n')
                    a = 2
                    continue
                line = line.split(',')
                del line[flag]
                f_w.write(",".join(line))
    else:
        print("表不存在，删除属性失败！")


# 创建索引(create index……on)
def createindex():
    indexname = str[13:str.find("on") - 1]
    tablename = str[str.find("on") + 3:len(str)]
    tablenamefile = tablename + '.txt'
    indexnamefile = indexname + '.txt'

    if os.path.exists(tablenamefile):
        # 创建索引字典
        f = open("index.txt", "a+")
        f.write("\n表名：" + tablename + "\n索引：" + indexname)
        f.close()
        print("索引创建成功！")

        # 创建索引表
        with open(tablenamefile, "r") as f:
            lines = f.readlines()
        with open(indexnamefile, "w") as f_w:
            c = 0
            indexlist = []
            for line in lines:
                # 不读第一行
                if c == 0:
                    c = c + 1
                    continue
                # 第几属性
                if c == 1:
                    c = c + 1
                    t = line.count(",", 0, line.find(indexname))
                    continue
                line = line.strip('\n') + "," + '%d' % c  # 加上所在行数
                list = line.split(",")
                indexlist.append(list)
                c = c + 1
            linesort = sorted(indexlist, key=lambda x: x[t])
            # 排序后写入索引文件
            for i in range(len(linesort)):
                tup = linesort[i]
                f_w.write(tup[t] + ' ')
                f_w.write(tup[len(tup) - 1])
                f_w.write('\n')
    else:
        print("表不存在，索引创建失败！")


# 删除索引(delete index……on)
def dropindex():
    indexname = str[11:str.find("on") - 1]
    tablename = str[str.find("on") + 3:len(str)]
    indexnamefile = indexname + '.txt'
    tablefile = tablename + '.txt'
    if os.path.exists(indexnamefile):
        # 删除索引字典中表相关信息
        with open("index.txt", "r") as f:
            lines = f.readlines()
        with open("index.txt", "w") as f_w:
            a = 0  # 标志位(为了连续删除两行)
            for line in lines:
                if line.strip() == "表名：" + tablename:
                    temp = line
                    a = 1
                    continue
                if a == 1:
                    if line.strip() == "索引：" + indexname:
                        a = 2
                        continue
                    else:
                        f_w.write(temp)
                f_w.write(line)
        os.remove(indexnamefile)
        print("索引已删除！")
    else:
        print("索引不存在，删除失败！")


# 建立用户
def setuser():
    username = str[str.find("to") + 3:str.find(",")]
    userpass = str[str.find(",") + 1:str.find("on") - 1]
    power = str[str.find("on") + 3:len(str)]
    f = open("user.txt", "a+")
    f.write("\n用户名：" + username + "\n密码：" + userpass + "\n权限：" + power)
    f.close()
    print("用户创建成功！")


# 选择算法
def selectalg1(condition, times):
    result = []
    c = 0
    row = 0
    symbol = 0
    select = str[str.find("select") + 7:str.find("from") - 1]
    selectfrom = str[str.find("from") + 5:str.find("where") - 1]
    # 分割查询结果
    selectlist = select.split(",")
    # 按不同运算符分割条件
    if condition.find("=") != -1:
        symbol = 1
        attribute = condition[0:condition.find("=")]
        value = condition[condition.find("=") + 1:len(condition)]
    if condition.find("<") != -1:
        symbol = 2
        attribute = condition[0:condition.find("<")]
        value = condition[condition.find("<") + 1:len(condition)]
    if condition.find(">") != -1:
        symbol = 3
        attribute = condition[0:condition.find(">")]
        value = condition[condition.find(">") + 1:len(condition)]

    if os.path.exists(selectfrom + '.txt'):
        if times == 1:  # 第一个查询条件
            with open(selectfrom + '.txt', "r") as f:
                lines = f.readlines()
        else:
            with open("middle.txt", "r") as f:
                lines = f.readlines()
            with open("middle.txt", "w") as f:
                f.truncate()

        for line in lines:
            if c == 0 and times == 1:
                c = c + 1
                continue
            if c == 1 and times == 1:
                t = line.count(",", 0, line.find(attribute))  # 操作域属性位置
                for i in range(len(selectlist)):  # 投影域属性位置（数组）
                    result.append(line.count(",", 0, line.find(selectlist[i])))
                c = c + 1
                continue

            if times != 1 and c==0:
                with open(selectfrom + '.txt', "r") as f:
                    lines = f.readlines()
                for line1 in lines:
                    if row == 0:
                        row=row+1
                        continue
                    if row == 1:
                        t = line1.count(",", 0, line1.find(attribute.strip(" ")))  # 操作域属性位置
                        #print(attribute)
                        c = c+1
                        break

            list = line.split(",")
            #print(line)
            if symbol == 1:  # 等于
                #print(list[t].strip('\n'),value.strip(" "))
                if list[t].strip('\n') == value.strip(" "):
                    f = open("middle.txt", "a+")
                    f.write(line)
                    f.close()

            if symbol == 2:  # 小于
                if list[t].strip('\n') < value.strip(" "):
                    f = open("middle.txt", "a+")
                    f.write(line)
                    f.close()

            if symbol == 3:  # 大于
                if list[t].strip('\n') > value.strip(" "):
                    f = open("middle.txt", "a+")
                    f.write(line)
                    f.close()
        times = times + 1
    else:
        print("表不存在，查询失败！")
    return result

# 选择
def selectalg():
    times = 1
    symbol = 0
    c = 0
    result = []
    ff = []
    select = str[str.find("1select") + 7:str.find("from") - 1]
    # selectfrom = str[str.find("from")+5:str.find("where")-1]
    fromwheres = str[str.find("where") + 6:len(str)]
    # 分割查询条件
    fromwhere = fromwheres.split("and")
    # 分割查询结果
    # selectlist = select.split(",")
    for i in range(len(fromwhere)):  # 循环调用选择函数
        if i > 0:
            times = 2
        if i==0:
            result = selectalg1(fromwhere[i], times)
        else:
            ff = selectalg1(fromwhere[i], times)

    with open("middle.txt", "r") as f:
        lines = f.readlines()
    #print(open("middle.txt").read())

    for line in lines:  # 投影
        list = line.split(",")
        for i in range(len(result)):
            print(list[result[i]])
    f = open("middle.txt", "r+")
    f.truncate()
    f.close()


# 连接算法
def connection1(table,condition):
    c1=0
    c2=0
    conditionlist = condition.split("=")     #属性
    with open(table + '.txt', "r") as f1:     #读取第二个表
        lines1 = f1.readlines()
    with open('middle.txt', "r") as f2:     #读取middle中的第一个表
        lines2 = f2.readlines()
    with open('middle.txt', "w") as f_w:
        for line1 in lines1:
            for line2 in lines2:
                if c1==0:
                    c1=c1+1
                    break
                if c2==0:
                    f_w.write(line2)
                    c2=c2+1
                    continue
                if c2==1:
                    f_w.write(line1.strip("\n")+","+line2)
                    #print(conditionlist[0],conditionlist[1])
                    #print(line1)
                    option1 = line2.count(",", 0, line2.find(conditionlist[0])+1)
                    option2 = line1.count(",", 0, line1.find(conditionlist[1])+1)
                    #print(line1.find(conditionlist[1]))
                    #print(option1,option2)
                    c2=c2+1
                    break
                else:
                    line1list = line1.split(",")
                    line2list = line2.split(",")
                    #print(line2list[option1])
                    #print(line1list[option2])

                    if len(line2list)==1:
                        continue
                    if line2list[option1]==line1list[option2]:

                        f_w.write(line1.strip("\n")+","+line2)
    #print(open("middle.txt").read())

# 连接
def connection():
    result = []
    c=0
    select = str[str.find("2select") + 7:str.find("from") - 1]
    selectfrom = str[str.find("from")+5:str.find("where")-1]
    table = selectfrom.split(",")   #分割表
    fromwheres = str[str.find("where") + 6:len(str)]
    # 分割查询条件
    fromwhere = fromwheres.split("and")
    # 分割查询结果
    selectlist = select.split(",")
    with open(table[0] + '.txt', "r") as f:     #将第一个表写入middle
        lines = f.readlines()
    with open('middle.txt', "w") as f_w:
        for line in lines:
            f_w.write(line)

    #print(open("middle.txt").read())

    for i in range(1,len(table)):      #循环调用连接函数
        #print(fromwhere[i-1].strip(" "))
        connection1(table[i],fromwhere[i-1].strip(" "))

    with open("middle.txt", "r") as f:
        lines = f.readlines()
    #print(open("middle.txt").read())

    for line in lines:  # 投影
        list = line.split(",")
        if c==0:
            c=c+1
            continue
        if c==1:
            for i in range(len(selectlist)):
                result.append(line.count(",", 0, line.find(selectlist[i].strip(" "))))
            c=c+1
            continue
        #print(result[0],result[1])
        for i in range(len(result)):
            print(list[result[i]])
    print(open("middle.txt").read())
    f = open("middle.txt", "r+")
    f.truncate()
    f.close()




#主函数
while(1) :

    a = 0
    king = 0      #是否为管理员
    name = input("请输入用户名：")
    key = input("请输入密码：")
    with open('userfile.txt', "r") as f:
        lines = f.readlines()
    for line in lines:
        if line.strip() == "用户名："+name:
            a = 1
            continue
        if line.strip() == "密码："+key and a==1:
            a = 2
            king = 1
            power = "king"
            break
    if king == 0:
        with open('user.txt', "r") as f:
            lines = f.readlines()
        for line in lines:
            if line.strip() == "用户名："+name:
                a = 1
                continue
            if line.strip() == "密码："+key and a == 1:
                a = 2
                continue
            if a == 2:
                power = line   #记录权限
                break
    if a==0:
        print("口令错误！")
    if a==1:
        print("密码错误！")
    if a==2:
        print("————————————————————")
        break

while (1):
    flag = 0
    str = input("请输入指令：")
    #selectalg()
    #connection()

    if power.find("s")!=-1 and power.find("c")!=-1:   #只有查询和建立表格权限
        if re.match(r"select", str, re.M | re.I):
            select()
            flag = 1

        if re.match(r"create table", str, re.M | re.I):
            create()
            flag = 1

        if flag == 0:
            print("非法命令！")

    elif power.find("s")!=-1:                      #只有查询权限
        if re.match(r"select", str, re.M | re.I):
            select()
            flag = 1

        if flag == 0:
            print("非法命令！")

    elif power.find("c")!=-1:                      #只有建立表格权限
        if re.match(r"create table", str, re.M | re.I):
            create()
            flag = 1

        if flag == 0:
            print("非法命令！")

    elif power.find("king")!=-1:                   #拥有所有权限
        if re.match(r"create table", str, re.M|re.I):
            create()
            flag = 1
        if re.match(r"insert into", str, re.M|re.I):
            insert()
            flag = 1
        if re.match(r"drop table", str, re.M|re.I):
            drop()
            flag=1
        if re.match(r"select", str, re.M|re.I):
            select()
            flag = 1
        if re.match(r"delete", str, re.M|re.I):
            delete()
            flag = 1
        if re.match(r"update", str, re.M|re.I):
            update()
            flag = 1
        if re.match(r"alter table", str, re.M|re.I):
            if re.search( r"add", str, re.M|re.I):
                altertableAdd()
                flag = 1
            if re.search( r"drop", str, re.M|re.I):
                altertableDrop()
                flag = 1
        if re.match(r"create index", str, re.M | re.I):
            createindex()
            flag = 1
        if re.match(r"drop index", str, re.M | re.I):
            dropindex()
            flag = 1
        if re.match(r"set user", str, re.M | re.I):
            setuser()
            flag = 1
        if re.match(r"1select", str, re.M|re.I):
            selectalg()
            flag = 1
        if re.match(r"2select", str, re.M|re.I):
            connection()
            flag = 1

        if flag==0:
            print("非法命令！")