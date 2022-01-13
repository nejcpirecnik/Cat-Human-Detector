
## Cat&Human Detector

**Cat&Human Detector** is a Python script that recognizes human and cat faces from an imported image.
##### It uses a ```opencv-python``` library. 
####
##### OpenCV is a library of Python bindings designed to solve computer vision problems. 
##### It makes use of ```Numpy```, which is a highly optimized library for numerical operations with a MATLAB-style syntax.

### How does it work?
##### This is a complete code breakdown.
####
```python
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
```
### Explained by sections
```import cv2``` Imports the OpenCV Python Library.

```
face_Cascade_cat = cv2.CascadeClassifier("cat.xml") 
face_Cascade_human = cv2.CascadeClassifier("human.xml")
```
It uses [Haar Cascade files](https://towardsdatascience.com/face-detection-with-haar-cascade-727f68dafd08) which include trained data to detect cat and human faces. ```cat.xml``` and ```human.xml``` both include seperate data.

```
image = cv2.imread('Photos/ch5.jpg')
imgGray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
```
In this section you must provide the path to your image. You do that by replacing the default image called ```Photos/ch5.jpg```. 
###### I've also provided a couple of example photos of humans and cats.
The second line converts the imported image into *grayscale*.

```
faces_cats = face_Cascade_cat.detectMultiScale(imgGray, 1.1, 4)
faces_humans = face_Cascade_human.detectMultiScale(imgGray, 1.1, 4)
```
In this section we use a function called ```detectMultiScale```, and assign it to a variable. Using that, we can detect both small and large faces.
```python
for (x, y, w, h) in faces_cats:
  cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 2)
  cv2.putText(image, "Macka".format(1), (x, y - 10),
              cv2.FONT_HERSHEY_DUPLEX, 1, (0, 0, 255), 2)

for (x, y, w, h) in faces_humans:
  cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 2)
  cv2.putText(image, "Clovek".format(1), (x, y - 10),
              cv2.FONT_HERSHEY_DUPLEX, 1, (255, 0, 0), 2)
```
We run 2 loops. Both are very similar, the only difference is that one's for the cat and the other is for the human. We draw a rectangle around both faces and set its color, aswell as write the coresponding text above both rectangles. We can detect as many faces as we'd like.
