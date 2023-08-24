import pygame
import math

class Enemy:
    def __init__(self,x,y) -> None:
        self.x = x
        self.y = y
        self.scale = (30,30)
        self.rotation = 0
        self.position = (x,y)
        self.image = pygame.image.load('E:/github_projects/mazeGame/assest/enemy.png')
        self.image = pygame.transform.scale(self.image,self.scale)
        self.sprite = self.image
        self.direction = "right"
        self.speed = 5
        self.isDeleted = False
        self.rect = self.image.get_rect(center=self.position)

    def rotate(self,sprite,angle)->None:#Degree
        self.rotation = angle
        self.image = pygame.transform.rotate(sprite,self.rotation)
    
    def rotate_around(self,object):
        x_dis = object.x - self.x
        y_dis = object.y - self.y
        angle = ((180 / math.pi) * -math.atan2(y_dis, x_dis)) - 90
        self.rotate(self.sprite,int(angle))
        self.rect = self.image.get_rect(center=(self.x,self.y))

    def draw(self,window):
        window.blit(self.image,(self.x,self.y))
    
    def delete(self):
        self.isDeleted = True
    
    def move_toward(self,object):
        x_dif = object.x - self.x
        y_dif = object.y - self.y
        dis = math.sqrt(x_dif**2+y_dif**2)
        if dis!=0:
            x_dif /= dis
            y_dif /= dis
        self.x += x_dif*self.speed*0.1
        self.y += y_dif*self.speed*0.1

if __name__ == "__main__":
    print("open game.py to execute")