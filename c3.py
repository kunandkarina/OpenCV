import cv2
import numpy as np

kernel = np.ones((3,3), np.uint8)
kernel1 = np.ones((5,5), np.uint8)

img = cv2.imread('bp.png')
img = cv2.resize(img, (0,0), fx=0.5, fy=0.5)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)    #轉成灰階圖片
blur = cv2.GaussianBlur(img, (15,15), 20)       #轉成模糊
canny = cv2.Canny(img, 150, 200)                #轉成邊緣
dilate = cv2.dilate(img, kernel, iterations=1)  #膨脹線條
erode = cv2.erode(img, kernel1, iterations=1)   #侵蝕線條


cv2.imshow('bp', img)
cv2.imshow('gray', gray)
cv2.imshow('blur', blur)
cv2.imshow('canny', canny)
cv2.imshow('dilate', dilate)
cv2.imshow('erode', erode)

cv2.waitKey(0)