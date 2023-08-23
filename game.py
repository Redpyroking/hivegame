import pygame
from sys import exit
import random
from player import Player
from arrow import Arrow
from enemy import Enemy

pygame.init()

pygame.display.set_caption("Game")

BG_COLOR = (255,255,255)
WIDTH = 640
HEIGHT = 320
FPS = 60

window = pygame.display.set_mode((WIDTH,HEIGHT))
player = Player(320,160)
arrow = Arrow(320,160)
enemy_ship = Enemy(400,200)
new_ships = []

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
    for i in range(4):
        new_enemy_ship = Enemy(random.randrange(100,600),random.randrange(30,300))
        new_ships.append(new_enemy_ship)

def process(window):
    keys = pygame.key.get_pressed()
    window.fill((135, 206, 235))
    if player:
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
        player.draw(window)
    if arrow:
        arrow.follow(player)
        arrow.rotate_around(player)
        arrow.draw(window)
    if enemy_ship:
        if not enemy_ship.isDeleted:
            enemy_ship.draw(window)
        enemy_ship.delete()
    for i in new_ships:
        i.draw(window)

if __name__ == "__main__":
    main(window)