from pandaeditor import *

class FlyController(Entity):

    def __init__(self):
        super().__init__()
        self.speed = 0
        self._speed = 0
        self.max_speed = .5
        self.acceleration_rate = 5

        self.paused = True

    def start(self):
        camera.parent = self
        camera.position = (0,0,0)
        camera.rotation = (0,0,0)
        camera.fov = 90
        mouse.locked = True
        self.position = (0,50,0)
        self.rotation_speed = 3
        self.target_rotation_y = self.rotation_y
        self.target_rotation_x = self.rotation_x



    def input(self, key):
        if key == 'space':
            self.speed = 0
            self.rotation_speed /= 2
        elif key == 'space up':
            self.speed = self.max_speed
            self.rotation_speed *= 2



    def update(self, dt):
        ## mouse movement
        # if self.y >= 0:
        #     self.target_rotation_y += mouse.velocity[0] * 20
        #     self.target_rotation_x -= mouse.velocity[1] * 20
        # else:
        #     self.target_rotation_y -= mouse.velocity[0] * 20
        #     self.target_rotation_x -= mouse.velocity[1] * 20


        # keyboard movement
        self.target_rotation_x -= held_keys['s']
        self.target_rotation_x += held_keys['w']
        if self.y >= 0:
            self.target_rotation_y += held_keys['d']
            self.target_rotation_y -= held_keys['a']
        else:
            self.target_rotation_y += held_keys['d'] * -1
            self.target_rotation_y -= held_keys['a'] * -1


        self.rotation_y = lerp(self.rotation_y, self.target_rotation_y, dt * self.rotation_speed)
        self.rotation_x = lerp(self.rotation_x, self.target_rotation_x, dt * self.rotation_speed)
        self._speed = lerp(self._speed, self.speed, dt * self.acceleration_rate)




        self.position += self.forward * self._speed
