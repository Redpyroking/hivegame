import pygame

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

    def rotate(self,angle)->None:#Degree
        self.rotation = angle
        self.image = pygame.transform.rotate(self.sprite,self.rotation)
    
    def draw(self,window):
        window.blit(self.image,(self.x,self.y))
    
    def delete(self):
        self.isDeleted = True

if __name__ == "__main__":
    print("open game.py to execute")