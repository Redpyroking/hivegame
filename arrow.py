import pygame
import math
class Arrow:

    def __init__(self,x,y) -> None:
        self.position = (x,y)
        self.x = x
        self.y = y
        self.scale = (20,20)
        self.rotation = 0
        self.image = pygame.image.load('E:/github_projects/mazeGame/assest/arrow.png')
        self.image = pygame.transform.scale(self.image,self.scale)
        self.sprite = self.image
        self.offset = [5,-15]
    
    def follow(self,object)->None:
        self.x = object.x+self.offset[0]
        self.y = object.y+self.offset[1]
    
    def rotate_around(self,object):
        mouse_pos = pygame.mouse.get_pos()
        x_dis = mouse_pos[0] - self.x
        y_dis = mouse_pos[1] - self.y
        angle = (180 / math.pi) * -math.atan2(y_dis, x_dis)
        self.rotation += 1
        self.image = pygame.transform.rotate(self.image,int(angle))
        self.rect = self.image.get_rect(center=self.position)

    def draw(self,window):
        window.blit(self.image,(self.x,self.y))