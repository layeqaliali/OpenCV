import cv2 as cv

img = cv.imread('image/nature.jpg')
cv.imshow('Image', img)

b,g,r = cv.split(img)
cv.imshow('BLUE', b)
cv.imshow('Green', g)
cv.imshow('Red', r)

print(img.shape)
print(b.shape)
print(g.shape)
print(r.shape)

merge = cv.merge([b,g,r])
cv.imshow('Merge', merge)

cv.waitKey(0)