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
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        process(window)
        clock.tick(FPS)
        pygame.display.update()


def start(window):
    window.fill((44, 92, 221))

def process(window):
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        player.direction = "left"
        player.move((-5,0),window)
    elif keys[pygame.K_RIGHT]:
        player.direction = "right"
        player.move((5,0),window)
    if keys[pygame.K_UP]:
        player.direction = "up"
        player.move((0,-5),window)
    elif keys[pygame.K_DOWN]:
        player.direction = "down"
        player.move((0,5),window)
    if player.direction == "right":
        player.image = player.sprite
    elif player.direction == "left":
        player.image = player.flip_sprite
    window.fill((44, 92, 221))
    player.create(window)


if __name__ == "__main__":
    main(window)