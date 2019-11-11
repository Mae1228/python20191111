from haikang.three3 import Computer
name=input('input cumputer name')
style=input('input computer style')
system=input('input computer system')
cpu=input('input computer cpu')
yingpan=input('input computer yinpan')

c=Computer(name,style,system,cpu,yingpan)
# c.show()
while True:
    f=input('是否关机Y')
    if f=='Y' or f=='y':
        c.cancle()
        break

    if f=='N' or f=='n':
        c.begin()
        c.show()