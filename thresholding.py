import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

img = cv.imread('image/image.jpg')
cv.imshow('Image', img)

#grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
#cv.imshow('Gray', gray)

#simple thresholding
threshold, thresh = cv.threshold(gray, 150, 255, cv.THRESH_BINARY_INV)

#adaptive thresholding
adaptive = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 7, 3)
cv.imshow('Adaptive Thresh', adaptive)


cv.waitKey(0)