#pygame制作简单的游戏界面
import pygame
import sys
from haikang.four1_Setting import Setting
# from haikang.hw_five_Ship import Ship
from haikang.four2_Ship import Ship
from haikang.Monster import Monster
from haikang.seven_game_state import Game_state
import haikang.hw_five_Game_Function as gf  #as起别名
from pygame.sprite import Group
def show_window():
    pygame.init()#初始化窗口参数
    window_setting=Setting()#创建窗口参数设置的对象
    screen=pygame.display.set_mode((window_setting.screen_width,window_setting.screen_height))#窗口尺寸
    pygame.display.set_caption("这是我的游戏")#设置窗口标题

    ship=Ship(screen)#创建飞机
    bulletGroup=Group()#创建子弹编组
    # monster = Monster(screen)  # 创建怪物

    # 创建一个怪物
    # monster = Monster(screen)
    # 创建一行怪物
    monsterGroup = Group()

    # 创建外星人
    gf.create_monster(window_setting, screen, ship, monsterGroup)

    # 统计游戏状态信息
    state=Game_state(window_setting)

   # 窗口主循环
    while True:
        gf.check_event(screen, ship, bulletGroup)  # 监视事件
        if state.game_active:
            ship.update_pos()  # 更新飞机位置
            ship.show_ship()  # 显示飞机
            # 更新怪物
            gf.update_monster(window_setting, screen, bulletGroup, monsterGroup, ship, state)
            #更新子弹
            gf.update_bullets(window_setting, screen, ship, bulletGroup, monsterGroup)
            # 显示怪物
            monsterGroup.draw(screen)
            gf.update_screen(screen,window_setting,ship,bulletGroup,monsterGroup,state)#绘制和更新屏幕
        else:
            print('game over')

show_window()

