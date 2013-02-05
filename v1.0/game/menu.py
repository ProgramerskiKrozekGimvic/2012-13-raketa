import pyglet
from .screen import *
from .gameover import *
from .seznami import *
from . import gumb

class Menu():
    def __init__(self):
        #gameover.game_over=True
        #gumb=gumb.Gumb
        self.buttons = []
        self.buttonsBatch = pyglet.graphics.Batch()


    def draw(self):
        self.buttonsBatch.draw()

    def preveriKlike(self):
        for i in self.buttons:
            i.klik()

    def addButton(self):
        pass

        
        


    
    


