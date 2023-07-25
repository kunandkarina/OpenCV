import cv2
import numpy as np
import random

img = cv2.imread('bp.png')
print(img.shape)   # img的維度


# 做一張圖片出來
img = np.empty((300,300,3), np.uint8)    # unit => 正整數 , 8 => 2的次方
for row in range(300):
    for column in  range(300):
        img[row][column] = [random.randint(0,255),random.randint(0,255),random.randint(0,255)]
cv2.imshow('pic', img)
cv2.waitKey(0)

# 對原本圖片修改
img = cv2.imread('bp.png')
for row in range(150):
    for column in  range(img.shape[1]):      # shape[0] => img的長 , shape[1] => img的寬
        img[row][column] = [random.randint(0,255),random.randint(0,255),random.randint(0,255)]
cv2.imshow('pic', img)
cv2.waitKey(0)

#切割圖片
img = cv2.imread('bp.png')
newimg1 = img[:150, :300]     # img的長0~150,寬0~300
newimg2 = img[:300, 150:400]  # img的長0~300,寬150~400
cv2.imshow('img', img)
cv2.imshow('newimg1', newimg1)
cv2.imshow('newimg2', newimg2)
cv2.waitKey(0)