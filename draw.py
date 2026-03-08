import cv2 as cv
import numpy as np

blank = np.zeros((500,500,3), dtype = 'uint8')
cv.imshow('Blank', blank)

blank[:] = 0,255,0
cv.imshow('Green', blank)

blank[200:300,200:300] = 0,255,0
cv.imshow('Green', blank)

final = np.zeros((500,500,3), dtype = 'uint8')

cv.rectangle(blank, (0,0), (250,250), (255,0,0), thickness = cv.FILLED)
cv.imshow('Rectangle', blank)

cv.circle(blank, (250,250), 100, (0,0,255), thickness = cv.FILLED)
cv.imshow('Circle', blank)


cv.line(blank, (0,0), (500,500), (255,255,255), thickness = 3)
cv.imshow('Line', blank)

cv.putText(blank, 'Hello World', (250,250), cv.FONT_HERSHEY_TRIPLEX, 1.0, (255,255,255), thickness = 2)
cv.imshow('Text', blank)

cv.putText(final, 'Hello World', (250,250), cv.FONT_HERSHEY_TRIPLEX, 1.0, (255,255,255), thickness = 2)
cv.imshow('Text', final)


img = cv.imread('photos/griffin_logo.png')
cv.imshow('Griffin Logo', img)
cv.waitKey(0)