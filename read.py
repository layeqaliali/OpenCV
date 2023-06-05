import cv2 as cv

img = cv.imread('image/person.jpg')
cv.imshow('Image', img)

#capture = cv.VideoCapture(0) Web camera
capture = cv.VideoCapture('video/vid.mp4')
while True:
    isTrue, frame = capture.read()
    cv.imshow('Video', frame)

    if cv.waitKey(20) & 0xFF == ord('d'):
        break
capture.release()
cv.destroyAllWindows()
