import cv2 as cv
from cv2 import rectangle
import numpy as np

blank = np.zeros((400,400), dtype='uint8')

circle = cv.circle(blank.copy(), (200, 200), 200, 255, -1)
rectangle = cv.rectangle(blank.copy(), (30,30), (370,370), 255, -1)

cv.imshow('Circle', circle)
cv.imshow('Rectangle', rectangle)

bitwise = cv.bitwise_and(circle, rectangle)
cv.imshow('AND', bitwise)

bitwise_or = cv.bitwise_or(circle, rectangle)
cv.imshow('OR', bitwise_or)

bitwise_xor = cv.bitwise_xor(circle, rectangle)
cv.imshow('XOR', bitwise_xor)

bitwise_Nor = cv.bitwise_not(rectangle)
cv.imshow('NOT', bitwise_Nor)

cv.waitKey(0)