import cv2
import numpy as np
from matplotlib import pyplot as plt

# Load image
img = cv2.imread('afrika.jpg', 0)

# Define mask for selective filtering
rows, cols = img.shape
mask = np.zeros((rows, cols), np.uint8)
mask[50:200, 100:300] = 1

# Apply Fourier Transform to the image and the mask
f = np.fft.fft2(img)
fshift = np.fft.fftshift(f)
f_mask = fshift * mask
fshift_mask = np.fft.ifftshift(f_mask)

# Apply Inverse Fourier Transform to the masked image
img_masked = np.fft.ifft2(fshift_mask)
img_masked = np.abs(img_masked)

# Display the original image and the masked image
plt.subplot(121), plt.imshow(img, cmap='gray')
plt.title('Original Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122), plt.imshow(img_masked, cmap='gray')
plt.title('Selective Filtered Image'), plt.xticks([]), plt.yticks([])
plt.show()
