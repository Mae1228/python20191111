#pygame制作简单的游戏界面
import pygame
import sys
def show_window():
    #初始化窗口参数
    pygame.init()
    screen=pygame.display.set_mode((1200,724))#窗口尺寸
    pygame.display.set_caption("这是我的游戏")#设置窗口标题
    bg_color=(188,222,255)#设置颜色
   # 窗口主循环
    while True:
        screen.fill(bg_color)#绘制屏幕颜色
        pygame.display.flip()#显示屏幕
        #监视事件（退出）
        for ev in pygame.event.get():
            if(ev.type==pygame.QUIT):
                sys.exit()

show_window()
