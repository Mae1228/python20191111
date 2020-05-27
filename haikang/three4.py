#!/usr/bin/env python
background_image_filename='star.jpg'
mouse_image_filename='three_副本.jpg'
import pygame
from pygame.locals import *
from sys import exit
pygame.init()#初始化
screen=pygame.display.set_mode((1200,724),0,32)#设置屏幕窗口的尺寸
pygame.display.set_caption('Hello,world!')#屏幕标题的内容
background=pygame.image.load(background_image_filename).convert()#窗口的背景图
mouse_cursor=pygame.image.load(mouse_image_filename).convert_alpha()
while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            exit()
    screen.blit(background,(0,0))
    x,y=pygame.mouse.get_pos()
    x-=mouse_cursor.get_width()/2
    y-=mouse_cursor.get_height()/2
    screen.blit(mouse_cursor,(x,y))
    pygame.display.update()