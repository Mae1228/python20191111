# 面向对象：抽象、封装、继承、多态
#类 class，类名用大写
# 类中：成员属性，成员方法
# 构造方法：创建对象时自动调用------封装，赋值
class Game():
    def __init__(self,name,score):
        self.name=name
        self.score=score

    def show_details(self):
        print(self.name,self.score)