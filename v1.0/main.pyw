import pyglet
import random
from pyglet.window import key
from game import object, physObj, meteor, neMeteor, raketa, metek, menu, gumb
from game.seznami import *
from game.screen import *
from game import gameover



#krneki=menu.MenuEnd()

#options_menu = menu.Menu()

@window.event
def on_draw():
    window.clear()
    menu1.draw()
    print(gameover.game_over)
    if(not gameover.game_over):
        main_batch.draw()
        test.draw()
        test2.draw()
    
    else:
        menu1.draw()
#        for e in menuEnd_list[:]:
#            e.draw()

@window.event
def on_mouse_press(x, y, button, modifiers):
    pass
    #print(x, y, button, modifiers)
    menu1.preveriKlike()

def update(dt):
    if(not gameover.game_over):
       # print(metek_list)
        test.update(dt)
        for m in meteorji_list[:]:
            m.update(dt)
        for i in metek_list[:]:
            i.update(dt)
        for m in meteorji_list[:]:
            m.collision(test)
            for i in metek_list[:]:
                m.collision(i)
    else:
        pass
             
         


def dodaj(dt):
    tmp = meteor.Meteor(pyglet.resource.image('meteor2.png'), batch = main_batch)
    tmp.x=random.randint(0, window.width-100)
    tmp.y=window.height
    tmp.vy = random.randint(-150, -50)
    meteorji_list.append(tmp)


    


menu1 = menu.Menu()
#menu2 = menu.Menu()
tmp = pyglet.resource.image('bla.png')
tmp.anchor_x = tmp.width/2
tmp.anchor_y = tmp.height/2
menu1.buttons.append(gumb.Gumb(tmp, name = "Retry", batch = menu1.buttonsBatch, x = window.width/2, y = window.height/2))
menu1.buttons.append(gumb.Gumb(tmp, name = "Retry", batch = menu1.buttonsBatch, x = window.width/4, y = window.height/4))

test = raketa.Raketa(pyglet.resource.image('raketa2.png'), batch=main_batch)
window.push_handlers(test.key_handler)

napis = pyglet.text.Label(text="Game over", font_size=50, x=75, y=350, bold = True)
napis.rotation = 50
menuEnd_list.append(napis)



if(__name__ == '__main__'):
    pyglet.clock.schedule_interval(update, 1/120)
    dodaj(0)
    pyglet.clock.schedule_interval(dodaj, 1)
    pyglet.app.run()
    
