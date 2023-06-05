import cv2 as cv
from cv2 import circle
import numpy as np

img = cv.imread('image/person.jpg')
cv.imshow('Image', img)

blank = np.zeros(img.shape[:2], dtype='uint8')

circle = cv.circle(blank, (img.shape[1]//2, img.shape[0]//2+100), 100, 255, -1)
cv.imshow('Circle', circle)
rectangles = cv.rectangle(blank, (30,30),(370,370),255, -1)
cv.imshow('Rect', rectangles)

weird_shape = cv.bitwise_and(circle, rectangles)

masked = cv.bitwise_and(img, img, mask=rectangles)
cv.imshow('Mask', masked)

cv.waitKey(0)