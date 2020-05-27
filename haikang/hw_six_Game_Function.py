import pygame
import sys
from haikang.hw_six_Star import Star
from haikang.hw_six_Set import Setting
#游戏操作：1.监视事件2.绘制与更新屏幕
#1.监视事件

# 2.绘制和更新屏幕
def update_screen(screen, window_setting,starGroup):
    bg_color = window_setting.bg_color
    screen.fill(bg_color)# 绘制屏幕颜色

    # 显示怪物
    star = Star(screen)
    star_num_max = (window_setting.screen_width - 2 * star.rect.width) / (2 * star.rect.width)
    star_num_maxy = (window_setting.screen_height - 2 * star.rect.height) / (2 * star.rect.height)#可容纳的行数
    for s1 in range(int(star_num_maxy)):
        for s in range(int(star_num_max)):
            star = Star(screen)

            # 赋值每一个外星人的具体位置使之不互相覆盖
            star.x = star.rect.width + s * 2 * star.rect.width
            star.rect.x = star.x
            star.y = star.rect.height + s1 * 2 * star.rect.height
            star.rect.y = star.y
            # # 显示
            # star.show_star()

            # 添加到编组中
            starGroup.add(star)

    for star in starGroup:
        star.show_star()

    pygame.display.flip()# 显示屏幕
    for ev in pygame.event.get():
        if (ev.type == pygame.QUIT):
            sys.exit()