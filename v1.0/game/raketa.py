import pyglet
from pyglet.window import key
from .seznami import *
from . import neMeteor, metek


class Raketa(neMeteor.NeMeteor):
    def __init__ (self, *args,**kwargs):
        super().__init__(*args, **kwargs)
        self.key_handler=key.KeyStateHandler()
        self.vx = 200

    def update(self, dt):
        if(self.key_handler[key.LEFT]):
            self.x -= self.vx*dt
        if(self.key_handler[key.RIGHT]):
            self.x += self.vx*dt
        if(self.x<=-self.width//2):
            self.x=500-self.width//2
        if(self.x>500-self.width//2):
            self.x=-self.width//2
        if(self.key_handler[key.SPACE]):
            self.strel()

    def collision(self, other):
        super().collision(other)
        
    def strel(self):
        tmp = metek.Metek(pyglet.resource.image('bull1.png'), batch = main_batch)
        tmp.x = self.x + self.width//2-2
        tmp.y = self.height
        metek_list.append(tmp)

    def zabij(self):
        super().zabij()


                        
