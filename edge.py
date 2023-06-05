import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

img = cv.imread('image/image.jpg')
cv.imshow('Image', img)

#grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

#laplacian
lap = cv.Laplacian(gray, cv.CV_64F)
lap = np.uint8(np.absolute(lap))
#cv.imshow('Laplacian', lap)

#Sobel
sobelx = cv.Sobel(img, cv.CV_64F, 1, 0)
cv.imshow('SobelX', sobelx)
sobely = cv.Sobel(img, cv.CV_64F, 0, 1)
cv.imshow('SobelY', sobely)
combine = cv.bitwise_or(sobelx, sobely)
cv.imshow('Sobel', combine)

#Edge Cascade
cascade = cv.Canny(gray, 125,175)
cv.imshow('Cascade', cascade)
cv.waitKey(0)