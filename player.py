import pygame


sprite = pygame.image.load('E:/github_projects/mazeGame/assest/player.png')
rotation = 0
scale = (1,1)

def create(window,position):
    pygame.transform.scale(sprite,scale)
    window.blit(sprite,position)

def start():
    pass

def process():
    pass

