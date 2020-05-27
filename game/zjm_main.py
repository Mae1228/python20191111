import pygame
from pygame.sprite import Group

from game.zjm_settings import Settings
from game.zjm_game_stats import GameStats
from game.zjm_ship import Ship
import game.zjm_game_functions as gf

def run_game():
    #初始化pygame、设置屏幕对象
    pygame.init()
    set = Settings()
    #初始化屏幕大小参数
    screen = pygame.display.set_mode((set.screen_width, set.screen_height))
    #设置标题
    pygame.display.set_caption("大战外星人")

    stats = GameStats(set)

    #设置背景颜色
    bg_color = (230,230,230)
    screen.fill(bg_color)
    #画飞船
    ship = Ship(set,screen)
    #创建子弹组
    bullets = Group()
    aliens = Group()
    #创建外星人群
    gf.create_fleet(set, screen, ship, aliens)

    #游戏主循环
    while True:
        #监视键盘鼠标事件
        gf.check_events(set, screen, ship, bullets)

        if stats.game_active:
            ship.update()
            gf.update_bullets(set, screen, ship, aliens, bullets,stats)
            gf.update_aliens(set, stats, screen, ship, aliens, bullets)

        gf.update_screen(set, screen, ship, aliens, bullets,stats)

run_game()