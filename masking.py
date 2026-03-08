import cv2 as cv
import numpy as np


img = cv.imread('photos/ironman.jpg')
rimg = cv.resize(img, (1500,750), interpolation=cv.INTER_CUBIC)
cv.imshow('ironman resize', rimg)

blank = np.zeros(rimg.shape[:2], dtype='uint8')
cv.imshow('Blank', blank)

mask = cv.rectangle(blank.copy(), (rimg.shape[1]//2, rimg.shape[0]//2 + 45), (rimg.shape[1]//2 + 250, rimg.shape[0]//2 + 45 + 250), 255, -1)
cv.imshow('Mask', mask)

masked = cv.bitwise_and(rimg, rimg, mask=mask)
cv.imshow('Masked Image', masked)

circle_mask = cv.circle(blank.copy(), (rimg.shape[1]//2, rimg.shape[0]//2 + 45), 125, 255, -1)
cv.imshow('Circle Mask', circle_mask)
cv.waitKey(0)