import pygame
from sys import exit
from player import Player
from arrow import Arrow

pygame.init()

pygame.display.set_caption("Game")

BG_COLOR = (255,255,255)
WIDTH = 640
HEIGHT = 320
FPS = 60

window = pygame.display.set_mode((WIDTH,HEIGHT))
player = Player(320,160)
arrow = Arrow(320,160)

def main(window):
    clock = pygame.time.Clock()
    run = True
    start(window)
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        process(window)
        clock.tick(FPS)
        pygame.display.update()


def start(window):
    pass

def process(window):
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        player.direction = "left"
        player.rotate(90)
        player.move((-1,0))
    elif keys[pygame.K_RIGHT]:
        player.direction = "right"
        player.rotate(-90)
        player.move((1,0))
    if keys[pygame.K_UP]:
        player.direction = "up"
        player.flip("ver",False)
        player.move((0,-1))
    elif keys[pygame.K_DOWN]:
        player.direction = "down"
        player.flip("ver",True)
        player.move((0,1))
    arrow.follow(player)
    arrow.rotate_around(player)
    window.fill((135, 206, 235))
    player.draw(window)
    arrow.draw(window)

if __name__ == "__main__":
    main(window)