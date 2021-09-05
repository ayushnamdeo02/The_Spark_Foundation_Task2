import easyocr
import cv2
from matplotlib import pyplot as plt
import numpy as np
from IPython.display import display, Image
#Image 1 before OCR
image_path= 'way.jpg'
im1 = cv2.imread('way.jpg')
plt.imshow(im1)
plt.show()
reader = easyocr.Reader(['en'],gpu=False)
result = reader.readtext(image_path)
#result
top_left = tuple(result[0][0][0])
bottom_right = tuple(result[0][0][2])
text = result[0][1]
font = cv2.LINE_AA
#Image 1 after OCR
img = cv2.imread(image_path)
img = cv2.rectangle(img,top_left,bottom_right,(0,255,0),35)
img = cv2.putText(img,text,top_left, font, 2,(255,0,0),10,cv2.LINE_AA)
plt.figure(figsize=(7,7))
plt.imshow(img)
plt.show()
#Image 2 before OCR
image_path2='garbage.png'
im2 = cv2.imread('garbage.png')
plt.imshow(im2)
plt.show()

reader = easyocr.Reader(['en'],gpu=False)
result = reader.readtext(image_path2)
#result
#Image 2 after OCR
img = cv2.imread(image_path2)
for detection in result: 
    top_left = tuple([int(val) for val in detection[0][0]])
    bottom_right = tuple([int(val) for val in detection[0][2]])
    text = detection[1]
    font = cv2.FONT_HERSHEY_SIMPLEX
    img = cv2.rectangle(img,top_left,bottom_right,(0,255,0),5)
    img = cv2.putText(img,text,top_left, font, 2,(0,0,204),2,cv2.LINE_AA)

plt.figure(figsize=(10,10))
plt.imshow(img)
plt.show()
#Image 3 before OCR
image_path3='Yugen.jpg'
im3 = cv2.imread('Yugen.jpg')
plt.imshow(im3)
plt.show()
reader = easyocr.Reader(['en'],gpu=False)
result = reader.readtext(image_path3)
#result
#Image 3 after OCR
img = cv2.imread(image_path3)
for detection in result: 
    top_left = tuple([int(val) for val in detection[0][0]])
    bottom_right = tuple([int(val) for val in detection[0][2]])
    text = detection[1]
    font = cv2.FONT_HERSHEY_SIMPLEX
    img = cv2.rectangle(img,top_left,bottom_right,(102,255,102),2)
    img = cv2.putText(img,text,top_left, font, 0.8,(204,0,0),2,cv2.LINE_AA)

plt.figure(figsize=(15,15))
plt.imshow(img)
plt.show()
#Image 4 before OCR
image_path4='kenopsia.jpg'
im4 = cv2.imread('kenopsia.jpg')
plt.imshow(im4)
plt.show()

reader = easyocr.Reader(['en'],gpu=False)
result = reader.readtext(image_path4)
#result
#Image 4 after OCR 
img = cv2.imread(image_path4)
for detection in result: 
    top_left = tuple([int(val) for val in detection[0][0]])
    bottom_right = tuple([int(val) for val in detection[0][2]])
    text = detection[1]
    font = cv2.FONT_HERSHEY_SIMPLEX
    img = cv2.rectangle(img,top_left,bottom_right,(102,255,102),2)
    img = cv2.putText(img,text,top_left, font, 0.8,(255,0,127),2,cv2.LINE_AA)

plt.figure(figsize=(15,15))
plt.imshow(img)
plt.show()
#Image 5 before OCR
image_path5='fox3.jpg'
im5 = cv2.imread('fox3.jpg')
plt.imshow(im5)
plt.show()
reader = easyocr.Reader(['en'],gpu=False)
result = reader.readtext(image_path5)
#result
#Image 5 after OCR 
img = cv2.imread(image_path5)
for detection in result: 
    top_left = tuple([int(val) for val in detection[0][0]])
    bottom_right = tuple([int(val) for val in detection[0][2]])
    text = detection[1]
    font = cv2.FONT_HERSHEY_SIMPLEX
    img = cv2.rectangle(img,top_left,bottom_right,(0,255,0),1)
    img = cv2.putText(img,text,top_left, font, 0.5,(255,0,0),1,cv2.LINE_AA)

plt.figure(figsize=(10,10))
plt.imshow(img)
plt.show()
#Image 6 before OCR
image_path6='hand15.jpg'
im6 = cv2.imread('hand15.jpg')
plt.imshow(im6)
plt.show()
reader = easyocr.Reader(['en'],gpu=False)
result = reader.readtext(image_path6)
#result
#Image 6 after OCR
img = cv2.imread(image_path6)
for detection in result: 
    top_left = tuple([int(val) for val in detection[0][0]])
    bottom_right = tuple([int(val) for val in detection[0][2]])
    text = detection[1]
    font = cv2.FONT_HERSHEY_SIMPLEX
    img = cv2.rectangle(img,top_left,bottom_right,(0,255,1),5)
    img = cv2.putText(img,text,top_left, font,5,(255,0,0),5,cv2.LINE_AA)

plt.figure(figsize=(10,10))
plt.imshow(img)
plt.show()