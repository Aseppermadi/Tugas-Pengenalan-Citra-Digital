import cv2

# load citra pertama
img1 = cv2.imread('1.jpg')
# konversi ke grayscale
gray1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)

# load citra kedua
img2 = cv2.imread('2.jpg')
# konversi ke grayscale
gray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

# hitung perbedaan citra
diff_img = cv2.absdiff(gray1, gray2)

# tampilkan citra hasil
cv2.imshow('Difference Image', diff_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
