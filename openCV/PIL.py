from PIL import Image
from PIL import ImageEnhance
import cv2
import numpy as np

img = Image.open('averaging.png')
#img = Image.open('upsampling.png')


img_sharp = ImageEnhance.Contrast(img)
para = 3
imgOut = img_sharp.enhance(para)
imgOut.save('newimage.png')

#img_sharp = ImageEnhance.Sharpness(img)
#sharpness = 2
#image_sharped = img_sharp.enhance(sharpness)
#image_sharped.save('newimage.png')

print('program finished...')