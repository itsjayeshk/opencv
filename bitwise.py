import cv2 as cv
import numpy as np

# Create a blank black image
blank = np.zeros((400, 400), dtype='uint8')

# Draw shapes
rectangle = cv.rectangle(blank.copy(), (30, 30), (370, 370), 255, -1)
circle = cv.circle(blank.copy(), (200, 200), 150, 255, -1)

# Show original shapes
cv.imshow('Rectangle', rectangle)
cv.imshow('Circle', circle)

# Bitwise AND (intersection)
bitwise_and = cv.bitwise_and(rectangle, circle)
cv.imshow('Bitwise AND', bitwise_and)

# Bitwise OR (union)
bitwise_or = cv.bitwise_or(rectangle, circle)
cv.imshow('Bitwise OR', bitwise_or)

# Bitwise XOR (non-overlapping parts)
bitwise_xor = cv.bitwise_xor(rectangle, circle)
cv.imshow('Bitwise XOR', bitwise_xor)

# Bitwise NOT (invert)
bitwise_not = cv.bitwise_not(rectangle)
cv.imshow('Bitwise NOT (Rectangle)', bitwise_not)

# Wait for key press before closing
cv.waitKey(0)
cv.destroyAllWindows()