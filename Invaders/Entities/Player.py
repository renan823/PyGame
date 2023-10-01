from Entities.Bullet import Bullet

class Player:
    def __init__(self, width, height):
        self.position = { "x": width/2, "y": (0.85 * height) }
        self.speed = 1
        self.points = 0
        self.dimension = { "w": 50, "h": 50, "screen": (width, height) }
        self.moving = { "l": False, "r": False }
        self.bullets = list()
    
    def move(self):
        if self.moving["l"]:
            if 0 < self.position["x"]:
                self.position["x"] -= self.speed
        elif self.moving["r"]:
            if self.dimension["screen"][1] > (self.position["x"] + self.dimension["w"]):
                self.position["x"] += self.speed
    
    def shoot(self):
        if len(self.bullets) < 10:
            self.bullets.append(Bullet({ "x": (self.position["x"] + (self.dimension["w"]/2)), "y": self.position["y"] }))

    def reload(self):
        bullets = list()
        for bullet in self.bullets:
            if bullet.alive:
                bullets.append(bullet)
        self.bullets = bullets
    
    def rect(self):
        #return player's rect collisor
        return [self.position["x"], self.position["y"], self.dimension["w"], self.dimension["h"]]