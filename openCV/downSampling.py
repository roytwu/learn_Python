import cv2
import numpy as np
print(cv2.__version__)

#img = cv2.imread('upSampling.png', 0)
img = cv2.imread('upSampling.png')
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#dimen = img.shape
#print(dimen)

#img =cv2.pyrDown(img)
#img =cv2.pyrDown(img)
#img =cv2.pyrDown(img)
#img =cv2.pyrDown(img)

#img = median_filter(img, 1)

#lap = cv2.Laplacian(imgGray, cv2.CV_64F)
#lap2 = lap/lap.max()
#sharp = imgGray - 0.7*lap

# Create kernel
kernel = np.array([[0, -1, 0], [-1, 5,-1], [0, -1, 0]])
#kernel = np.array([[-1,-1,-1], [-1,9,-1], [-1,-1,-1]])

# Sharpen image
sharp = cv2.filter2D(imgGray, -1, kernel)

dimen = img.shape
print(dimen)
      
cv2.imwrite('output.png', sharp)
#cv2.imshow('output', sharp)
#cv2.waitKey(0)
print('program finished...')