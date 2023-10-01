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

def addText(txt, pos, color, size):                              
    pygame.font.init()                                
    font = pygame.font.get_default_font()              
    useFont = pygame.font.SysFont(font , size)           
    txtScreen = useFont.render(txt, 1, color)  
    screen.blit(txtScreen, pos)   

while True:

    screen.fill((0, 0, 0))

    #player movement
    player.move()
    pygame.draw.rect(screen, (255, 255, 255), player.rect())

    #bullets movement 
    for bullet in player.bullets:
        bullet.move()
        pygame.draw.rect(screen, (0, 255, 0), bullet.rect())
    player.reload()

    #enemies movement
    alive = list()
    for enemy in enemies:
        enemy.move(player)  
        if enemy.alive:
            alive.append(enemy)
        pygame.draw.rect(screen, enemy.color, enemy.rect())
    enemies = alive

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
    
    addText(str(player.points), (20, 20), (255, 255, 255), 40)
    
    if len(enemies) != 8:
        enemies.append(Enemy(width, height))
  
    if (not player.alive) or (player.points < 0):
        pygame.quit()
        sys.exit()

    pygame.display.update()