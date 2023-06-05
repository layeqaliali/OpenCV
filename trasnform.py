from pickle import NONE
from turtle import width
import cv2 as cv
import numpy as np

img = cv.imread('image/person.jpg')
cv.imshow('Image', img)

def translate(img, x, y):
    transMat = np.float32([[1,0,x],[0,1,y]])
    dimensions = (img.shape[1], img.shape[0])
    return cv.warpAffine(img, transMat,dimensions)

# -x --- left
# y --- up
# x --- right
# -y --- down

#translated = translate(img, -100, 100)
#cv.imshow('Tranform', translated)

#Rotate image
def rotate(img, angle, rotPoint = None):
    (height,width) = img.shape[:2]

    if rotPoint is None:
        rotPoint = (width//2, height//2)

    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
    dimension = (width, height)

    return cv.warpAffine(img, rotMat, dimension)

rotated = rotate(img, 65)
cv.imshow('Rotated', rotated)

rotated_image = rotate(rotated, -65)
cv.imshow('Rotated image', rotated_image)

#flipping
flip = cv.flip(img, -1)
cv.imshow('Flip', flip)

cv.waitKey(0)