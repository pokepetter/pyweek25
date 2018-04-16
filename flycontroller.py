from pandaeditor import *

class FlyController(Entity):

    def __init__(self):
        super().__init__()
        self.speed = .5

        self.paused = True

    def start(self):
        camera.parent = self
        camera.position = (0,0,0)
        camera.rotation = (0,0,0)
        camera.fov = 90
        mouse.locked = True
        self.position = (0,50,0)
        self.rotation_speed = 10
        self.target_rotation_y = self.rotation_y
        self.target_rotation_x = self.rotation_x



    def input(self, key):
        if key == 'escape':
            self.paused = not self.paused

    def update(self, dt):
        if self.paused:
            return

        if self.y >= 0:
            self.target_rotation_y += mouse.velocity[0] * 20
            self.target_rotation_x -= mouse.velocity[1] * 20
        else:
            self.target_rotation_y -= mouse.velocity[0] * 20
            self.target_rotation_x -= mouse.velocity[1] * 20

        self.rotation_y = lerp(self.rotation_y, self.target_rotation_y, dt * self.rotation_speed)
        self.rotation_x = lerp(self.rotation_x, self.target_rotation_x, dt * self.rotation_speed)
        # self.rotation_x -= mouse.velocity[1] * 20
        # self.rotation_x = clamp(camera.rotation_x, -90, 90)

        # if held_keys['w']:
        self.position += self.forward * self.speed
