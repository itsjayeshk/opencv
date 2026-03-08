import cv2 as cv

img = cv.imread('photos/griffin_logo.png')

cv.imshow('Griffin Logo', img)
cv.waitKey(0)

capture = cv.VideoCapture('videos/Griffin.mp4')
while True:
    isTrue, frame = capture.read()

    if isTrue:
        cv.imshow('Video', frame)

        if cv.waitKey(20) & 0xFF == ord('d'):
            break
    else:
        break
capture.release()
cv.destroyAllWindows()
