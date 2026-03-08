import cv2 as cv

img = cv.imread('photos/ironman.jpg')

rimg = cv.resize(img, (1500,750), interpolation=cv.INTER_CUBIC)
cv.imshow('ironman resize', rimg)






gray = cv.cvtColor(rimg, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

hsv = cv.cvtColor(rimg, cv.COLOR_BGR2HSV)
cv.imshow('HSV', hsv)

lab = cv.cvtColor(rimg, cv.COLOR_BGR2LAB)
cv.imshow('LAB', lab)



cv.waitKey(0)