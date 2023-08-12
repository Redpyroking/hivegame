import pygame

class Player:

    def __init__(self,x,y) -> None:
        self.x = x
        self.y =y
        self.scale = (30,30)
        self.rotation = 0
        self.image = pygame.image.load('E:/github_projects/mazeGame/assest/player.png')
        self.image = pygame.transform.scale(self.image,self.scale)
        self.sprite = pygame.transform.flip(self.image,False,False)
        self.flip_sprite = pygame.transform.flip(self.image,True,False)
        self.direction = "right"

    def create(self,window):
        window.blit(self.image,(self.x,self.y))

    def move(self,step,window):
        self.x += step[0]
        self.y += step[1]




