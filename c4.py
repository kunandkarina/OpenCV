import cv2
import numpy as np

img = np.zeros((550,600,3), np.uint8)
# 畫直線
cv2.line(img, (2,2), (300,450), (0,255,255), 1 ) 
cv2.line(img, (2,2), (img.shape[0], img.shape[1]), (0,255,0), 1 )
cv2.line(img, (2,2), (img.shape[1], img.shape[0]), (140,255,190), 1 )

#畫矩形
cv2.rectangle(img, (0,0), (200,350), (50,50,50), 2)
cv2.rectangle(img, (300,480), (400,500), (180,40,200), cv2.FILLED)   # 填滿矩形

#畫圓形
cv2.circle(img, (500,130), (30), (123,231,90),2)

#寫文字
cv2.putText(img, 'Jisoo', (480, 200), cv2.FONT_HERSHEY_PLAIN, 2, (40,99,166), 1)      # 不支援中文

cv2.imshow('img', img)
cv2.waitKey(0)