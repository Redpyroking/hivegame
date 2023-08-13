import pygame
class Arrow:

    def __init__(self,x,y) -> None:
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
        pass

    def draw(self,window):
        window.blit(self.image,(self.x,self.y))