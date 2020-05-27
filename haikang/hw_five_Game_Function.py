#作业：编写游戏，将飞船放在屏幕左侧，
# 允许上下移动但不能移到屏幕外面，
# 按空格键时圆形子弹从飞船头部发射向右穿行的子弹

import pygame
import sys
from haikang.hw_five_Bullet import Bullet
from haikang.Monster import Monster
from time import sleep
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
                if len(bulletGroup)<10:
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
def update_screen(screen, window_setting, ship,bulletGroup,monsterGroup,state):
    bg_color = window_setting.bg_color
    # bg_img = pygame.image.load(window_setting.bg_img)

    screen.fill(bg_color)# 绘制屏幕颜色
    # screen.blit(bg_img, (0, 0))# 填充背景
    # print(pygame.font.get_fonts())

    # pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(200,50, 100, 150),1)#在屏幕（200，50）处画大小为（100，150）的图形
    # pygame.draw.circle(screen,(0, 255, 0),(400,80),10,0)#在屏幕（400，80）处画直径为10的圆


    # 显示
    # for monster in monsterGroup:
    #     monster.show_monster()


    pygame.display.flip()# 显示屏幕

# 更新子弹
def update_bullets(window_setting,screen,ship,bulletGroup,monsterGroup):
    count = 0

    # 显示子弹
    for bullet in bulletGroup:
        count += 1
        bullet.bullet_move()
        bullet.show_bullet()

    # 删除消失的子弹
    Bullet(screen, ship).delete_Bullet(bulletGroup)

    txt = pygame.font.Font('font/daiyu.ttf', 30)
    bullet_count = txt.render(u"子弹数量：" + str(count), 1, (255, 0, 0))  # x渲染文字对象     3：颜色 u:本地字符集utf_8
    screen.blit(bullet_count, (window_setting.screen_width - 200, 20))  # 显示文字并设置在屏幕的(100，200)处
    # 检测怪物与子弹碰撞
    collisions = pygame.sprite.groupcollide(bulletGroup, monsterGroup, True,True)  # 返回值时一个字典（存放一组碰撞元素的键值对，第一个True代表子弹消失，第二个True代表怪物消失）
    # 生成新的怪物
    if len(monsterGroup) == 0:
        bulletGroup.empty()  # 清空子弹
        create_monster(window_setting, screen, ship, monsterGroup)  # 创建怪物


#创建多行外星人
def create_monster(window_setting,screen,ship,monsterGroup):
    # 显示怪物
    m1 = Monster(screen)

    monster_num_width = (window_setting.screen_width - 2 * m1.rect.width-ship.rect.width) / (2 * m1.rect.width)
    monster_num_height = (window_setting.screen_height - 2 * m1.rect.height) / (2 * m1.rect.height)
    for m in range(int(monster_num_width)):
        for m1 in range(int(monster_num_height)):
            monster = Monster(screen)

            # 赋值每一个外星人的具体位置使之不互相覆盖
            monster.x = monster.rect.width + m * 2 * monster.rect.width
            monster.rect.x = monster.x
            monster.y = monster.rect.height + m1 * 2 * monster.rect.height
            monster.rect.y = monster.y

            # 添加到编组中
            monsterGroup.add(monster)



# 更新怪物的位置
def update_monster(window_setting, screen,bulletGroup,monsterGroup,ship,state):
    check_monster_edge(monsterGroup)
    monsterGroup.update()
    # 检测怪物与飞船碰撞spritecollideany(sprite)返回值group中的第一个碰撞到sprite元素
    if pygame.sprite.spritecollideany(ship,monsterGroup):
        print('碰撞了')
        hitwork(window_setting, screen, ship, bulletGroup, monsterGroup, state)
    # 怪物碰撞屏幕底部
        check_monsters_bottom(window_setting, screen, bulletGroup, monsterGroup, ship, state)

# 改变怪物方向：只要有一个怪物碰撞屏幕边缘，所有外星人都要改变方向
def check_monster_edge(monsterGroup):
    # 遍历怪物
    for monster in monsterGroup.sprites():
        if monster.check_screen_edge():
            for monster2 in monsterGroup.sprites():
                monster2.y+=10
                monster2.rect.y=monster2.y
                monster2.direct*=-1
            break



# 飞船与怪物碰撞之后的动作
def hitwork(window_setting, screen, ship,bulletGroup, monsterGroup,state):
    if state.ship_left>=0:
        state.ship_left -= 1
        # 清空怪物与子弹
        monsterGroup.empty()
        bulletGroup.empty()
        # 创建怪物与飞船，并且把飞船放在屏幕的底边
        create_monster(window_setting, screen, ship, monsterGroup)
        ship.center_ship()
        # 线程暂停0.5秒
        sleep(0.5)
    else:
        state.game_active=False




# 检测怪物到达屏幕底端
def check_monsters_bottom(window_setting, screen, bulletGroup, monsterGroup,ship, state):
    screen_rect=screen.get_rect()
    for monster in monsterGroup.sprites():
        if monster.rect.bottom>=screen_rect.bottom:
            hitwork(window_setting, screen, ship, bulletGroup, monsterGroup, state)
            break

'''
练习：找一个雨滴的图片，屏幕上创建一系列雨滴，雨滴往下落，到达屏幕底端消失，
消失后，屏幕顶端再次出现一行雨滴，实现连绵降雨的效果
#对象消失 remove()  kill()
'''