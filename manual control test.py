# simple example demonstrating how to control a Tello using your keyboard.
# For a more fully featured example see manual-control-pygame.py
# 
# Use W, A, S, D for moving, E, Q for rotating and R, F for going up and down.
# When starting the script the Tello will takeoff, pressing ESC makes it land
#  and the script exit.

# 简单的演示如何用键盘控制Tello
# 欲使用全手动控制请查看 manual-control-pygame.py
#
# W, A, S, D 移动， E, Q 转向，R、F上升与下降.
# 开始运行程序时Tello会自动起飞，按ESC键降落
# 并且程序会退出

from djitellopy import Tello
import cv2, math, time

tello = Tello()
tello.connect()

tello.streamon()
frame_read = tello.get_frame_read()

tello.takeoff()

tello.move_forward(30)
tello.move_left()

tello.land()