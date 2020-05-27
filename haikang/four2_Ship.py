import pygame
class Ship():
    # 设置飞机在屏幕位置
    def __init__(self,screen):
        self.screen=screen
        self.img=pygame.image.load('img/ship.bmp')
        self.img_star=pygame.image.load('img/three_副本.jpg')
        #pygame认为每一个元素都是一个矩形
        self.rect=self.img.get_rect()#获取图片矩形对象
        self.screen_rect=self.screen.get_rect()#获取屏幕矩形对象
        #定位：屏幕底部中央处
        # self.ship_rect.bottom=self.screen_rect.bottom#水平和底部不写y
        # self.ship_rect.centerx=self.screen_rect.centerx#在x轴上左右移动
        self.rect.bottom = self.screen_rect.bottom  # 水平和底部不写y
        self.rect.centerx = self.screen_rect.centerx  # 在y轴上左右移动

        self.star_rect=self.img.get_rect()
        self.star_rect.top = self.screen_rect.top
        self.star_rect.right=self.screen_rect.right-160
        # 设置一个标志控制连续移动
        self.moving_right = False
        self.moving_left = False
        self.moving_top=False
        self.moving_bottom=False

    def show_ship(self):
        self.screen.blit(self.img,self.rect)
        self.screen.blit(self.img_star,self.star_rect)


    #更新飞机位置
    def update_pos(self):
        if self.moving_right and self.rect.right<self.screen_rect.right:
            self.rect.centerx += 1
        elif self.moving_left and self.rect.left>0:
            self.rect.centerx -= 1
        elif self.moving_top and self.rect.top>0:
            self.rect.centery -= 1
        elif self.moving_bottom and self.rect.bottom<self.screen_rect.bottom:
            self.rect.centery += 1


    #定位飞船位置---屏幕中央处
    def center_ship(self):
        # self.rect.bottom = self.screen_rect.bottom  # 水平和底部不写y
        # self.rect.centerx = self.screen_rect.centerx  # 在y轴上左右移动
        self.center=self.screen_rect.centerx
