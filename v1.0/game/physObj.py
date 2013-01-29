import pyglet
from . import object


class PhysObj(object.Object):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.zabit = False

    def update(self, dt):
        super().update(dt)

    def collision(self, other):
        if ((self.width/2+other.width/2)**2 >= (self.y+self.height/2-other.y-other.height/2)**2+(self.x+self.width/2-other.x-other.width/2)**2):
            self.zabij()
            #other.zabij()


    def zabij(self):
        self.vx = self.vy = 0
        self.zabit = True

    
