import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

img = cv.imread('photos/ironman.jpg')

rimg = cv.resize(img, (1500,750), interpolation=cv.INTER_CUBIC)
cv.imshow('Ironman Resize', rimg)

blank = np.zeros(rimg.shape[:2], dtype='uint8')

gray = cv.cvtColor(rimg, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

mask = cv.circle(blank, (rimg.shape[1]//2, rimg.shape[0]//2), 100, 255, -1)

masked = cv.bitwise_and(rimg, rimg, mask=mask)
cv.imshow('Mask', masked)

# Grayscale histogram
gray_hist = cv.calcHist([gray], [0], mask, [256], [0,256])

plt.figure()
plt.title('Grayscale Histogram')
plt.xlabel('Bins')
plt.ylabel('# of pixels')
plt.plot(gray_hist)
plt.xlim([0,256])
plt.show()

# Colour histogram
plt.figure()
plt.title('Colour Histogram')
plt.xlabel('Bins')
plt.ylabel('# of pixels')

colors = ('b', 'g', 'r')

for i, col in enumerate(colors):
    hist = cv.calcHist([rimg], [i], mask, [256], [0,256])
    plt.plot(hist, color=col)
    plt.xlim([0,256])

plt.show()

cv.waitKey(0)
cv.destroyAllWindows()