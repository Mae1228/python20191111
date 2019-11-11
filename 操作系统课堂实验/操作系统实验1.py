import random
import copy
a = [[random.randint(0, 1) for j in range(1, 9)] for i in range(1, 9)]
a1 = copy.deepcopy(a)

def menu():
	print("|---------菜单--------|")
	print("1.创建进程")#创建线程
	print("2.时间片")#时间片
	print("3.阻塞")#阻塞
	print("4.唤醒")#唤醒
	print("5.显示")#显示
	print("6.结束进程")#结束进程
	print("|---------------------|")

'''CREATE LIST'''
running=[]#列表
ready=[]
blocked=[]
#创建线程
def one():
	name=input("请输入进程的名字: ")
	if running:
		ready.append(name)
	else:
		running.append(name)
		size = int(input('请输入进程的内存大小：'))
		s = size // 1024
		if size % 1024 == 0:
			s += 0
		else:
			s += 1
		sun = []
		print('未填1的位示图：', a)
		for i in range(len(a)):
			for j in range(len(a)):
				if a[i][j] == 0:
					if s != 0:
						s -= 1
						a[i][j] = 1
						sun1 = i * 8 + j
						sun.append(sun1)
		print('页表：', sun)
		print('位示图：', a)
		s = size // 1024
		if size % 1024 == 0:
			print('内存块数：', s)
		else:
			s += 1
			print('内存块数：', s)
		var = input("请输入十六进制的逻辑地址：")
		b = oct(int(var, 16))
		w = int(b[2:])
		if w <= size:
			print('十进制的逻辑地址：', w)
			w0 = w // 1024
			print('页号：', w0)
			w1 = w % 1024
			print('页内偏移地址：', w1)
			w2 = sun[w0]
			print('物理块号：', w2)
			w3 = w2 * 1024 + w1
			print('物理地址：', w3)
		else:
			print('输入错误')
	print()
	main()
#时间片到
def two():
	if running:
		ready.append(running[0])
		del running[0]
		running.append(ready[0])
		del ready[0]
	else:
		menu()
#阻塞
def three():
	if running:
		blocked.append(running[0])
		del running[0]
		running.append(ready[0])
		del ready[0]
	else:
		menu()
#唤醒
def four():
	if running:
		ready.append(blocked[0])
		del blocked[0]
	else:
		menu()
#结束进程
def six():
	if running:
		for i in range(len(a)):
			for j in range(len(a)):
				if a[i][j] != a1[i][j]:
					a[i][j] = a1[i][j]
		print('位示图反向回填“0”：', a)
		print()
		main()
		del running[0]
		running.append(ready[0])
		del ready[0]
	else:
		menu()
#显示
def five():
	print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<*")
	print("Running:")
	print(running)
	print("Ready:")
	print(ready)
	print("Blocked:")
	print(blocked)
	print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>*")
		
def main():
	while True:
		menu()
		a=eval(input("请输入要执行的序号: "))
		if a==1:
			one()
		elif a==2:
			two()
		elif a==3:
			three()
		elif a==4:
			four()
		elif a==5:
			five()
		elif a==6:
			six()
		else:
			exit()
main()
		

