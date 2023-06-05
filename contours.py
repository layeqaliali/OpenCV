import cv2 as cv

img = cv.imread('image/person.jpg')
cv.imshow('Image', img)

#grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

#Edges
#canny = cv.Canny(img, 125, 175)
#cv.imshow('Canny', canny)

#Blur
#blur = cv.GaussianBlur(canny, (5,5), cv.BORDER_DEFAULT)
#cv.imshow('BLUR', blur)

ret, thresh = cv.threshold(gray, 125, 255, cv.THRESH_BINARY)
cv.imshow('Thresh',thresh)

contours, hierarchies = cv.findContours(thresh, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
print(f'{len(contours)} contours found' )


cv.waitKey(0)