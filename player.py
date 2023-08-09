import pygame

class Player:

    def __init__(self,x,y) -> None:
        self.x = x
        self.y =y
        self.scale = (50,50)
        self.rotation = 0
        self.sprite = pygame.image.load('E:/github_projects/mazeGame/assest/player.png')
        self.sprite = pygame.transform.scale(self.sprite,self.scale)

    def create(self,window):
        window.blit(self.sprite,(self.x,self.y))

    def move(self,step,window):
        self.x += step[0]
        self.y += step[1]
        self.create(window)

