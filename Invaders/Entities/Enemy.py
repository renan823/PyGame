import random

class Enemy:
    def __init__(self, width, height):
        self.position = { "x": random.randint(50, (width -50)), "y": (0.15 * height) }
        self.speed = (random.random() + 0.1)
        self.dimension = { "w": 60, "h": 60, "screen": (width, height)}
        self.alive = True

    def move(self): 
        if (self.dimension["h"] + self.position["y"]) < self.dimension["screen"][1]:
            self.position["y"] += self.speed
        else:
            self.alive = False
    
    def rect(self):
        return [self.position["x"], self.position["y"], self.dimension["w"], self.dimension["h"]]