import os
import re
import os.path

inodebitmap=[0,0,0,0,0,0,0,0]
databitmap=[0,0,0,0,0,0,0,0]
inodes=[]
datas=[]

def create():
    global inodebitmap
    global databitmap
    #print(inodebitmap)
    #print(databitmap)
    path = os.path.split(str[str.find("(") + 2:str.find(")") - 1])
    #print(path)
    filename = path[0]
    #print(filename)
    filename1 = re.split('/',filename)
    #print(len(filename1)-1)
    #print(filename1)
    isExists = os.path.exists('E:/移动互联网应用技术/操作系统实验'+filename)
    if not isExists:
        f = open("E:/移动互联网应用技术/操作系统实验/磁盘.txt", "a+")
        f.write("目录名：" + filename+'\n')
        f.close()
        os.makedirs('E:/移动互联网应用技术/操作系统实验'+filename)
        print(filename + '创建成功！')
        i=0
        while i < len(filename1)-1:
            if inodebitmap[i] == 0:
                inodebitmap[i] = 1
                #print(i)
                print(filename1[i+1])
                print('inodebitmap',inodebitmap)
                inode = ['d']
                inode.append(i)
                print('inode',inode)
                inodes.append(inode)
                print('inodes',inodes)
            if databitmap[i] == 0:
                databitmap[i] = 1
                print('databitmap',databitmap)
                data1 = ('.',)
                data2 = (i,)
                data3 = data1 + data2
                print('datas',data3)
            else:
                i = i + 1
    else:
        print(filename + '已创建')
        show = os.listdir(os.chdir('E:/移动互联网应用技术/操作系统实验' + filename))
        print(show)
        #print(os.path.dirname(filename))
    print()

def openfile():
    path = os.path.split(str[str.find("open f") + 8:str.find(";") - 2])
    #print(path)
    filename = path[0]
    #print(filename)
    filename2=str[str.find("write") + 6:str.find(',')]
    #print(filename2)
    isExists = os.path.exists('E:/移动互联网应用技术/操作系统实验'+filename)
    os.chdir('E:/移动互联网应用技术/操作系统实验'+filename)
    isExists2 = os.path.exists(filename2)
    if not isExists:
        print('该目录没有创建')
    else:
        if not isExists2:
            f = open("E:/移动互联网应用技术/操作系统实验/磁盘.txt", "a+")
            f.write("目录名：" + filename+'/'+filename2+'\n')
            f.close()
            os.makedirs(filename+'/'+filename2)
            print(filename+'/'+filename2 + '创建成功！')
            i = 0
            while i < 8:
                if inodebitmap[i] == 0:
                    inodebitmap[i] = 1
                    print(inodebitmap)
                    break
                else:
                    i = i + 1
            inode = ['d']
            inode.append(i)
            print(inode)
            inodes.append(inode)
            print(inodes)
            y = 0
            while y < 8:
                if databitmap[y] == 0:
                    databitmap[y] = 1
                    print(databitmap)
                    break
                else:
                    y = y + 1
        else:
            print(filename+'/'+filename2 + '已创建')
            show = os.listdir(filename+'/'+filename2)
            print('show',show)
    print()

b=0
def mkdir():
    global b
    global count
    global inodebitmap
    global databitmap
    #print(inodebitmap)
    #print(databitmap)
    path=os.path.split(str[str.find("(") + 2:str.find(")")-1])
    #print(path)
    directorienametxt=path[1]
    filename=path[0]
    isExists = os.path.exists('E:/移动互联网应用技术/操作系统实验'+filename)
    if not isExists:
        print('该目录没有创建')
    else:
        os.chdir('E:/移动互联网应用技术/操作系统实验'+filename)
        if os.path.exists(directorienametxt) == 0:
            f = open("E:/移动互联网应用技术/操作系统实验/磁盘.txt", "a+")
            f.write("文件名：" + filename+'/'+directorienametxt + '\n')
            f.close()
            f = open(directorienametxt, "a+")
            f.close()
            print(directorienametxt + '创建成功！')
            i=0
            while i<8:
                if inodebitmap[i] == 0:
                    inodebitmap[i] = 1
                    b=i
                    #print(b)
                    print('inodebitmap',inodebitmap)
                    inode = ['f', -1]
                    inode.append(count)
                    print('inode',inode)
                    inodes.append(inode)
                    print('inodes',inodes)
                    print('databitmap',databitmap)
                    break
                else:
                    i=i+1
            return True
        else:
            print(directorienametxt + '已创建')
            show = os.listdir(os.chdir('E:/移动互联网应用技术/操作系统实验'+filename))
            print('show',show)
            return False
    print()

def opendirectorie():
    global b
    global count
    global inodebitmap
    global databitmap
    #print(inodebitmap)
    #print(databitmap)
    path = os.path.split(str[str.find("(") + 2:str.find(")") - 1])
    path1 = os.path.split(str[str.find("write") + 6:str.find(",")])
    path2 = re.split(',', str[str.find(".txt")+5:len(str) - 1])
    #print(path2)
    #print(path)
    #print(path1)
    directorienametxt = path1[1]
    filename = path[0]
    isExists = os.path.exists('E:/移动互联网应用技术/操作系统实验' + filename)
    if not isExists:
        print('没有该目录')
    else:
        os.chdir('E:/移动互联网应用技术/操作系统实验' + filename)
        if os.path.exists(directorienametxt) != 0:
            f = open("E:/移动互联网应用技术/操作系统实验/磁盘.txt", "a+")
            f.write("文件名：" + filename + '/' + directorienametxt + '\n')
            f.close()
            f = open(directorienametxt, "a+")
            #print(path2[0])
            f.write(path2[0]+'\n')
            f.close()
            #print(b)
            i=0
            while i<8:
                if databitmap[i] == 0:
                    databitmap[i] = 1
                    print('inodebitmap', inodebitmap)
                    print('databitmap',databitmap)
                    data1 = ('.',)
                    data2 = (i,)
                    data3 = data1 + data2
                    inode = ['f']
                    inode.append(i)
                    inode.append(count)
                    print('inode', inode)
                    #print(inodes[b])
                    inodes[b] = inode
                    #print(inodes[b])
                    print('inodes', inodes)
                    print('datas',data3)
                    break
                else:
                    i=i+1
        else:
            print(directorienametxt + '没创建')
            show = os.listdir(os.chdir('E:/移动互联网应用技术/操作系统实验' + filename))
            print('show',show)
            return False
    print()

count = 1
def link():
    global count
    global inodebitmap
    global databitmap
    print(inodebitmap)
    print(databitmap)
    # 打开文件
    path = str[str.find("link") + 6:str.find(',') - 1]
    path='E:/移动互联网应用技术/操作系统实验'+path
    #print(path)
    dst = str[str.find(",") + 2:str.find(')')-1]
    dst='E:/移动互联网应用技术/操作系统实验'+dst
    #print(dst)
    isExistspath = os.path.exists(path)
    isExistsdst=os.path.exists(dst)
    if isExistspath:
        if not isExistsdst:
            fd = os.open(path, os.O_RDWR | os.O_CREAT)
            # 关闭文件
            os.close(fd)
            # 创建以上文件的拷贝
            os.link(path, dst)
            print("创建硬链接成功!!")
            count +=1
            print('count',count)
            print('inodes', inodes)
            f = open("E:/移动互联网应用技术/操作系统实验/磁盘.txt", "a+")
            f.write("硬链接文件名：" + path+'\n')
            f.close()
        else:
            print('该目的地址已经创建硬链接')
    else:
        print('没有该源地址，请输入正确的目的地址')
    print()

def unlink():
    global count
    # 列出目录
    path = str[str.find("unlink") + 8:str.find(')')-1]
    path='E:/移动互联网应用技术/操作系统实验'+path
    #print(path)
    #print("目录为: %s" % os.listdir(os.getcwd()))
    isExistspath = os.path.exists(path)
    if isExistspath:
        count -= 1
        print('count',count)
        if count == 0:
            os.unlink(path)
            print('源地址已经删除')
        # 删除后的目录
            #print("删除后的目录为 : %s" % os.listdir(os.getcwd()))
    else:
        print('没有该源地址')
    print()

allFileNum = 0
def show(level, path):
    global allFileNum
    ''''' 
    打印一个目录下的所有文件夹和文件 
    '''
    # 所有文件夹，第一个字段是次目录的级别
    dirList = []
    # 所有文件
    fileList = []
    # 返回一个列表，其中包含在目录条目的名称(google翻译)
    files = os.listdir(path)
    # 先添加目录级别
    dirList.append(str(level))
    for f in files:
        if (os.path.isdir(path + '/' + f)):
            # 排除隐藏文件夹。因为隐藏文件夹过多
            if (f[0] == '.'):
                pass
            else:
                # 添加非隐藏文件夹
                dirList.append(f)
        if (os.path.isfile(path + '/' + f)):
            # 添加文件
            fileList.append(f)
            # 当一个标志使用，文件夹列表第一个级别不打印
    i_dl = 0
    for dl in dirList:
        if (i_dl == 0):
            i_dl = i_dl + 1
        else:
            # 打印至控制台，不是第一个的目录
            print('-' * (int(dirList[0])), dl)
            # 打印目录下的所有文件夹和文件，目录级别+1
            dir((int(dirList[0]) + 1), path + '/' + dl)
    for fl in fileList:
        # 打印文件
        print('-' * (int(dirList[0])), fl)
        # 随便计算一下有多少个文件
        allFileNum = allFileNum + 1

while(1):
    flag=0
    str=input("请输入指令：")
    if re.match(r"create", str, re.M|re.I):
        create()
        flag = 1
    if re.match(r"open f", str, re.M|re.I):
        openfile()
        flag = 1
    if re.match(r"mkdir", str, re.M|re.I):
        mkdir()
        flag=1
    if re.match(r"open", str, re.M | re.I):
        opendirectorie()
        flag = 1
    if re.match(r"link", str, re.M|re.I):
        link()
        flag = 1
    if re.match(r"unlink", str, re.M|re.I):
        unlink()
        flag=1
    if flag==0:
        print("非法命令！")
        a = int(input('1.显示所有目录和文件\n2.显示指定目录'))
        if a == 1:
            show(1, 'E:\\移动互联网应用技术\\操作系统实验\\')
            print('总文件数 =', allFileNum)
        elif a == 2:
            s = input('请输入要查看的目录')
            show(1, 'E:\\移动互联网应用技术\\操作系统实验\\' + s)
            print('总文件数 =', allFileNum)
'''
指令：
create('/s/a/d/')
mkdir('/s/a.txt')
open('/s/');write(a.txt,w,4)
link('/s/a.txt','/s/a/ss.txt')
unlink('/s/a/ss.txt')
'''