from utils import *
import cv2

w,h=360,240

myDrone = intializeTello()

while True:
    ## STEP 1
    img = telloGetFrame(myDrone,w,h)

    img, info = findFace(img)
    print(info[0][0])
    # DISPLAY IMAGE
    cv2.imshow("Image", img)
    if cv2.waitKey(1) and 0xFF == ord('q'):
        myDrone.land()
        break
