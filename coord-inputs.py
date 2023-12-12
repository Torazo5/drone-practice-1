from djitellopy import Tello
import time
current_coords = (0,0)
def move_to_coordinates(coords, drone, x, y):
    dist_to_change = (x-coords[0], y-coords[1])
    print(dist_to_change)
    dist_x = dist_to_change[0]*10
    dist_y = dist_to_change[1]*10
    if dist_x < 0:
        if abs(dist_x) < 20:
            dist_x = 20
        drone.move_left(abs(dist_x))
    elif dist_x == 0:
        pass
    else:
        if abs(dist_x) < 20:
            dist_x = 20
        drone.move_right(abs(dist_x))
    time.sleep(0.5)
    if dist_y < 0:
        if abs(dist_y)<20:
            dist_y = 20
        drone.move_back(abs(dist_y))
    elif dist_y == 0:
        pass
    else:
        if abs(dist_y)<20:
            dist_y = 20
        drone.move_forward(abs(dist_y))
    time.sleep(0.5)


myDrone = Tello()
myDrone.connect()

print(myDrone.get_battery())

myDrone.takeoff()

while True:
    try:
        # Input coordinates as space-separated integers
        input_coords = input('Enter coordinates (x y): ')
        if input_coords.lower() == 'end':
            break

        x, y = map(int, input_coords.split())
        print(f'Moving to coordinates: ({x}, {y})')
        move_to_coordinates(current_coords, myDrone, x, y)
        time.sleep(2)  # Pause before next input
        current_coords = (x,y)
        print(f'Current coords x:{current_coords[0]} y:{current_coords[1]}')
    except ValueError:
        print('Invalid input. Please enter space-separated integers.')

myDrone.land()
myDrone.end()

#Enter coordinates (x y): -3 3
#Enter coordinates (x y): -4 3