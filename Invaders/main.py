import pygame
import sys

from Entities.Player import Player
from Entities.Enemy import Enemy

pygame.init()

#Screen setup
width = 800
height = 800

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Invasores espaciais")

#Player settings
player = Player(width, height)

enemies = [Enemy(width, height)]

while True:

    screen.fill((0, 0, 0))

    #player movement
    player.move()
    pygame.draw.rect(screen, (255, 255, 255), player.rect())

    #bullets movement 
    for bullet in player.bullets:
        collide = bullet.move()
        pygame.draw.rect(screen, (255, 255, 255), bullet.rect())
    player.reload()

    #enemies movement
    for enemy in enemies:
        enemy.move()
        pygame.draw.rect(screen, (255, 255, 255), enemy.rect())

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        if event.type == pygame.KEYDOWN:
            
            if event.key == pygame.K_LEFT:
                player.moving["r"] = False
                player.moving["l"] = True

            if event.key == pygame.K_RIGHT:
                player.moving["l"] = False
                player.moving["r"] = True

            if event.key == pygame.K_SPACE:
                player.shoot()
        
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                player.moving["l"] = False

            if event.key == pygame.K_RIGHT:
                player.moving["r"] = False

    pygame.display.update()