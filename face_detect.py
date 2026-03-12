import cv2 as cv

img = cv.imread('photos/man1.jpg')
rimg = cv.resize(img, (500, 500))


if rimg is None:
    print("Image not found")
    exit()

gray = cv.cvtColor(rimg, cv.COLOR_BGR2GRAY)

haar_cascade = cv.CascadeClassifier(cv.data.haarcascades + 'haarcascade_frontalface_default.xml')

faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=1)

print(f'Number of faces found = {len(faces_rect)}')

for (x,y,w,h) in faces_rect:
    cv.rectangle(rimg,(x,y),(x+w,y+h),(0,255,0),2)

cv.imshow('Detected Face', rimg)

cv.waitKey(0)
cv.destroyAllWindows()