import cv2 as cv
from cv2 import imshow
import numpy as np

blank = np.zeros((500,500,3), dtype= 'uint8')
cv.imshow('Image', blank)

blank [:] = 0,0,255
#cv.imshow('Color', blank)

#Draw Square
blank[200:300, 300:400] = 0,0,255
#cv.imshow('Image', blank)

#Draw rectangle
cv.rectangle(blank, (0,0),(250,500),(255,0,255), thickness=cv.FILLED)
#cv.imshow('Blank', blank)

#Draw Circle
cv.circle(blank, (250,250), 40, (0,0,255), thickness=cv.FILLED)
#cv.imshow('Circle', blank)

#draw line
cv.line(blank, (250,250), (0,400), (255,255,255), thickness=3)
#cv.imshow('Line', blank)

#Draw Text
cv.putText(blank, 'Hello', (250,250), cv.FONT_HERSHEY_DUPLEX, 3.0, (255,255,255), thickness=2)
cv.imshow('TEXT', blank)

cv.waitKey(0)