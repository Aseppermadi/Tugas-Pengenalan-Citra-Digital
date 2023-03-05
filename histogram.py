import cv2
import numpy as np
from matplotlib import pyplot as plt

# membaca gambar
img = cv2.imread('monyet1.jpg', 0)

# menghitung histogram gambar
hist, bins = np.histogram(img.flatten(), 256, [0, 256])

# menampilkan gambar dan histogramnya
cv2.imshow('Image', img)
plt.hist(img.flatten(), 256, [0, 256], color='r')
plt.xlim([0, 256])
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()
