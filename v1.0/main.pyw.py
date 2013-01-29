import pyglet
import random
from pyglet.window import key
from game import object, physObj, meteor, neMeteor, raketa, metek
from game.seznami import *


window = pyglet.window.Window(width=500, height=500)

@window.event
def on_draw():
    window.clear()
    main_batch.draw()
#    test.draw()
#    test2.draw()

def update(dt):
    test.update(dt)
    for m in meteorji_list[:]:
        m.update(dt)
        m.collision(test)
        if(m.zabit):
            meteorji_list.remove(m)
    for i in metek_list[:]:
        i.update(dt)
        i.collision(test)
        if(i.zabit):
            metek_list.remove(i)


def dodaj(dt):
    tmp = physObj.PhysObj(pyglet.resource.image('meteor1.png'), batch = main_batch)
    tmp.x=random.randint(0, window.width-100)
    tmp.y=window.height
    tmp.vy = random.randint(-150, -50)
    meteorji_list.append(tmp)


    



test = raketa.Raketa(pyglet.resource.image('raketa1.png'), batch=main_batch)
window.push_handlers(test.key_handler)




if(__name__ == '__main__'):
    pyglet.clock.schedule_interval(update, 1/120)
    dodaj(0)
    pyglet.clock.schedule_interval(dodaj, 1)
    pyglet.app.run()
    
