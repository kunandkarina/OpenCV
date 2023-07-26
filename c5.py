import cv2
import numpy as np

def empty(v):
    pass


img = cv2.imread('cartoon.jpg')
img = cv2.resize(img, (0,0), fx=0.5, fy=0.5)

cv2.namedWindow('TrackBar')                 # 創建視窗函式
cv2.resizeWindow('TrackBar', 640, 320)      # (視窗名稱, 寬度, 高度)

#製作控制條
cv2.createTrackbar('Hue min', 'TrackBar', 0, 179, empty)    
cv2.createTrackbar('Hue Max', 'TrackBar', 179, 179, empty)
cv2.createTrackbar('Sat min', 'TrackBar', 0, 255, empty)
cv2.createTrackbar('Sat Max', 'TrackBar', 255, 255, empty)
cv2.createTrackbar('Val min', 'TrackBar', 0, 255, empty)
cv2.createTrackbar('Val Max', 'TrackBar', 255, 255, empty)

hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)  # hsv圖檔另一種格式

while True:
    #取得控制條的值
    h_min = cv2.getTrackbarPos('Hue min', 'TrackBar')       
    h_Max = cv2.getTrackbarPos('Hue Max', 'TrackBar')
    S_min = cv2.getTrackbarPos('Sat min', 'TrackBar')
    S_Max = cv2.getTrackbarPos('Sat Max', 'TrackBar')
    V_min = cv2.getTrackbarPos('Val min', 'TrackBar')
    V_Max = cv2.getTrackbarPos('Val Max', 'TrackBar')
    print(h_min, h_Max, S_min, S_Max, V_min, V_Max)

    lower = np.array([h_min, S_min, V_min])
    upper = np.array([h_Max, S_Max, V_Max])

    mask = cv2.inRange(hsv, lower, upper)
    res = cv2.bitwise_and(img, img, mask=mask)

    cv2.imshow('img', img)
    cv2.imshow('hsv', hsv)
    cv2.imshow('mask', mask)
    cv2.imshow('res', res)

    cv2.waitKey(1)


