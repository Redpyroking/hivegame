import pygame
from sys import exit
from player import Player

pygame.init()

pygame.display.set_caption("Game")

BG_COLOR = (255,255,255)
WIDTH = 640
HEIGHT = 320
FPS = 60

window = pygame.display.set_mode((WIDTH,HEIGHT))
player = Player(320,160)

def main(window):
    clock = pygame.time.Clock()
    run = True
    start(window)
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        process(window)

def start(window):
    window.fill((44, 92, 221))

def process(window):
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player.move((-10,0),window)
    if keys[pygame.K_RIGHT]:
        player.move((10,0),window)
    window.fill((44, 92, 221))
    player.create(window)
    pygame.display.update()

if __name__ == "__main__":
    main(window)