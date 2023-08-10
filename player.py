import pygame

class Player:

    def __init__(self,x,y) -> None:
        self.x = x
        self.y =y
        self.scale = (30,30)
        self.rotation = 0
        self.sprite = pygame.image.load('E:/github_projects/mazeGame/assest/player.png')
        self.sprite = pygame.transform.scale(self.sprite,self.scale)

    def create(self,window):
        window.blit(self.sprite,(self.x,self.y))

    def move(self,step,window):
        self.x += step[0]
        self.y += step[1]
        if step[0] < 0:
            self.flip_sprite("hor",True)
        else:
            self.flip_sprite("hor",False)
        self.create(window)
    
    def flip_sprite(self,place,value):#hor = horizontal,ver = verticle
        scale = list(self.scale)
        if place == "hor" and value:
            scale[0] * -1
            self.scale = tuple(scale)
        elif place == "ver" and value:
            scale[1] * -1
            self.scale = tuple(scale)
        self.sprite = pygame.transform.scale(self.sprite,self.scale)


