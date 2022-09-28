from enum import Enum
from pico2d import *

open_canvas()

character = load_image('hero_spritesheet.png')
grass = load_image('grass.png')

class Motion(Enum):
    Basic = 0
    Walk = 1
    Slow_Walk = 2
    Die = 3
    Gun = 4

x = 0
y = 0
z = 0

MotionList = [8, 6, 6, 7, 2]
frame1 = 0
frame2 = 0
frame3 = 0
frame4 = 0
frame5 = 0

while (x < 800):
    clear_canvas()
    grass.draw(400, 30)
    character.clip_draw(frame1 * 80, 380 - 94 * 0, 80, 94, 200, 90)  #가만히 총 쏘기
    character.clip_draw(frame2 * 80, 380 - 94 * 1, 80, 94, x, 90)   #한소으로 총들고 걷기
    character.clip_draw(frame3 * 80, 380 - 94 * 2, 80, 94, y, 90)   #두손으로 총들고 느리게 걷기
    character.clip_draw(frame4 * 80, 380 - 94 * 3, 80, 94, 300, 90)   #죽는거 구현
    character.clip_draw(frame5 * 80, 380 - 94 * 4, 80, 94, 400, 80) #앉아서 총쏘기
    update_canvas()
    frame1 = (frame1 + 1) % MotionList[0]
    frame2 = (frame2 + 1) % MotionList[1]
    frame3 = (frame3 + 1) % MotionList[2]    
    frame4 = (frame4 + 1) % MotionList[3]
    frame5 = (frame5 + 1) % MotionList[4]

    x += 5
    y += 2
    z += 1
    delay(0.1)
    get_events()

close_canvas()
