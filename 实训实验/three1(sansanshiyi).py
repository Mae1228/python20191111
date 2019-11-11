# 函数 def 作用：提高代码复用性，
# 函数种类：无参无返回值，含参无返回值，无参有返回值，含参有返回值

# 无参无返回值
def juice_enter():
    print('一杯草莓果汁')
#     调用
juice_enter()
# 含参
def juice_enter(fruit):
    print('一杯'+fruit+'果汁')
juice_enter('苹果')
# 含多参
def juice_enter(f1,f2):
    print('一杯'+f1+' '+f2+'果汁')
juice_enter('香蕉','牛奶')

def juice_enter(fruit):
    str=''
    for i in fruit:
        str+=','+i
    print('一杯'+str+'果汁')
juice_enter(['苹果','香蕉','牛奶'])

def juice_enter(fruit):
    str = ''
    for i in fruit:
        str += ',' + i
    return str+'果汁'
res=juice_enter(['苹果','香蕉','牛奶'])
print('纸杯装着'+res)

# 练习：写一个函数用于铺地板，地板#
# 需求：多少行，多少列，
# 地板的样式：木制，瓷砖，还是别的
# 100*30#
##########
##########
# 打印图形
# 结算工资，一块#地板是1.5块钱，%地板2块钱，其他地板1块钱
stye = int(input('地板的样式 1：木制 2：瓷砖 3：其他样式'))
if stye==1:
    money=1.5
elif stye==2:
    money=2
else:
    money=1

# money = float(input('木制：1.5 瓷砖：2 其他样式 ：1'))
def jisuan(s):
    print(money)
    hang = int(input('请输入行数'))
    lie = int(input('请输入列数'))
    if stye == s:
        for i in range(hang):
            print("#"*lie)
    count = hang * lie * money
    print(count)
jisuan(stye)