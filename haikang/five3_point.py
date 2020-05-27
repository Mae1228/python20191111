#pygame中画图形：矩形，圆
# import pygame
# pygame.draw.rect(screen,(255,0,0),pygame.Rect(x,y,width,height))#界面，颜色，位置，rect对象，0填充1空白
# pygame.draw.circle(screen,(255,0,0),(x,y),直径,)#界面，颜色，位置，直径，0填充
#删除消失的子弹：屏幕中看不见的子弹
# group()  列表
# 列表删除 remove()
# 遍历列表 ，变化列表的长度：会出现越界异常
# for obj in group():
#     group.remove(obj)
# 知识点：python中提出了深度拷贝 ----副本 copy()，副本在操作完成结束可以替换源文件，
# for obj in group.copy():
#     group.remove(obj)