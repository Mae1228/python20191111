#pygame制作简单的游戏界面
import pygame
from haikang.four1_Setting import Setting
import haikang.hw_six_Rain_Function as gf  #as起别名
from pygame.sprite import Group
def show_window():
    pygame.init()#初始化窗口参数
    window_setting=Setting()#创建窗口参数设置的对象
    screen=pygame.display.set_mode((window_setting.screen_width,window_setting.screen_height))#窗口尺寸
    pygame.display.set_caption("这是我的游戏")#设置窗口标题

    # 创建一行怪物
    rainGroup = Group()

    # 创建外星人
    gf.create_rain(window_setting, screen,rainGroup)

   # 窗口主循环
    while True:
        gf.update_screen(screen,window_setting,rainGroup)#绘制和更新屏幕

show_window()

