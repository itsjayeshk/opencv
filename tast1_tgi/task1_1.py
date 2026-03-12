import cv2 as cv
import numpy as np
capture = cv.VideoCapture(0)
while True:
    isTrue, frame = capture.read()
    if not isTrue:
        print("Camera not found")
        break
    if isTrue:
        cv.imshow('Webcam', frame)
        if cv.waitKey(20) & 0xFF == ord('d'):
            break
    else:
        break
capture.release()
cv.destroyAllWindows()
    
