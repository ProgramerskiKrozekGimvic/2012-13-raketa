import pyglet

game_window = pyglet.window.Window(500,500)

@game_window.event
def on_draw():
    pyglet.gl.glClearColor(1, 1, 1, 1)
    game_window.clear()
    rak.blit(100, 100)
    #rak.draw()
    rak1.draw()


if(__name__ == "__main__"):
    #rak = pyglet.sprite.Sprite(pyglet.image.load("raketa2.png"), x = 100, y = 100)
    rak = pyglet.image.load("raketa.png")
    rak1 = pyglet.sprite.Sprite(pyglet.image.load("raketa1.png"), x = 200, y = 300)
    pyglet.app.run()
