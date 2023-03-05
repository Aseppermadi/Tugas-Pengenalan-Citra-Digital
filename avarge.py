import cv2
import numpy as np

# load citra dengan noise
img_noise = cv2.imread('monyet1.jpg')

# tampilkan citra dengan noise
cv2.imshow('Image with noise', img_noise)

# kernel untuk image average
kernel = np.ones((5,5), np.float32)/25

# lakukan konvolusi citra dengan kernel
img_avg = cv2.filter2D(img_noise, -1, kernel)

# tampilkan citra hasil
cv2.imshow('Image after image averaging', img_avg)
cv2.waitKey(0)
cv2.destroyAllWindows()