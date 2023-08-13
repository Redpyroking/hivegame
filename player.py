import pygame

class Player:

    def __init__(self,x,y) -> None:
        self.x = x
        self.y =y
        self.scale = (30,30)
        self.rotation = 0
        self.image = pygame.image.load('E:/github_projects/mazeGame/assest/player.png')
        self.image = pygame.transform.scale(self.image,self.scale)
        self.sprite = self.image
        self.direction = "right"
        self.speed = 5

    def flip(self,place,value)-> None:
        if place == "hor":
            self.image = pygame.transform.flip(self.sprite,value,False)
        elif place == "ver":
            self.image = pygame.transform.flip(self.sprite,False,value)

    def rotate(self,angle)->None:#Degree
        self.rotation = angle
        self.image = pygame.transform.rotate(self.sprite,self.rotation)

    def draw(self,window):
        window.blit(self.image,(self.x,self.y))

    def move(self,step):
        self.x += step[0] * self.speed
        self.y += step[1] * self.speed




