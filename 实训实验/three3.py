class Computer():
    def __init__(self,name,style,system,cpu,yingpang):
        self.name=name
        self.style=style
        self.system=system
        self.cpu=cpu
        self.yingpan=yingpang

    def begin(self):
        print('电脑'+self.name+'正在开机')

    def show(self):
        print('电脑名为'+self.name,'类型为'+self.style,'系统为'+self.system,'cpu为'+self.cpu,'硬盘大小为'+self.yingpan+'正在编程')

    def cancle(self):
        print('电脑'+self.name+'正在关机')

