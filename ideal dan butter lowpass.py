import cv2
import numpy as np

# Load image
img = cv2.imread('afrika.jpg', cv2.IMREAD_GRAYSCALE)

# Fourier transform
f = np.fft.fft2(img)
fshift = np.fft.fftshift(f)

# Ideal Lowpass Filter
rows, cols = img.shape
crow, ccol = rows//2, cols//2
d = 30  # cut-off distance
mask = np.zeros((rows, cols), np.uint8)
mask[crow-d:crow+d, ccol-d:ccol+d] = 1

# Butterworth Lowpass Filter
# order of filter
n = 4
# cut-off frequency
d0 = 30
u, v = np.meshgrid(np.arange(cols) - ccol, np.arange(rows) - crow)
d = np.sqrt(u**2 + v**2)
h = 1 / (1 + (d/d0)**(2*n))

# Apply mask to spectrum
fshift_filtered = fshift * mask
# Apply Butterworth filter to spectrum
fshift_filtered_bw = fshift * h

# Inverse Fourier transform
img_back = np.fft.ifft2(np.fft.ifftshift(fshift_filtered)).real
img_back_bw = np.fft.ifft2(np.fft.ifftshift(fshift_filtered_bw)).real

# Display images
cv2.imshow('Original', img)
cv2.imshow('Ideal Lowpass Filter', img_back)
cv2.imshow('Butterworth Lowpass Filter', img_back_bw)
cv2.waitKey(0)
cv2.destroyAllWindows()
