import pygame
from sys import exit
import player

pygame.init()

pygame.display.set_caption("Game")

BG_COLOR = (255,255,255)
WIDTH = 640
HEIGHT = 320
FPS = 60

window = pygame.display.set_mode((WIDTH,HEIGHT))


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
    window.fill((115,55,205))
    player.create(window,(320,160))
    pygame.display.update()

def process(window):
    pass

if __name__ == "__main__":
    main(window)