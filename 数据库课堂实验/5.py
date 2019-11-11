import os
import re
import itertools
import linecache

def select():
    i=int(input('qingshurushu:'))
    if i==1:
        tablename = str[str.find('from') + 5:str.find('where')-1]
        indexname = str[str.find("select")+7:str.find('from')-1]
        zhilinname=str[str.find("where")+6:str.find('==')-1]
        #print(zhilinname)
        iname=str[str.find('==')+2:]
        #print(iname)
        tablenamefile = tablename + '.txt'
        indexnamefile = indexname + '.txt'
        zhilinnamefile=zhilinname+'.txt'

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
                    #print(tup)
                    if tup[t1] == iname:
                        f_w.write(tup[t] + ' ')
                        print(tup[t])
                        continue
                        #print(tup[t1])
                    #f_w.write(tup[len(tup) - 1])
                    else:
                        print()
                    f_w.write('\n')
        else:
            print("表不存在，索引创建失败！")
    '''
    elif i==2:
        tablename1 = str[str.find('from') + 5:str.find(',')]
        tablename2 = str[str.find(',') + 1:str.find('where')-1]
        print(tablename2)
        indexname = str[str.find("select") + 7:str.find('from') - 1]
        zhilinname = str[str.find("where") + 6:str.find('==') - 1]
        # print(zhilinname)
        iname = str[str.find('==') + 2:]
        # print(iname)
        tablenamefile1 = tablename1 + '.txt'
        tablenamefile2 = tablename2 + '.txt'
        indexnamefile = indexname + '.txt'
        linecache.checkcache(tablenamefile1)
        count = linecache.getlines(tablenamefile1)
        s=linecache.getline(tablenamefile1,1)
        print(count)
        #print(s)
        ii=len(open(tablenamefile1, 'r').readlines())
        jj = len(open(tablenamefile2, 'r').readlines())
        print(ii)
        i=1
        j=1
        while i<ii:
            c = linecache.getline(tablenamefile1, i + 1)
            while j<jj:
                s=c.strip('\n')+','+linecache.getline(tablenamefile2,j+1)
                j=j+1
                #print(s)
            i = i + 1
            print(s)

        with open(tablenamefile1, "r") as f:
            lines1 = f.readlines()
            print(lines1)
        with open(tablenamefile2, "r") as f:
            lines2 = f.readlines()
        ff = []
        # for x in itertools.product(count1,count2):
        for x in itertools.product(lines1, lines2):
            #print(x)
            ff.append(x)
        print(ff)
        with open("t.txt", "a+") as f:
            f.write(ff)
            f.close()
        
        if os.path.exists(tfile):

            # 创建索引表
            with open(tablename1, "r") as f:
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
                # print(indexlist)
                # 排序后写入索引文件
                for i in range(len(indexlist)):
                    tup = indexlist[i]
                    # print(tup)
                    if tup[t1] == iname:
                        f_w.write(tup[t] + ' ')
                        print(tup[t])
                        continue
                        # print(tup[t1])
                    # f_w.write(tup[len(tup) - 1])
                    else:
                        print()
                    f_w.write('\n')
        else:
            print("表不存在，索引创建失败！")
        f=[]
        #for x in itertools.product(count1,count2):
        for x in itertools.product(lines1, lines2):
            print(x)
            f.append(x)
        print(f)
        '''
while(1):
    flag=0
    str=input("请输入指令：")
    if re.match(r"select", str, re.M | re.I):
        select()
        flag = 1