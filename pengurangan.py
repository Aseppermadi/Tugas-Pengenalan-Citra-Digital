import cv2
import numpy as np

# load citra pertama
img1 = cv2.imread('monyet2.jpg')
# konversi ke grayscale
gray1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)

# load citra kedua
img2 = cv2.imread('monyet2.jpg')
# konversi ke grayscale
gray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

# hitung pengurangan citra
result = cv2.subtract(gray1, gray2)

# tampilkan citra hasil
cv2.imshow('Result', result)
cv2.waitKey(0)
cv2.destroyAllWindows()
