import pyglet
from . import object


class PhysObj(object.Object):
    def __init__(self, game, *args, **kwargs):
        super().__init__(game, *args, **kwargs)
        self.zabit = False

    def update(self, dt):
        super().update(dt)

    def collision(self, other):
        if ((self.width/2+other.width/2)**2 >= (self.y+self.height/2-other.y-other.height/2)**2+(self.x+self.width/2-other.x-other.width/2)**2):
            other.zabij()
            self.zabij()
            


    def zabij(self):
        #if(self.tip = "Meteor" and self.velikost = "v"):
        if(self.tip == "Raketa"):
            self.life()
        else:
            self.brisanje()
            self.zabit = True
        #self.score += 20
