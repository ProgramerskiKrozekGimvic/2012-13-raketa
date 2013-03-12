import pyglet
from .screen import *
from . import gameover

class Gumb(pyglet.sprite.Sprite):
    def __init__ (self, game, *args, name = "Gumb", **kwargs):
        super().__init__(*args, **kwargs)
        self.name = name
        self.game = game


    def klik(self, x, y):
        #print("klik")
        if(self.x - self.width/2 <= x and self.x+self.width/2 >= x and self.y - self.height/2 <= y and self.y+self.height/2 >= y):
            print(self.name)
            if(self.name == "Exit"):
                window.close()
            elif(self.name == "Retry"):
                self.game.myInit()
            elif(self.name == "Main Menu"):
                self.game.start()
                gameover.start = True
            elif(self.name == "Start"):
                self.game.myInit()
            return(True)
        else:
            return(False)
