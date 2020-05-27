import pygame

class Ship():

    def __init__(self, set, screen):
        self.set = set
        self.screen = screen
        #导入图片，获取图片所在矩形宽、高
        self.image = pygame.image.load('img/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        #设置飞船放在屏幕底部中央
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        #在飞船的属性centerx修改为浮点，便于小数运算
        self.center = float(self.rect.centerx)
        #移动标志
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def center_ship(self):
        """将飞船放在中央"""
        self.center = self.screen_rect.centerx

    #更新飞船坐标
    def update(self):

        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.set.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.set.ship_speed_factor
        if self.moving_up and self.rect.top>=0:
            self.rect.bottom-= self.set.ship_speed_factor
        if self.moving_down and self.rect.bottom<=self.screen_rect.bottom:
            self.rect.bottom += self.set.ship_speed_factor
        self.rect.centerx = self.center

    def blitme(self):
        #指定位置绘制飞船，两个参数，绘制的图片Surface、画的位置dest
        self.screen.blit(self.image,self.rect)
