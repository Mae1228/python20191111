#元组:元素不能通过赋值修改，元组不能改变
tt=('aa','bb','cc')
#长度len()
print(len(tt),type(tt))
#获取下标为1的元素
print(tt[1])
#tt[1]='hello'元组不可重复赋值
# tt.append('hello') 不可以添加元素试图修改
for i in tt:
    print(i)

