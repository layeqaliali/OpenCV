import cv2 as cv

img = cv.imread('image/person.jpg')
cv.imshow('Image', img)

#Averaging
average = cv.blur(img, (7,7))
cv.imshow('Average', average)

#Guassian Blur
guass = cv.GaussianBlur(img, (7,7), 0)
cv.imshow('Guass', guass)

#Median blur
median = cv.medianBlur(img, 3)
cv.imshow('Median', median)

#biletral blur
bilate = cv.bilateralFilter(img, 5, 15, 15)
cv.imshow('Bilate', bilate)

cv.waitKey(0)