import pyglet
import random
from .import physObj

class Meteor(physObj.PhysObj):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.tip = "Meteor"

    def update(self, dt):
        super().update(dt)

    def collision(self, other):
        super().collision(other)

    def zabij(self):
        super().zabij()
        if(self.velikost=="v"):
            x=random.randint(1,3)
            if(x==1):
                self.split()
        #Za score.
        if(self.game.raketa.zabit==False):
            if(self.zabit == True and self.velikost == "m"):
                self.game.score += 20
            elif(self.zabit == True and self.velikost == "v"):
                self.game.score += 30
        self.game.raketa.zabit=False

    def split(self):
        for i in range (2):
            tmp = Meteor(self.game, pyglet.resource.image('meteor1.png'), batch = self.game.main_batch)
            tmp.velikost="m"
            tmp.y=self.y+(2-i)*30
            tmp.x=self.x+(i-1)*30
            tmp.vy=self.vy
            self.game.meteorji_list.append(tmp)

    
