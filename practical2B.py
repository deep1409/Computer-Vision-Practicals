# Python program to explain cv2.imread() method
# importing cv2
import cv2
# path
path = r'C:\\Users\\Deep\\Downloads\\\product-sans\\photo.jpg'
# Using cv2.imread() method
# Using 0 to read image in grayscale mode
img = cv2.imread(path, 0)
# Displaying the image
cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
