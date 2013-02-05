import pyglet


class Gumb(pyglet.sprite.Sprite):
    def __init__ (self, *args, name = "Gumb", **kwargs):
        super().__init__(*args, **kwargs)
        self.name = name


    def klik(self, x, y):
        if(self.x<x and self.x+self.width>x and self.y<y and self.y+self.height>y):
            print("True")
            return(True)
        else:
            return(False)
