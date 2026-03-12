import cv2 as cv
import numpy as np

capture = cv.VideoCapture(0)

while True:
    isTrue, frame = capture.read()

    if not isTrue:
        print("Camera not found")
        break

    blur = cv.GaussianBlur(frame, (5,5), 0)

    gray = cv.cvtColor(blur, cv.COLOR_BGR2GRAY)

    edges = cv.Canny(gray, 50, 150)

    contours, _ = cv.findContours(edges, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

    for contour in contours:

        area = cv.contourArea(contour)

        if area < 500:
            continue

        peri = cv.arcLength(contour, True)

        approx = cv.approxPolyDP(contour, 0.04 * peri, True)

        vertices = len(approx)

        if vertices == 3:
            shape = "Triangle"

        elif vertices == 4:
            shape = "Rectangle"

        elif vertices == 5:
            shape = "Pentagon"

        else:
            shape = "Circle"

        x, y, w, h = cv.boundingRect(contour)

        cv.rectangle(frame, (x,y), (x+w,y+h), (0,255,0), 2)

        cv.putText(frame,
                   shape,
                   (x, y-10),
                   cv.FONT_HERSHEY_SIMPLEX,
                   0.6,
                   (0,255,0),
                   2)

    cv.imshow('Webcam', frame)

    if cv.waitKey(20) & 0xFF == ord('d'):
        break

capture.release()
cv.destroyAllWindows()

#Webcam Frame->Blur->Grayscale->Edge Detection->Contours->Polygon Approximation->Count Vertices->Classify Shape->Draw Box + Label
#calculte area of contour and ignore small areas
#calculate perimeter of contour and apply polygon approximation
#count vertices of approximated contour and classify shape
#and then identify the shape based on number of sides and draw a bounding box around the shape and label it on the webcam feed
