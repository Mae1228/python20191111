import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):

    def __init__(self, set, screen, ship):
        """创建一个管理子弹的类"""
        super().__init__()
        self.screen = screen

        #在（0,0）位置画矩形子弹，然后设置子弹位置
        self.rect = pygame.Rect(0, 0, set.bullet_width,set.bullet_height)
        #X坐标等于飞船X中间，Y坐标等于飞船top的Y坐标
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        #小数化Y坐标，便于移动运算
        self.y = float(self.rect.y)
        #子弹颜色、速度
        self.color = set.bullet_color
        self.speed_factor = set.bullet_speed_factor

    def update(self):
        """向上移动子弹"""
        # 更新子弹Y坐标.
        self.y -= self.speed_factor
        self.rect.y = self.y

    def draw_bullet(self):
        """将子弹画在屏幕上"""
        pygame.draw.rect(self.screen, self.color, self.rect)
