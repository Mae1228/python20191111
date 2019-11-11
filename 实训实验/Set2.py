import pygame
class Set2():
    def __init__(self,screen):
        self.screen=screen
        self.img1 = pygame.image.load('img/手枪.gif')
        self.img =pygame.image.load ('img/子弹.jpg')
        self.screen_rect=self.screen.get_rect()
        self.img1_rect=self.img.get_rect()
        self.img_rect = self.img.get_rect()
        # self.img_rect.centerx=self.screem_rect.centerx
        self.moving_right = False
        self.moving_left = False
        self.moving_top = False
        self.moving_bottom = False

    def show_img(self):
        self.screen.blit(self.img,self.img_rect)
        self.screen.blit(self.img1,self.img1_rect)

    def update_pos(self):
        if self.moving_right and self.img1_rect.right < self.screen_rect.right:
            self.img1_rect.centerx += 1
            self.img_rect.centerx += 1
        elif self.moving_left and self.img1_rect.left > 0:
            self.img1_rect.centerx -= 1
            self.img_rect.centerx -= 1
        elif self.moving_top and self.img1_rect.top > 0:
            self.img1_rect.centery -= 1
            self.img_rect.centery -= 1
        elif self.moving_bottom and self.img1_rect.bottom < self.screen_rect.bottom:
            self.img1_rect.centery += 1
            self.img_rect.centery += 1