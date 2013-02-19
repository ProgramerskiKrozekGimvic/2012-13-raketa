import pyglet
import random
from pyglet.window import key
from .screen import *
from game import menu, raketa, gumb, meteor, gameover

class Game():
    def __init__(self):
        pass
        #myInit()

    def myInit(self):
        self.main_batch = pyglet.graphics.Batch()
        self.meteorji_list = []
        self.metek_list = []
        self.menuEnd_list = []
        self.menuStart_list = []
        self.menuPause_list = []

        
        self.menu1 = menu.Menu()
        #menu2 = menu.Menu()
        tmp = pyglet.resource.image('gumb.png')
        tmp.anchor_x = tmp.width/2
        tmp.anchor_y = tmp.height/2
        self.menu1.buttons.append(gumb.Gumb(tmp, name = "Retry", batch = self.menu1.buttonsBatch, x = window.width/2, y = window.height/2))
        self.menu1.buttons.append(gumb.Gumb(tmp, name = "Exit", batch = self.menu1.buttonsBatch, x = window.width/2, y = window.height/2 - 80))
        for i in self.menu1.buttons[:]:
            napis  = pyglet.text.Label(text=i.name, font_size=20, x=i.x, y=i.y, bold = True, color=(0, 0, 255, 255), anchor_x = "center", anchor_y = "center")
            self.menu1.labels.append(napis)

        self.restart()

    def restart(self):
        gameover.game_over = False
        self.main_batch = []
        self.meteorji_list = []
        self.metek_list = []
        self.raketa = raketa.Raketa(pyglet.resource.image('raketa2.png'), batch=self.main_batch)
        window.push_handlers(self.raketa.key_handler)

        napis = pyglet.text.Label(text="Game over", font_size=50, x=75, y=350, bold = True, color=(250, 250, 0, 255))
        napis.rotation = 50
        self.menu1.labels.append(napis)

    def draw(self):
        if(not gameover.game_over):
            self.main_batch.draw()
            self.raketa.draw()
        
        else:
            self.menu1.draw()
            for e in self.menu1.labels[:]:
                e.draw()

    def mouse_press(self, x, y):
        if(gameover.game_over):
            self.menu1.preveriKlike(x, y)

    def update(self, dt):
        if(not gameover.game_over):
            self.raketa.update(dt)
            for m in self.meteorji_list[:]:
                m.update(dt)
            for i in self.metek_list[:]:
                i.update(dt)
            for m in self.meteorji_list[:]:
                m.collision(self.raketa)
                for i in self.metek_list[:]:
                    m.collision(i)
        else:
            pass

    def dodaj(self):        
        tmp = meteor.Meteor(pyglet.resource.image('meteor2.png'), batch = self.main_batch)
        tmp.x=random.randint(0, window.width-100)
        tmp.y=window.height
        tmp.vy = random.randint(-150, -50)
        self.meteorji_list.append(tmp)

    
