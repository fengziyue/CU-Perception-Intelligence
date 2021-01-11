import numpy as np
import cv2

# Load an color image
img = cv2.imread('xxx.jpg')

# Show image
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
