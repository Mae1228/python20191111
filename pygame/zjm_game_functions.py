import sys
from time import sleep
import pygame
from zjm_bullet import Bullet
from zjm_alien import Alien

def check_keydown_events(event, set, screen, ship, bullets):
    """响应按键"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_UP:  # 按上键
        ship.moving_up = True
    elif event.key == pygame.K_DOWN:  # 按下键
        ship.moving_down = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(set, screen, ship, bullets)
    elif event.key == pygame.K_q:
        sys.exit()

def check_keyup_events(event, ship):
    """响应按键松开"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False
    elif event.key == pygame.K_UP:  # 按上键
        ship.moving_up = False
    elif event.key == pygame.K_DOWN:  # 按下键
        ship.moving_down = False

def check_events(set, screen, ship, bullets):
    """响应键盘、鼠标事件"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, set, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)


def fire_bullet(set, screen, ship, bullets):
    """没有超过限制就创建一个子弹，并且加入子弹组"""
    if len(bullets) < set.bullets_allowed:
        new_bullet = Bullet(set, screen, ship)
        bullets.add(new_bullet)

def update_screen(set, screen, ship, aliens, bullets,stats):
    """更新屏幕图像，显示新的图像"""
    # 每次循环时重新绘制屏幕
    screen.fill(set.bg_color)

    #画出所有子弹，在飞船、外星人的后面
    count=0
    for bullet in bullets.sprites():
        bullet.draw_bullet()
        count+=1
    ship.blitme()
    aliens.draw(screen)
    """屏幕显示游戏信息"""
    txt = pygame.font.Font("font/daiyu.ttf", 20)
    bullet_count = txt.render(u"子弹数量：" + str(count), 1, (155, 155, 155))
    screen.blit(bullet_count, (40, 30))

    ship_count = txt.render(u"飞船命数：" + str(stats.ships_left), 1, (155, 155, 155))
    screen.blit(ship_count, (40, 50))

    alien_count = txt.render(u"得分(射杀外星人的个数)：" + str(stats.count), 1, (155, 155, 155))
    screen.blit(alien_count, (40, 70))

    #让最近的绘制可见
    pygame.display.flip()

def update_bullets(set, screen, ship, aliens, bullets,stats):
    #更新子弹
    bullets.update()
    #删除消失的子弹
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

    check_bullet_alien_collisions(set, screen, ship, aliens, bullets,stats)

def check_bullet_alien_collisions(set, screen, ship, aliens, bullets,stats):
    """检查子弹外是否击中外星人"""
    #删除相遇的子弹，外星人
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
    if collisions:
        stats.count += 1
    if len(aliens) == 0:
        #删除现有子弹，创建新的一群外星人
        bullets.empty()
        create_fleet(set, screen, ship, aliens)

def check_fleet_edges(set, aliens):
    """有外星人到达边缘后，改变方向"""
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(set, aliens)
            break

def change_fleet_direction(set, aliens):
    """将外星人下移，并且改变运动方向"""
    for alien in aliens.sprites():
        alien.rect.y += set.fleet_speed
    set.fleet_direction *= -1


def ship_hit(set, stats, screen, ship, aliens, bullets):
    """响应飞船被撞到"""
    if stats.ships_left > 0:
        #生命值减去1
        stats.ships_left -= 1
    else:
        stats.game_active = False
        print("Game Over")
    #清空子弹、外星人
    aliens.empty()
    bullets.empty()
    #新建一群外星人、将飞船放在中央
    create_fleet(set, screen, ship, aliens)
    ship.center_ship()
    #暂停一下
    sleep(0.5)

def check_aliens_bottom(set, stats, screen, ship, aliens, bullets):
    """检查是否有外星人到达了屏幕底端"""
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            #想飞船相撞一样处理
            ship_hit(set, stats, screen, ship, aliens, bullets)
            break

def update_aliens(set, stats, screen, ship, aliens, bullets):
    """检查是否到达屏幕两边"""
    check_fleet_edges(set, aliens)
    aliens.update()
    # 检测外星人和飞船碰撞
    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(set, stats, screen, ship, aliens, bullets)
    # 检查是否有外星人到达屏幕底端
    check_aliens_bottom(set, stats, screen, ship, aliens, bullets)

def get_number_aliens_x(set, alien_width):
    """计算一行能有多少外星人"""
    available_space_x = set.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x

def get_number_rows(set, ship_height, alien_height):
    """计算有几行外星人"""
    available_space_y = (set.screen_height -(3 * alien_height) - ship_height)
    number_rows = int(available_space_y / (2 * alien_height))
    return number_rows

def create_alien(set, screen, aliens, alien_number, row_number):
    """创建外星人"""
    alien = Alien(set, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)

def create_fleet(set, screen, ship, aliens):
    """创建外星人群"""
    #导入参数，获取一行几个，有几行
    alien = Alien(set, screen)
    number_aliens_x = get_number_aliens_x(set, alien.rect.width)
    number_rows = get_number_rows(set, ship.rect.height, alien.rect.height)
    #创建外星人
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            create_alien(set, screen, aliens, alien_number,row_number)
