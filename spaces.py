import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread('image/person.jpg')
cv.imshow('Image', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Grayscale', gray)

hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow('HSV', hsv)

lab = cv.cvtColor(img, cv.COLOR_BGR2RGB)
cv.imshow('LAB', lab)

plt.imshow(img)
plt.show()

cv.waitKey(0)