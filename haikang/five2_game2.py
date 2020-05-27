#pygame制作简单的游戏界面
import pygame
import sys
from haikang.four1_Setting import Setting
from haikang.four2_Ship import Ship
import haikang.five1_Game_Function as gf  #as起别名
from pygame.sprite import Group
def show_window():
    pygame.init()#初始化窗口参数
    window_setting=Setting()#创建窗口参数设置的对象
    screen=pygame.display.set_mode((window_setting.screen_width,window_setting.screen_height))#窗口尺寸
    pygame.display.set_caption("这是我的游戏")#设置窗口标题

    ship=Ship(screen)#创建飞机
    bulletGroup=Group()#创建子弹编组

   # 窗口主循环
    while True:
        gf.check_event(screen,ship,bulletGroup)#监视事件
        gf.update_screen(screen,window_setting,ship,bulletGroup)#绘制和更新屏幕

show_window()

