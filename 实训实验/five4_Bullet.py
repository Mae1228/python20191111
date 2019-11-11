import pygame
from pygame.sprite import Sprite
class Bullet(Sprite):
    # 屏幕中子弹个数，使用编组的方式Goup()，相当于列表，要操作编组中的元素通常使用精灵sprite
    def __init__(self,screen,ship):
        super(Bullet,self).__init__()#初始化父类的成员
        self.screen=screen
        # 绘制子弹，子弹位置，颜色，尺寸（宽，高）
        self.color=255,0,0
        self.rect=pygame.Rect(0,0,5,10)
        # 设置位置：在飞船中上方
        self.rect.centerx=ship.ship_rect.centerx
        self.rect.top = ship.ship_rect.top
        # 子弹当前位置
        self.y=float(self.rect.y)

     # 显示子弹
    def show_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect, 0)

    # 移动子弹：向上移动
    def bullet_move(self):
        self.y-=1
        self.rect.y=self.y

    # 删除子弹
    def delete_Bullet(self,bulletGroup):
        for obj in bulletGroup.copy():
            # 判断子弹不在屏幕中：子弹底部=屏幕上部0
            if obj.rect.bottom <=0:
                bulletGroup.remove(obj)
        # print('子弹个数：', len(bulletGroup))
