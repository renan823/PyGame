import random
from utils import *

colors = [
    (255, 0, 255),
    (0, 255, 255),
    (255, 255, 0)
]

class Enemy:
    def __init__(self, width, height):
        self.position = { "x": random.randint(50, (width -60)), "y": random.randint(-80, -30) }
        self.speed = (random.randrange(2, 5) / 10)
        self.dimension = { "w": 60, "h": 60, "screen": (width, height)}
        self.alive = True
        self.color = colors[random.randint(0, len(colors)) -1]

    def move(self, player): 
        if collider(self, player):
            player.alive = False
            self.alive = False
            return
        if (self.dimension["h"] + self.position["y"]) + 1 < self.dimension["screen"][1]:
            for bullet in player.bullets:
                if collider(self, bullet):
                    player.points += 40
                    self.alive = False
                    bullet.alive = False
                    return
            self.position["y"] += self.speed
        else:
            self.alive = False
            player.points -= 10
    
    def rect(self):
        return [self.position["x"], self.position["y"], self.dimension["w"], self.dimension["h"]]