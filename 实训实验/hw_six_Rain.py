import pygame
from pygame.sprite import Sprite

class Rain(Sprite):
    """设置怪物属性：图片，位置，移动的当前位置"""
    def __init__(self,screen):
        super(Rain,self).__init__()      # 初始化父类成员
        self.screen = screen
        self.image = pygame.image.load("img/rain.png")
        self.rect = self.image.get_rect()

        # 设置初始位置
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # 用于改变怪物的位置
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    # 显示怪物
    def show_rain(self):
        self.screen.blit(self.image,self.rect)

    # 移动：屏幕边缘检测做哟屏幕检测，改变移动方向direct -1左方向 direct*x 1右方向+x direct*x
    def update(self):
        # 检测是否触碰屏幕右侧
        self.y += 0.1
        self.rect.y = self.y

    # 屏幕检测：True碰撞，False为抵达屏幕边缘
    def check_screen_edge(self):
        if self.rect.bottom >= self.screen.get_rect().bottom:#抵达屏幕右侧
            return True
        else:
            return False

