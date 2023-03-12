import cv2
import numpy as np

def gaussian_lowpass_filter(image, sigma):
    rows, cols = image.shape
    dft = np.fft.fft2(image)
    dft_shift = np.fft.fftshift(dft)
    H = np.zeros((rows, cols))
    for i in range(rows):
        for j in range(cols):
            H[i,j] = np.exp(-((i-rows//2)**2 + (j-cols//2)**2)/(2*sigma**2))
    G = np.multiply(dft_shift, H)
    g = np.fft.ifft2(np.fft.ifftshift(G))
    return np.abs(g)

def ideal_highpass_filter(image, cutoff):
    rows, cols = image.shape
    dft = np.fft.fft2(image)
    dft_shift = np.fft.fftshift(dft)
    H = np.zeros((rows, cols))
    for i in range(rows):
        for j in range(cols):
            distance = np.sqrt((i-rows//2)**2 + (j-cols//2)**2)
            if distance > cutoff:
                H[i,j] = 1
    G = np.multiply(dft_shift, H)
    g = np.fft.ifft2(np.fft.ifftshift(G))
    return np.abs(g)

# Load the input image
image = cv2.imread('afrika.jpg', 0)

# Apply Gaussian lowpass filter with sigma=10
filtered_image = gaussian_lowpass_filter(image, 10)

# Apply Ideal highpass filter with cutoff=50
filtered_image = ideal_highpass_filter(image, 50)

# Display the original and filtered images
cv2.imshow('Original Image', image)
cv2.imshow('Filtered Image', filtered_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
