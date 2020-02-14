import scipy
from scipy import ndimage
import matplotlib.pyplot as plt

img = cv2.imread('upSampling.png')
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

blurred_f = ndimage.gaussian_filter(imgGray, 3)

filter_blurred_f = ndimage.gaussian_filter(blurred_f, 1)

alpha = 30
sharpened = blurred_f + alpha * (blurred_f - filter_blurred_f)

cv2.imwrite('result.png', sharpened)
print('program finished...')