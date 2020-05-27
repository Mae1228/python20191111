'''
#在1200*400的窗口中，背景色为（246,252,251）显示满屏的星星
#扩展：为了使星星分布更逼真，可以随机放置星星
'''

import pygame
from haikang.hw_six_Set import Setting
from haikang.hw_six_Star import Star
import haikang.hw_six_Game_Function as gf  #as起别名
from pygame.sprite import Group
def show_window():
    pygame.init()#初始化窗口参数
    window_setting=Setting()#创建窗口参数设置的对象
    screen=pygame.display.set_mode((window_setting.screen_width,window_setting.screen_height))#窗口尺寸
    pygame.display.set_caption("漫天星星")#设置窗口标题


    starGroup = Group()

   # 窗口主循环
    while True:
        gf.update_screen(screen,window_setting,starGroup)#绘制和更新屏幕

show_window()

