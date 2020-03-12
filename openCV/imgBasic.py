#* ----------------------------------------
#* Author:      Roy Wu
#* Description: Basic program of Python OpenCV
#* ----------------------------------------
import cv2
import numpy as np
print(cv2.__version__)

#* read an image
img = cv2.imread('sample/robot.png')

print(img.shape)
print(img.dtype)

#b,g,r = cv2.split(img)
#print("b is ...", b)


px127 = img[127, 127]
pxA   = img[30, 60]
print("px127 is ...", px127) #* shall be black (B,G,R)
print("pxA is ...", pxA)     #* shall be cyan (B,G,R)

#* make window resizable 
cv2.namedWindow('resized_Win', cv2.WINDOW_NORMAL)
#* resize window
h = img.shape[0] #* height
w = img.shape[1] #* width
cv2.resizeWindow('resized_Win', w*3, h*3)

cv2.imshow('resized_Win', img)

