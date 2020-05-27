import pygame
import sys
from haikang.five4_Bullet import Bullet
#游戏操作：1.监视事件2.绘制与更新屏幕
#1.监视事件
def check_event(screen,ship,bulletGroup):
    # 监视事件（退出）
    for ev in pygame.event.get():
        if (ev.type == pygame.QUIT):
            sys.exit()
        elif ev.type == pygame.KEYDOWN:  # 按下键
            if ev.key == pygame.K_RIGHT:  # 按右键
                ship.moving_right = True
            if ev.key == pygame.K_LEFT:  # 按左键
                ship.moving_left = True
            if ev.key == pygame.K_UP:  # 按上键
                ship.moving_top = True
            if ev.key == pygame.K_DOWN:  # 按下键
                ship.moving_bottom = True
            if ev.key==pygame.K_SPACE:
                bullet=Bullet(screen,ship)
                bulletGroup.add(bullet)
        elif ev.type == pygame.KEYUP:  # 弹起键
            if ev.key == pygame.K_RIGHT:  # 按右键
                ship.moving_right = False
            if ev.key == pygame.K_LEFT:  # 按左键
                ship.moving_left = False
            if ev.key == pygame.K_UP:  # 按上键
                ship.moving_top = False
            if ev.key == pygame.K_DOWN:  # 按下键
                ship.moving_bottom = False


# 2.绘制和更新屏幕
def update_screen(screen, window_setting, ship,bulletGroup):
    bg_color = window_setting.bg_color
    bg_img = pygame.image.load(window_setting.bg_img)

    screen.fill(bg_color)# 绘制屏幕颜色
    screen.blit(bg_img, (0, 0))# 填充背景
    # print(pygame.font.get_fonts())

    pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(200,50, 100, 150),1)#在屏幕（200，50）处画大小为（100，150）的图形
    pygame.draw.circle(screen,(0, 255, 0),(400,80),10,0)#在屏幕（400，80）处画直径为10的圆

    # txt = pygame.font.Font("font/daiyu.ttf", 30)# 创建字体对象
    # txt_fm = txt.render(u"hello你好。。", 1, (255, 0, 0))# 渲染文字对象  # u指的是本地字符集utf-8
    # screen.blit(txt_fm,(100,200))# 显示文字并设置在屏幕的坐标的(100,200)处
    # screen.blit(txt_fm, (window_setting.screen_width / 2, window_setting.screen_height / 2))# 显示在屏幕中间

    ship.update_pos()# 更新飞机位置

    ship.show_ship()# 显示飞机
    # ship.show_bullet()#显示子弹

    count = 0

    # 显示子弹
    for bullet in bulletGroup:
        count += 1
        bullet.bullet_move()
        bullet.show_bullet()
    # 删除消失的子弹
    Bullet(screen,ship).delete_Bullet(bulletGroup)

    txt = pygame.font.Font('font/daiyu.ttf', 30)
    bullet_count = txt.render(u"子弹数量：" + str(count), 1, (255, 0, 0))  # x渲染文字对象     3：颜色 u:本地字符集utf_8
    screen.blit(bullet_count, (window_setting.screen_width-200, 20))  # 显示文字并设置在屏幕的(100，200)处
    pygame.display.flip()# 显示屏幕