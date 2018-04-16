from pandaeditor import *
from flycontroller import FlyController

app = PandaEditor()
# window.size *= .33
window.center_on_screen()

e = Entity(
    model = 'quad',
    texture = 'world_0',
    rotation_x = 90
    )

sky = Sky()

e.scale *= 500
water = Entity(
    model = 'quad',
    color = color.color(227, .2, .55),
    rotation_x = 90,
    scale = (9999, 9999, 9999),
    y = -1
    )
# water = Sky('world_0')
# water.color = color.blue
# water.rotation_z = 180

player = FlyController()

camera.position = (100, 100,100)
camera.look_at(e)

e = Entity(
    model = 'quad',
    texture = 'world_0',
    rotation_x = -90,
    color = color.blue
    )
e.scale *= 500

app.run()
