import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """创建一个外星人类"""

    def __init__(self, set, screen):
        """始化外星人并设置起始位置"""
        super(Alien, self).__init__()
        self.screen = screen
        self.set = set

        #加载图片，并设置rect属性
        self.image = pygame.image.load('img/alien.bmp')
        self.rect = self.image.get_rect()

        #外星人位置为左上角，left=x,top=y
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        #浮点化，便于运算
        self.x = float(self.rect.x)

    def check_edges(self):
        """检查外星人是否到达屏幕边缘"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True

    def update(self):
        """左右移动外星人"""
        self.x += (self.set.alien_speed *self.set.fleet_direction)
        self.rect.x = self.x

    def blitme(self):
        """制定位置绘制外星人，两个参数，绘制的图片Surface、画的位置dest"""
        self.screen.blit(self.image, self.rect)
