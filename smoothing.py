import cv2 as cv

img = cv.imread('photos/ironman.jpg')
rimg = cv.resize(img, (1500,750), interpolation=cv.INTER_CUBIC)
cv.imshow('ironman resize', rimg)

average = cv.blur(rimg, (7,7))
cv.imshow('Average Blur', average)

gauss = cv.GaussianBlur(rimg, (7,7), 0)
cv.imshow('Gaussian Blur', gauss)

median = cv.medianBlur(rimg, 7)
cv.imshow('Median Blur', median)

bilateral = cv.bilateralFilter(rimg, 7, 75, 75)
cv.imshow('Bilateral Blur', bilateral)

cv.waitKey(0)

