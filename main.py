from pandaeditor import *
from flycontroller import FlyController
from point import Point

def point_in_box(*args):
    if len(args) == 0:
        return (random.uniform(-.5, .5), random.uniform(-.5, .5), random.uniform(-.5, .5))

    if len(args) == 1:
        return Vec3(
            random.uniform(-args[0], args[0]),
            random.uniform(-args[0], args[0]),
            random.uniform(-args[0], args[0])
            ) / 2
    if len(args) == 2:
        return Vec2(
            random.uniform(-args[0], args[0]),
            random.uniform(-args[1], args[1]),
            ) / 2
    if len(args) == 3:
        return Vec3(
            random.uniform(-args[0], args[0]),
            random.uniform(-args[1], args[1]),
            random.uniform(-args[2], args[2])
            ) / 2


app = PandaEditor()

sky = Sky()
ground = Plane(500, texture = 'world_0')
water = Plane(9999, color = color.color(227, .2, .55), y = -1)
# clouds = Plane(500, texture = 'clouds', y = 20)
# clouds.setTwoSided(True)

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

random.seed(0)
# for i in range(10):
#     p = Point()
#     p.position = (random.uniform(-30, 30), random.uniform(-30, 30), random.uniform(-30, 30))


for i in range(10):
    p = Entity(model = 'cube',color = color.random_color())
    p.setTwoSided(True)
    p.color  = color.dark_gray + (color.random_color() * .2)
    p.scale *= 40
    p.scale_y *= 2
    p.position = point_in_box(400, 200, 400) + (0, 140, 0)

    for j in range(10):
        p1 = Entity(model = 'cube',color = color.random_color(), parent = p)
        p1.setTwoSided(True)
        p1.color = p.color + (color.random_color() * .1)
        p1.scale *= .25
        p1.position = point_in_box()




cursor = Cursor()
app.run()
