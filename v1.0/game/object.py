import pyglet
from .seznami import *
from .screen import *

class Object(pyglet.sprite.Sprite):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.vx = 0
        self.vy = 0
        self.tip = "Object"

    def update(self, dt):
        self.x += self.vx * dt
        self.y += self.vy * dt

        if(window.height <= self.y):
            self.brisanje()
        if(self.y+self.height <= 0):
            self.brisanje()
        
        
    def brisanje(self):
       # print("brisem se!!!!")
        if(self.tip=='Meteor'):
            game.meteorji_list.remove(self)
        if(self.tip=='Metek'):
            game.metek_list.remove(self)
            
