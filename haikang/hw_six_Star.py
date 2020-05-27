import pygame
from pygame.sprite import Sprite

class Star(Sprite):
    """设置怪物属性：图片，位置，移动的当前位置"""
    def __init__(self,screen):
        super(Star,self).__init__()      # 初始化父类成员
        self.screen = screen
        self.image = pygame.image.load("img/star.png")
        self.rect = self.image.get_rect()

        # 设置初始位置
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # 用于改变怪物的位置
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def show_star(self):
        self.screen.blit(self.image,self.rect)

