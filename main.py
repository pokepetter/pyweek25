from pandaeditor import *
from flycontroller import FlyController

app = PandaEditor()

sky = Sky()
ground = Plane(500, texture = 'world_0')
water = Plane(9999, color = color.color(227, .2, .55), y = -1)
clouds = Plane(500, texture = 'clouds', y = 20)
clouds.setTwoSided(True)

player = FlyController()

camera.position = (100, 100,100)
camera.look_at(ground)

ground = Entity(
    model = 'quad',
    texture = 'world_0',
    rotation_x = -90,
    color = color.blue
    )
ground.scale *= 500

app.run()
