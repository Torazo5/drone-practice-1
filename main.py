from djitellopy import tello
import KeyPressModule as kp
from time import sleep

kp.init()
me = tello.Tello()
me.connect()
print(me.get_battery())


def getKeyboardInput():
    lr, fb, ud, yv = 0, 0, 0, 0
    speed = 50
    if kp.getKey("LEFT"):
        lr = -speed
        #left right input is negative
    elif kp.getKey("RIGHT"):
        lr = speed
        #left right input is positive
    if kp.getKey("UP"):
        fb = speed
    elif kp.getKey("DOWN"):
        fb = -speed
    if kp.getKey("w"):
        ud = speed
    elif kp.getKey("s"):
        ud = -speed
    if kp.getKey("a"):
        yv = -speed
    elif kp.getKey("d"):
        yv = speed
    if kp.getKey("l"):
        me.land()
        sleep(3)
    if kp.getKey("t"):
        me.takeoff()
    #returns what has been pressed, so what changes have been made
    return [lr, fb, ud, yv]


while True:
    vals = getKeyboardInput()
    #output what we have been pressing 
    me.send_rc_control(vals[0], vals[1], vals[2], vals[3])
    sleep(0.05)
