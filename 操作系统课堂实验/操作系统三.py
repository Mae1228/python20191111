
def Create(name):
    Files.append(name)
    if name.count("/", 0,len(name))==1:
        print("########")
        name = name[1:len(name)]
        inodes[0]=inodes[0][0:9]+chr(ord(inodes[0][9])+1)+"]"
        #inodes[0] = inodes[0][0:len(inodes[0]) - 3] + chr(ord(inodes[0][len(inodes[0]) - 3]) + 1) + "]"
        for i in range(8):
            if inodebitmap[i]=="0":
                inodebitmap[i]="1"
                break
        inodes[i]="[f a:-1 r:1]"
        datablocks[0]=datablocks[0][0:len(datablocks[0])-1]+"("+name+","+'%d' % i+")]"
    else:
        print("^^^^^^^^^^")
        namelist = name.split("/")
        for i in range(8):
            if inodebitmap[i]=="0":
                inodebitmap[i]="1"
                break
        inodes[i]="[f a:-1 r:1]"
        w = int(datablocks[0].find(namelist[1])+2)
        s = int(datablocks[0][w])
        l = int(inodes[s][5])
        datablocks[l]=datablocks[l][0:len(datablocks[l])-2]+ "("+namelist[2]+","+'%d' % i+")]"

def Open(name):
    for i in range(16):
        if databitmap[i]=="0":
            databitmap[i]="1"
            break
    datablocks[i]="["+name+"]"

    for j in range(16):
        if datablocks[j].find(name)!=-1:
            w = int(datablocks[j].find(name) + 2)
            break
    #print(w)
    s = int(datablocks[j][w])
    #print(s)
    inodes[s]=inodes[s][0:5]+'%d' % i+" r:1]"

def Mkdir(name):
    Directories.append(name)
    for i in range(8):
        if inodebitmap[i]=="0":
            inodebitmap[i]="1"
            break
    for j in range(16):
        if databitmap[j]=="0":
            databitmap[j]="1"
            break
    #inodes[0] = inodes[0][0:len(inodes[0])-3] + chr(ord(inodes[0][len(inodes[0])-3]) + 1) + "]"
    inodes[0] = inodes[0][0:9] + chr(ord(inodes[0][9]) + 1) + "]"
    inodes[i]= "[d a:"+'%d' % j+" r:2]"
    datablocks[0] = datablocks[0][0:len(datablocks[0]) - 1] + "(" + name + "," + '%d' % i + ")]"
    datablocks[j] = "[(.,"+'%d' % i + ")(..,0)] "

def Link(name):
    Files.append(name)
    namelist = name.split(",")
    namelist[0]=namelist[0][1:len(namelist[0])]
    namelist[1] = namelist[1][1:len(namelist[1])]
    w = int(datablocks[0].find(namelist[0]) + 2)
    s = int(datablocks[0][w])
    datablocks[0]=datablocks[0][0:len(datablocks[0])-1]+"("+namelist[1]+","+'%d' % s+")]"
    inodes[0] = inodes[0][0:9] + chr(ord(inodes[0][9]) + 1) + "]"
    inodes[s] = inodes[s][0:len(inodes[s])-2] + chr(ord(inodes[s][len(inodes[s])-2]) + 1) + "]"

def Unlink(name):
    for i in range(len(Files)):
        if Files[i].find(name)!=-1:
            Files.remove(Files[i])
            break
    name = name[1:len(name)]
    c = int(datablocks[0].find(name) - 1)
    w = int(datablocks[0].find(name) + 2)
    s = int(datablocks[0][w])
    datablocks[0]=datablocks[0][0:c]+"]"
    inodes[0] = inodes[0][0:9] + chr(ord(inodes[0][9]) - 1) + "]"
    inodes[s] = inodes[s][0:len(inodes[s])-2] + chr(ord(inodes[s][len(inodes[s])-2]) - 1) + "]"


inodes=8
data_blocks=16
inodebitmap =[]
inodes = []
databitmap = []
datablocks = []
Files =[]
Directories =['/']
#初始化位示图
for i in range(8):
    if i==0:
        inodebitmap.append("1")
        inodes.append("[d a:0 r:2]")
    inodebitmap.append("0")
    inodes.append("[]")
for i in range(16):
    if i==0:
        databitmap.append("1")
        datablocks.append("[(.,0)(..,0)]")
    databitmap.append("0")
    datablocks.append("[]")


while(1):
    for j in range(8):
        print(inodebitmap[j],end="")
    print("\n")
    for j in range(8):
        print(inodes[j],end="")
    print("\n")
    for j in range(16):
        print(databitmap[j],end="")
    print("\n")
    for j in range(16):
        print(datablocks[j],end="")
    print("\n")
#空闲inode
    for i in range(8):
        if inodebitmap[i]=="0":
            break
    print("free inodes(8):",8-i)
#空闲data
    for j in range(16):
        if databitmap[j]=="0":
            break
    print("free blocks(16):",16-j)
    print("Files",Files)
    print("Directories",Directories)

    print("-------------")
    print("1.create")
    print("2.open")
    print("3.link")
    print("4.unlink")
    print("5.mkdir")
    print("-------------")
    #print("输入命令:")
    n=input("输入命令:")
    if n=="1":
        name = input("输入")
        Create(name)
    if n=="2":
        name = input("输入")
        Open(name[1:len(name)])
    if n=="3":
        name = input("输入")
        Link(name)
    if n=="4":
        name = input("输入")
        Unlink(name)
    if n=="5":
        name = input("输入")
        Mkdir(name[1:len(name)])

