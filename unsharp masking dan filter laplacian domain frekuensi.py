import cv2
import numpy as np
from matplotlib import pyplot as plt

# Load image
img = cv2.imread('ah.png', 0)

# Apply Fourier Transform to the image
f = np.fft.fft2(img)
fshift = np.fft.fftshift(f)

# Define Laplacian filter in frequency domain
rows, cols = img.shape
crow, ccol = int(rows/2), int(cols/2)
mask = np.zeros((rows, cols), np.uint8)
mask[crow-1:crow+2, ccol-1:ccol+2] = np.array([[0, 1, 0],
                                                 [1, -4, 1],
                                                 [0, 1, 0]], np.uint8)
fshift_laplacian = fshift * mask

# Apply Inverse Fourier Transform to the Laplacian filtered image
f_laplacian = np.fft.ifftshift(fshift_laplacian)
img_laplacian = np.fft.ifft2(f_laplacian)
img_laplacian = np.abs(img_laplacian)

# Apply Unsharp Masking to the image
blurred = cv2.GaussianBlur(img, (5, 5), 0)
unsharp_mask = cv2.addWeighted(img, 1.5, blurred, -0.5, 0)

# Display the original image, Laplacian filtered image, and Unsharp Masked image
plt.subplot(131), plt.imshow(img, cmap='gray')
plt.title('Original Image'), plt.xticks([]), plt.yticks([])
plt.subplot(132), plt.imshow(img_laplacian, cmap='gray')
plt.title('Laplacian Filtered Image'), plt.xticks([]), plt.yticks([])
plt.subplot(133), plt.imshow(unsharp_mask, cmap='gray')
plt.title('Unsharp Masked Image'), plt.xticks([]), plt.yticks([])
plt.show()
