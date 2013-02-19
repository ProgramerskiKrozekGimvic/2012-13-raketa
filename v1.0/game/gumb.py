import pyglet
from .screen import *


class Gumb(pyglet.sprite.Sprite):
    def __init__ (self, *args, name = "Gumb", **kwargs):
        super().__init__(*args, **kwargs)
        self.name = name


    def klik(self, x, y):
        #print("klik")
        if(self.x - self.width/2 <= x and self.x+self.width/2 >= x and self.y - self.height/2 <= y and self.y+self.height/2 >= y):
            print(self.name)
            if(self.name == "Exit"):
                window.close()
            elif(self.name == "Retry"):
                game.restart()
            return(True)
        else:
            return(False)
