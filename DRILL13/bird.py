from pico2d import *
import random
import game_framework
import game_world

PIXEL_PER_METER = (10.0 / 0.3)
RUN_SPEED_KMPH = 70.0
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 5

class Bird:
    def __init__(self):
        self.x, self.y = random.randint(100, 1500), 200
        self.frame = 0
        self.dir, self.face_dir = 1, 1
        self.image = load_image('bird_animation.png')

    def update(self):
        self.frame = (self.frame + FRAMES_PER_ACTION * game_framework.frame_time) % 5
        self.x += self.dir * RUN_SPEED_PPS * game_framework.frame_time

        if self.x <= 25:
            self.dir = 1
        elif self.x >= 1600:
            self.dir = -1

    def draw(self):
        if self.dir == -1:
            self.image.clip_composite_draw(int(self.frame)*180, 378, 180, 186, 0, 'v', self.x, self.y)
        elif self.dir == 1:
            self.image.clip_draw(int(self.frame)*180, 378, 180, 126, self.x, self.y)