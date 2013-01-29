import pyglet
from .seznami import *

class Object(pyglet.sprite.Sprite):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.vx = 0
        self.vy = 0
#        self.tip = "Object"

    def update(self, dt):
        self.x += self.vx * dt
        self.y += self.vy * dt
        """for i in metek_list[:]:
            if(window.height == self.y):
                metek_list.remove(i)
        for i in metek_list[:]:
            if(self.y+self.height == 0):
                meteor_list.remove(i)"""
            

    def brisanje(self):
        if(...):
            self.list.remove(self)
