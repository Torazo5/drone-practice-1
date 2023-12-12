from djitellopy import Tello
import time

# CONNECT TO TELLO
myDrone = Tello()
myDrone.connect()
myDrone.for_back_velocity = 0
myDrone.left_right_velocity = 0
myDrone.up_down_velocity = 0
myDrone.yaw_velocity = 0
myDrone.speed = 0
print(myDrone.get_battery())

def move_to_coords(x, y):
    velocity = 50

    if x > 0:
        myDrone.send_rc_control(0, velocity, 0, 0)
    else:
        myDrone.send_rc_control(0, -velocity, 0, 0)
    time.sleep((abs(x)*10)/velocity)
    print(f'Waited for {(abs(x)*10)/velocity} seconds')

    myDrone.send_rc_control(0, 0, 0, 0)

    if y > 0:
        myDrone.send_rc_control(velocity, 0, 0, 0)
    else:
        myDrone.send_rc_control(-velocity, 0, 0, 0)
    time.sleep((abs(y)*10)/velocity)
    print(f'Waited for {(abs(y)*10)/velocity} seconds')

    myDrone.send_rc_control(0, 0, 0, 0)


myDrone.takeoff()

while True:
    inp = input('Land? (y/n): ')
    if inp.lower() == 'y':
        myDrone.land()
        break

    print('Next coordinates? (x y):')
    try:
        next_coords_x, next_coords_y = map(int, input().split())
        move_to_coords(next_coords_x, next_coords_y)
        time.sleep(2)
    except ValueError:
        print('Invalid input. Please enter integer coordinates.')

myDrone.end()
