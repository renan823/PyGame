class Bullet:
    def __init__(self, position):
        self.position = { "x": (position["x"] - 5), "y": (position["y"] -10) }
        self.speed = 1
        self.dimension = { "w": 10, "h": 10 }
        self.alive = True
    
    def move(self):
        if self.position["y"] > 40:
            self.position["y"] -= self.speed
        else:
            self.alive = False
    
    def rect(self):
        return [self.position["x"], self.position["y"], self.dimension["w"], self.dimension["h"]]
