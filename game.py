import pygame
from sys import exit
import random
from player import Player
from arrow import Arrow
from enemy import Enemy
from player_bullet import playerBullet

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
bullets = []
global just_pressed
just_pressed = False

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
        #new_enemy_ship = Enemy(random.randrange(WIDTH+100,WIDTH+300),random.randrange(HEIGHT+100,HEIGHT+300))
        new_enemy_ship = Enemy(random.randrange(100,300),random.randrange(100,300))
        new_enemy_ship.speed = random.randrange(5,15)
        new_ships.append(new_enemy_ship)

def process(window):
    keys = pygame.key.get_pressed()
    mouse = pygame.mouse.get_pressed()
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
        if mouse[0] == True:
            global just_pressed
            if not just_pressed:#mouse[0] is left click and mouse is not just pressed
                bullet = playerBullet(player.x,player.y)
                bullet.followPos = pygame.mouse.get_pos()
                bullets.append(bullet)
                just_pressed = True
        else:
            just_pressed = False
        player.draw(window)
    if arrow:
        arrow.follow(player)
        arrow.rotate_around(player)
        arrow.draw(window)
    for i in new_ships:
        i.move_toward(player)
        i.rotate_around(player)
        i.draw(window)
    for i in bullets:
        if i.isDeleted:
            bullets.remove(i)
        i.move_toward_pos()
        i.draw(window)
        if i.is_outside_border(WIDTH,HEIGHT):
            i.isDeleted = True

if __name__ == "__main__":
    main(window)