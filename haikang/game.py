from haikang.Set import Set
from haikang.Set1 import Set1
from haikang.Set2 import Set2
import pygame
import sys
def show_window():
    pygame.init()
    window=Set()
    screen=pygame.display.set_mode((window.screen_width,window.screen_heigth),0,32)
    pygame.display.set_caption('射击游戏')
    # bg_img=pygame.image.load(window.bg_img)
    bg_color=window.bg_color
    zidan=Set1(screen)
    shouqiang=Set2(screen)
    while True:
        screen.fill(bg_color)  # 绘制屏幕颜色
        # zidan.show_img()
        shouqiang.show_img()
        # screen.blit(bg_img, (0, 200))
        zidan.updata_pos()
        shouqiang.update_pos()
        pygame.display.update()
        pygame.display.flip()
        for ev in pygame.event.get():
            if ev.type==pygame.QUIT:
                sys.exit()
            # elif ev.type == pygame.KEYDOWN:  # 按下键
            #     if ev.key == pygame.K_SPACE:  # 按空格键
            #         # ship.ship_rect.centerx+=10
            #         zidan.moving_right = True
            # elif ev.type == pygame.KEYUP:  # 按下键
            #     if ev.key == pygame.K_SPACE:  # 按空格键
            #         # ship.ship_rect.centerx+=10
            #         zidan.moving_right = False
            #         zidan.imgx = 170
            elif ev.type==pygame.KEYDOWN:#按下键
                if ev.key==pygame.K_RIGHT:#按右键
                    # ship.ship_rect.centerx+=10
                    shouqiang.moving_right=True
                if ev.key == pygame.K_LEFT:  # 按左键
                    # ship.ship_rect.centerx -= 10
                    shouqiang.moving_left = True
                if ev.key==pygame.K_UP:#按上键
                    # ship.ship_rect.centerx+=10
                    shouqiang.moving_top=True
                if ev.key == pygame.K_DOWN:  # 按下键
                    # ship.ship_rect.centerx -= 10
                    shouqiang.moving_bottom = True
            elif ev.type==pygame.KEYUP:#弹起键
                if ev.key==pygame.K_RIGHT:#按右键
                    shouqiang.moving_right = False
                if ev.key == pygame.K_LEFT:# 按左键
                    shouqiang.moving_left=False
                if ev.key==pygame.K_UP:#按上键
                    # ship.ship_rect.centerx+=10
                    shouqiang.moving_top=False
                if ev.key == pygame.K_DOWN:  # 按下键
                    # ship.ship_rect.centerx -= 10
                    shouqiang.moving_bottom = False
                if ev.key == pygame.K_SPACE:  # 按空格键
                    # ship.ship_rect.centerx+=10
                    zidan.moving_right = True



show_window()