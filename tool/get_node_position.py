import cv2
# pip install opencv-python
from PIL import Image, ImageDraw
clicked_points = []
mouse_x = 0
mouse_y = 0

img = cv2.imread('4.png')



def mouse_callback(event, x, y, flags, param):
    if event == cv2.EVENT_MOUSEMOVE:
        global mouse_x, mouse_y
        mouse_x = x
        mouse_y = y


cv2.namedWindow('Image')
cv2.setMouseCallback('Image', mouse_callback)
cv2.imshow('Image', img)

while True:
    key = cv2.waitKey(1)
    if key == ord('q'):
        break

    elif key == ord('a'):
        x, y = mouse_x, mouse_y
        clicked_points.append((x, y))
        print('Clicked point: ({}, {})'.format(x, y))
