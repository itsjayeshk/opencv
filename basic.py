import cv2 as cv

img = cv.imread('photos/griffin_logo.png')
cv.imshow('Griffin Logo', img)
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Griffin Logo Gray', gray)

blur = cv.GaussianBlur(img, (7,7), cv.BORDER_DEFAULT)
cv.imshow('Griffin Logo Blur', blur)

edge = cv.Canny(img, 125, 175)
cv.imshow('Griffin Logo Edge', edge)

dilated = cv.dilate(edge, (7,7), iterations=3)
cv.imshow('Griffin Logo Dilated', dilated)

eroded = cv.erode(dilated, (7,7), iterations=3)
cv.imshow('Griffin Logo Eroded', eroded)

resized = cv.resize(img, (500, 500), interpolation=cv.INTER_CUBIC)
cv.imshow('Griffin Logo Resized', resized)

cropped = img[50:200, 200:400]
cv.imshow('Griffin Logo Cropped', cropped)





cv.waitKey(0)