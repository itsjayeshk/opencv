import cv2 as cv
import numpy as np

img = cv.imread('photos/ironman.jpg')

if img is None:
    print("Image not found")
    exit()

rimg = cv.resize(img, (1500,750), interpolation=cv.INTER_CUBIC)

cv.imshow('Resized', rimg)

blank = np.zeros(rimg.shape[:2], dtype='uint8')

b,g,r = cv.split(rimg)

blue = cv.merge([b, blank, blank])
green = cv.merge([blank, g, blank])
red = cv.merge([blank, blank, r])

cv.imshow('Blue', blue)
cv.imshow('Green', green)
cv.imshow('Red', red)

merged = cv.merge([b,g,r])
cv.imshow('Merged', merged)

print("Image shape:", rimg.shape)
print("Blue channel shape:", b.shape)

cv.waitKey(0)