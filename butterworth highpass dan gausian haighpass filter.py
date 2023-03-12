import cv2
import numpy as np

def butterworth_highpass_filter(image, D, n):
    rows, cols = image.shape
    dft = np.fft.fft2(image)
    dft_shift = np.fft.fftshift(dft)
    H = np.zeros((rows, cols))
    for i in range(rows):
        for j in range(cols):
            distance = np.sqrt((i-rows//2)**2 + (j-cols//2)**2)
            H[i,j] = 1/(1 + (distance/D)**(2*n))
    G = np.multiply(dft_shift, H)
    g = np.fft.ifft2(np.fft.ifftshift(G))
    return np.abs(g)

def gaussian_highpass_filter(image, sigma):
    rows, cols = image.shape
    dft = np.fft.fft2(image)
    dft_shift = np.fft.fftshift(dft)
    H = np.zeros((rows, cols))
    for i in range(rows):
        for j in range(cols):
            distance = np.sqrt((i-rows//2)**2 + (j-cols//2)**2)
            H[i,j] = 1 - np.exp(-((distance**2)/(2*(sigma**2))))
    G = np.multiply(dft_shift, H)
    g = np.fft.ifft2(np.fft.ifftshift(G))
    return np.abs(g)

# Load the input image
image = cv2.imread('afrika.jpg', 0)

# Apply Butterworth highpass filter with D=50, n=2
filtered_image = butterworth_highpass_filter(image, 50, 2)

# Apply Gaussian highpass filter with sigma=10
filtered_image = gaussian_highpass_filter(image, 10)

# Display the original and filtered images
cv2.imshow('Original Image', image)
cv2.imshow('Filtered Image', filtered_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
