import pyglet
from .import physObj

class NeMeteor(physObj.PhysObj):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def update(self, dt):
        super().update(dt)

    def collision(self, other):
        super().collision(other)
        

    def zabij(self):
        super().zabij()
