#pygame制作简单的游戏界面
import pygame
import sys
from haikang.four1_Setting import Setting
from haikang.four2_Ship import Ship
def show_window():
    pygame.init()#初始化窗口参数
    window_setting=Setting()# 创建窗口参数是指的对象
    screen=pygame.display.set_mode((window_setting.screen_width,window_setting.screen_height),0,32)#窗口尺寸
    pygame.display.set_caption("游戏_1")#设置窗口标题
    bg_color=window_setting.bg_color#设置颜色
    bg_img=pygame.image.load(window_setting.bg_img)#设置背景图片
    ship=Ship(screen)#创建飞机
    txt = pygame.font.Font('font/daiyu.ttf', 30)
    txt_fm = txt.render(u'hello你好。。', 1, (255, 0, 0))  # x渲染文字对象     3：颜色 u:本地字符集utf_8
   # 窗口主循环
    while True:
        #监视事件（退出）
        for ev in pygame.event.get():
            if(ev.type==pygame.QUIT):
                sys.exit()
            elif ev.type==pygame.KEYDOWN:#按下键
                if ev.key==pygame.K_RIGHT:#按右键
                    # ship.ship_rect.centerx+=10
                    ship.moving_right=True
                if ev.key == pygame.K_LEFT:  # 按左键
                    # ship.ship_rect.centerx -= 10
                    ship.moving_left = True
                if ev.key==pygame.K_UP:#按上键
                    # ship.ship_rect.centerx+=10
                    ship.moving_top=True
                if ev.key == pygame.K_DOWN:  # 按下键
                    # ship.ship_rect.centerx -= 10
                    ship.moving_bottom = True
            elif ev.type==pygame.KEYUP:#弹起键
                if ev.key==pygame.K_RIGHT:#按右键
                    ship.moving_right = False
                if ev.key == pygame.K_LEFT:# 按左键
                    ship.moving_left=False
                if ev.key==pygame.K_UP:#按上键
                    # ship.ship_rect.centerx+=10
                    ship.moving_top=False
                if ev.key == pygame.K_DOWN:  # 按下键
                    # ship.ship_rect.centerx -= 10
                    ship.moving_bottom = False
        screen.fill(bg_color)  # 绘制屏幕颜色
        ship.update_pos()#更新飞机位置
        screen.blit(bg_img, (0, 0))  # 填充背景
        screen.blit(txt_fm, (100, 200))  # 显示文字并设置在屏幕的(100，200)处
        ship.show_ship()  # 显示飞机
        pygame.display.flip()  # 显示屏幕

show_window()

