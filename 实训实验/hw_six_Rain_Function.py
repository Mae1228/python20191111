import pygame
import sys
from haikang.hw_six_Rain import Rain
from haikang.four1_Setting import Setting
#游戏操作：1.监视事件2.绘制与更新屏幕
#1.监视事件

# 2.绘制和更新屏幕
def update_screen(screen, window_setting,rainGroup):
    bg_color = window_setting.bg_color
    # bg_img = pygame.image.load(window_setting.bg_img)

    screen.fill(bg_color)# 绘制屏幕颜色

    # 更新怪物
    update_rain(rainGroup)
    # 显示怪物
    rainGroup.draw(screen)
    pygame.display.flip()# 显示屏幕
    for ev in pygame.event.get():
        if (ev.type == pygame.QUIT):
            sys.exit()

#创建多行外星人
def create_rain(window_setting,screen,rainGroup):
    # 显示怪物
    rain = Rain(screen)

    rain_num_width = (window_setting.screen_width - 2 * rain.rect.width) / (2 * rain.rect.width)
    for r in range(int(rain_num_width)):
        rain = Rain(screen)

        # 赋值每一个外星人的具体位置使之不互相覆盖
        rain.x = rain.rect.width + r * 2 * rain.rect.width
        rain.rect.x = rain.x

        # 添加到编组中
        rainGroup.add(rain)

# 更新位置
def update_rain(rainGroup):
    check_rain_edge(rainGroup)
    rainGroup.update()

# 改变怪物方向：只要有一个怪物碰撞屏幕边缘，所有外星人都要改变方向
def check_rain_edge(rainGroup):
    # 遍历怪物
    for rain in rainGroup.sprites():
        if rain.check_screen_edge():
            # for rain2 in rainGroup.sprites():
            #     rain2.y=0
            #     rain2.rect.y=rain2.y
            # break
            rainGroup.remove(rain)
        else:
            if rainGroup==0:
                create_rain(rainGroup)
                print('3',rainGroup)
            else:
                rainGroup.update

'''
练习：找一个雨滴的图片，屏幕上创建一系列雨滴，雨滴往下落，到达屏幕底端消失，
消失后，屏幕顶端再次出现一行雨滴，实现连绵降雨的效果
#对象消失 remove()  kill()
'''