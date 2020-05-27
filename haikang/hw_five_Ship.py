import pygame
class Ship():
    # 设置飞机在屏幕位置
    def __init__(self,screen):
        self.screen=screen
        self.img=pygame.image.load('img/ship_副本.bmp')
        #pygame认为每一个元素都是一个矩形
        self.ship_rect=self.img.get_rect()#获取图片矩形对象
        self.screen_rect=self.screen.get_rect()#获取屏幕矩形对象
        #定位：屏幕底部中央处
        # self.ship_rect.bottom=self.screen_rect.bottom#水平和底部不写y
        # self.ship_rect.centerx=self.screen_rect.centerx#在x轴上左右移动
        self.ship_rect.left = self.screen_rect.left  # 水平和底部不写y
        self.ship_rect.centery=self.screen_rect.centery#在y轴上左右移动

        # 设置一个标志控制连续移动
        self.moving_right = False
        self.moving_left = False
        self.moving_top=False
        self.moving_bottom=False
    def show_ship(self):
        self.screen.blit(self.img,self.ship_rect)
        # self.screen.blit(self.img_star,self.star_rect)
    #更新飞机位置
    def update_pos(self):
        if self.moving_right and self.ship_rect.right<self.screen_rect.right:
            self.ship_rect.centerx += 1
        elif self.moving_left and self.ship_rect.left>0:
            self.ship_rect.centerx -= 1
        elif self.moving_top and self.ship_rect.top>0:
            self.ship_rect.centery -= 1
        elif self.moving_bottom and self.ship_rect.bottom<self.screen_rect.bottom:
            self.ship_rect.centery += 1