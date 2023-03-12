import cv2
import numpy as np
from matplotlib import pyplot as plt

# Membaca citra digital
image = cv2.imread('afrika.jpg', 0)

# Melakukan Transformasi Fourier pada citra
fft = np.fft.fft2(image)

# Menggeser frekuensi agar nol frekuensi berada di tengah
fft_shifted = np.fft.fftshift(fft)

# Menghitung magnitudo spektrum frekuensi
magnitude_spectrum = 20*np.log(np.abs(fft_shifted))

# Menampilkan citra asli dan magnitudo spektrum frekuensi
plt.subplot(121),plt.imshow(image, cmap = 'gray')
plt.title('Citra Asli'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(magnitude_spectrum, cmap = 'gray')
plt.title('Magnitudo Spektrum Frekuensi'), plt.xticks([]), plt.yticks([])
plt.show()
