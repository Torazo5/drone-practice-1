from djitellopy import Tello
import time
myDrone = Tello()
myDrone.connect()

print(myDrone.get_battery())

myDrone.takeoff()
time.sleep(1)
myDrone.land()