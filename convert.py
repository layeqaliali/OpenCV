import cv2 as cv
from cv2 import imshow

img = cv.imread('image/img.jpeg')
cv.imshow('Image', img)

#COnvert to Grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('GRAY', gray)

#Blur
blur = cv.GaussianBlur(img, (7,7), cv.BORDER_DEFAULT)
cv.imshow('BLUR', blur)

#Edge Cascade
cascade = cv.Canny(img, 125,175)
cv.imshow('Cascade', cascade)

#Dilated image
dilated =  cv.dilate(img, (3,3), iterations=1)
cv.imshow('Dilated', dilated)

#Eroded
eroded = cv.erode(img, (3,3), iterations=1)
cv.imshow('Eroded', eroded)

#resize
resize = cv.resize(img, (400,400))
imshow('Resize', resize)

#crop
crop = img[00:200, 200:400]
imshow('Cropped', crop)

cv.waitKey(0)