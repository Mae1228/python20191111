import pygame
from pygame.sprite import Sprite
class Bullet(Sprite):
    # 屏幕中子弹个数，使用编组的方式Goup()，相当于列表，要操作编组中的元素通常使用精灵sprite
    def __init__(self,screen,ship):
        super(Bullet,self).__init__()#初始化父类的成员
        self.screen=screen
        self.screen_rect = self.screen.get_rect()  # 获取屏幕矩形对象
        # 绘制子弹，子弹位置，颜色，尺寸（宽，高）
        self.color=0,255,0
        self.rect=self.rect=pygame.Rect(0,0,5,10)
        # 设置位置：在飞船中上方
        self.rect.centerx=ship.rect.centerx
        self.rect.top = ship.rect.top
        # 子弹当前位置
        self.y=float(self.rect.y)

     # 显示子弹
    def show_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect, 0)


    # 移动子弹：向右移动
    def bullet_move(self):
        self.y-=1
        self.rect.y=self.y

    # 删除子弹
    def delete_Bullet(self, bulletGroup):
        for obj in bulletGroup.copy():
            # 判断子弹不在屏幕中：子弹底部=屏幕上部0
            if obj.rect.top <=0:
                bulletGroup.remove(obj)

    # def show_bullet_count(self,bulletGroup):
    #     if len(bulletGroup)<=6:
    #          self.show_bullet()
    #     else:
    #         self.delete_Bullet(bulletGroup)