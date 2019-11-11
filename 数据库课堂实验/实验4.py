import os
import re
import itertools
import linecache

#split():以空格字符为分隔符进行划分
#strip():字符串开头和结尾的字符，空格和制表符和换行符都删除
#建立数据库表结构的功能(create table)eg:create table s(name char(10),age int(10))
def create() :
    tablename = str[13:str.find("(")]
    table = str[str.find("(")+1:len(str)-1]
    tablefile = tablename+'.txt'

    #如果表不存在则创建
    if os.path.exists(tablefile)==0 :
        #将表写入数据字典
        f = open("table.txt", "a+")
        f.write("表名："+tablename+"\n属性："+table+'\n')
        f.close()
        #创建表并写入属性
        f = open(tablefile, "a+")
        f.write(table+'\n')
        f.close()
        print("表已创建成功！")
    else :
        print("表已存在，创建失败！")

#删除表的功能(drop table)drop table s(表名)
def drop() :
    tablename = str[11:len(str)]
    tablefile = tablename+'.txt'
    if os.path.exists(tablefile) :
        #删除数据字典中表相关信息
        with open("table.txt", "r") as f:
            lines = f.readlines()
        with open("table.txt", "w") as f_w:
            a=1       #标志位(为了连续删除两行)
            for line in lines:
                if line.strip() == "表名："+tablename :
                    a=0
                    continue
                if a==0 :
                    a=1
                    continue
                f_w.write(line)
        os.remove(tablefile)
        print("表已删除！")
    else :
        print("表不存在，删除失败！")

#输入数据库记录的功能(insert into)eg:insert into s(ag,10)
def insert() :
    tablename = str[12:str.find("(")]
    tabletxt = re.split('[\']',str[str.find("(")+1:len(str)-1])
    tabletxtstr = "".join(list(tabletxt))
    tablefile = tablename+'.txt'
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
                    c=line.count(',')
                 #   print(c)
                    break
        if tabletxtstr.count(',')!=c:
            print("插入属性数量不匹配！")
    #如果表存在则插入
        else:
            f = open(tablefile, "a+")
            f.write(tabletxtstr+'\n')
            f.close()
            print("信息添加成功！")
    else :
        print("表不存在，信息添加失败！")

#显示数据库结构和内容(以表格形式显示)(select * from 关系名)select * from s(表名)
def select() :
    tablename = str[str.find('from') + 5:str.find('where') - 1]
    indexname = str[str.find("select") + 7:str.find('from')-1]
    zhilinname = str[str.find("where") + 6:str.find('==') - 1]
    # print(zhilinname)
    iname = str[str.find('==') + 2:]
    # print(iname)
    tablenamefile = tablename + '.txt'
    indexnamefile = indexname + '.txt'
    zhilinnamefile = zhilinname + '.txt'

    if os.path.exists(tablenamefile):

        # 创建索引表
        with open(tablenamefile, "r") as f:
            lines = f.readlines()
        with open(indexnamefile, "w") as f_w:
            c = 0
            indexlist = []
            for line in lines:
                if c == 0:
                    c = c + 1
                    t = line.count(",", 0, line.find(indexname))
                    t1 = line.count(",", 0, line.find(zhilinname))
                    continue

                line = line.strip('\n') + "," + '%d' % c  # 加上所在行数
                list = line.split(",")  # 以逗号进行分割
                indexlist.append(list)
                c = c + 1
            for i in range(len(indexlist)):
                tup = indexlist[i]
                # print(tup)
                if tup[t1] == iname:
                    f_w.write(tup[t])
                    print(tup[t])
                    continue
                    # print(tup[t1])
                # f_w.write(tup[len(tup) - 1])
                else:
                    print()
                f_w.write('\n')

#删除数据库记录的功能(delete)eg:delete s(qq,11)
def delete() :
    tablename = str[7:str.find("(")]
    tablefile = tablename + '.txt'
    deletetxt = re.split('[\']',str[str.find("(")+1:str.find(")")])
    deletetxtstr = "".join(list(deletetxt))
    a=0
    if os.path.exists(tablefile) :
        with open(tablefile, "r") as f:
            lines = f.readlines()
        with open(tablefile, "w") as f_w:
            for line in lines:
                if line.strip() == deletetxtstr:
                    a=1
                    continue
                f_w.write(line)
        if a==0 :
            print("数据不存在删除失败！")
        else :
            print("数据删除成功！")
    else :
        print("表不存在，信息删除失败！")

#修改数据库记录的功能(update)eg:update s set aq,1 to qa,13
def update() :
    tablename = str[7:str.find("set")-1]
    tablefile = tablename + '.txt'
    beforeupdate = re.split('[\']',str[str.find("set")+4:str.find("to")-1])
    beforeupdatestr = "".join(list(beforeupdate))
    afterupdate = re.split('[\']',str[str.find("to")+3:len(str)])
    afterupdatestr = "".join(list(afterupdate))
    a=0
    if os.path.exists(tablefile):
        with open(tablefile, "r") as f:
            lines = f.readlines()
        with open(tablefile, "w") as f_w:
            for line in lines:
                if line.strip() == beforeupdatestr:
                    a=1
                    f_w.write(afterupdatestr+'\n')
                    continue
                f_w.write(line)
        if a==0 :
            print("数据不存在修改失败！")
        else :
            print("数据修改成功！")
    else :
        print("表不存在，信息修改失败！")

#在已有的关系中添加属性的功能(alter table……add)eg:alter table s add(tel char(11))
def altertableAdd() :
    altertablename = str[12:str.find("add")-1]
    altertablefile = altertablename + '.txt'
    addtable = str[str.find("add")+4:len(str)]
    if os.path.exists(altertablefile) :
        #添加数据字典中属性
        with open("table.txt", "r") as f:
            lines = f.readlines()
        with open("table.txt", "w") as f_w:
            a=0
            for line in lines:
                if line.strip() == "表名："+altertablename :
                    a=1
                    f_w.write(line)
                    continue
                if a==1 :
                    f_w.write(line.strip("\n")+','+addtable+'\n')
                    a=0
                    continue
                f_w.write(line)
        print("属性已添加！")
        #添加表中的属性
        with open(altertablefile, "r") as f:
            lines = f.readlines()
        with open(altertablefile, "w") as f_w:
            a = 0
            for line in lines:
                if a==1 :
                    f_w.write(line.strip("\n")+','+addtable+'\n')
                    a=a+1
                    continue
                f_w.write(line)
                if a<3 :
                    a=a+1
    else:
        print("表不存在，添加属性失败！")

#从已有的关系中删除属性的功能(alter table……drop)eg:alter table s drop(tel char(11))
def altertableDrop() :
    altertablename = str[12:str.find("drop")-1]
    altertablefile = altertablename + '.txt'
    droptable = str[str.find("drop")+5:len(str)]
   # print(droptable)
    if os.path.exists(altertablefile) :
        #删除数据字典中属性
        with open("table.txt", "r") as f:
            lines = f.readlines()
        with open("table.txt", "w") as f_w:
            a = 0
            for line in lines:
                if line.strip() == "表名："+altertablename :
                    a = 1
                    f_w.write(line)
                    continue
                if a == 1:
                #    f_w.write(line+','+droptable+'\n')
                    line = line[3:len(line)]
                    line = line.split(',')
                 #   print(line)
                    for i in range(len(line)-1):
                        print(line[i])
                        if line[i].find(droptable)!=-1:
                        #    print("删除")
                            del line[i]
                            flag=i
                    line = ",".join(line)
                    attribute=line          #   记录删除后的属性行
                    f_w.write("属性:"+line+'\n')
                    a=0
                    continue
                f_w.write(line)
        print("属性已删除！")
        #删除表中的属性
        a=0
        with open(altertablefile, "r") as f:
            lines = f.readlines()
        with open(altertablefile, "w") as f_w:
            for line in lines:
                if a == 0:
                    f_w.write(line)
                    a = 1
                    continue
                if a == 1:
                    f_w.write(attribute+'\n')
                    a = 2
                    continue
                line = line.split(',')
                del line[flag]
                f_w.write(",".join(line))
    else :
        print("表不存在，删除属性失败！")

#创建索引(create index……on)create index sname（属性） on s（表名）
def createindex():
    indexname = str[13:str.find("on")-1]
    tablename = str[str.find("on")+3:len(str)]
    tablenamefile = tablename + '.txt'
    indexnamefile = indexname + '.txt'

    if os.path.exists(tablenamefile):
        #创建索引字典
        f = open("index.txt", "a+")
        f.write("表名："+tablename+"\n索引："+indexname+'\n')
        f.close()
        print("索引创建成功！")

        #创建索引表
        with open(tablenamefile, "r") as f:
            lines = f.readlines()
        with open(indexnamefile, "w") as f_w:
            c=0
            indexlist = []
            for line in lines:
                #不读第一行
                #if c==0:
                    #c=c+1
                    #continue
                #第几属性
                if c==0:
                    c = c + 1
                    t = line.count(",",0,line.find(indexname))
                    continue

                line = line.strip('\n')+","+'%d' %c       #加上所在行数
                list = line.split(",")#以逗号进行分割
                indexlist.append(list)
                c = c + 1
            #print(indexlist)
            linesort = sorted(indexlist, key= lambda x: x[t])
            #print(linesort)
            #排序后写入索引文件
            for i in range(len(linesort)):
                tup = linesort[i]
                #print(tup)
                f_w.write(tup[t]+' ')
                f_w.write(tup[len(tup)-1])
                f_w.write('\n')
    else:
        print("表不存在，索引创建失败！")

#删除索引(drop index……on)drop index name(属性) on s(表名)
def dropindex():
    indexname = str[11:str.find("on")-1]
    tablename = str[str.find("on")+3:len(str)]
    indexnamefile = indexname+'.txt'
    tablefile = tablename+'.txt'
    if os.path.exists(indexnamefile) :
        #删除索引字典中表相关信息
        with open("index.txt", "r") as f:
            lines = f.readlines()
        with open("index.txt", "w") as f_w:
            a=0       #标志位(为了连续删除两行)
            for line in lines:
                if line.strip() == "表名："+tablename:
                    temp = line
                    a=1
                    continue
                if a==1 :
                    if line.strip() == "索引："+indexname:
                        a=2
                        continue
                    else:
                        f_w.write(temp)
                f_w.write(line)
        os.remove(indexnamefile)
        print("索引已删除！")
    else :
        print("索引不存在，删除失败！")


#主函数
'''while(1) :
    a=0
    name = "口令："+input("请输入口令：")
    key = "密码："+input("请输入密码：")
    with open('userfile.txt', "r") as f:
        lines = f.readlines()
    for line in lines:
        if line.strip() == name:
            a = 1
            continue
        if line.strip() == key and a==1:
            a = 2
            break
    if a==0:
        print("口令错误！")
    if a==1:
        print("密码错误！")
    if a==2:
        print("————————————————————")
        break
'''
while(1):
    flag=0
    str=input("请输入指令：")
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
    if flag==0:
        print("非法命令！")