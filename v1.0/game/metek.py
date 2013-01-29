import pyglet
from pyglet.window import key
from . import neMeteor

class Metek(neMeteor.NeMeteor):
    def __init__ (self, *args,**kwargs):
        super().__init__(*args, **kwargs)
        self.vy = 400
        self.tip = "Metek"

    def update(self, dt):
        super().update(dt)

    def collision(self, other):
        super().collision(other)
        
    def zabij(self):
        super().zabij()
