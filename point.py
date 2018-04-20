from pandaeditor import *

class Point(Entity):

    def __init__(self):
        super().__init__()
        self.model = 'cube'
        self.collider = 'box'
        self.scale *= 2


    def on_mouse_enter(self):
        self.color = color.lime
        self.animate_scale(self.scale * 0, duration=1)
