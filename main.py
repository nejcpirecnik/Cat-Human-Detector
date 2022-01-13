import cv2

face_Cascade_cat = cv2.CascadeClassifier("cat.xml")
face_Cascade_human = cv2.CascadeClassifier("human.xml")

image = cv2.imread('Photos/ch5.jpg')
imgGray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

faces_cats = face_Cascade_cat.detectMultiScale(imgGray, 1.1, 4)
faces_humans = face_Cascade_human.detectMultiScale(imgGray, 1.1, 4)

for (x, y, w, h) in faces_cats:
  cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 2)
  cv2.putText(image, "Macka".format(1), (x, y - 10),
              cv2.FONT_HERSHEY_DUPLEX, 1, (0, 0, 255), 2)

for (x, y, w, h) in faces_humans:
  cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 2)
  cv2.putText(image, "Clovek".format(1), (x, y - 10),
              cv2.FONT_HERSHEY_DUPLEX, 1, (255, 0, 0), 2)

cv2.imshow("Rezultat", image)
cv2.waitKey(0)