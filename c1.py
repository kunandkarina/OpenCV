import cv2

# 讀取圖片
img = cv2.imread('bp.png')

# img = cv2.resize(img, (700,300))
img = cv2.resize(img, (0,0), fx=0.5, fy=0.5)  # 用原本圖片的大小改變

cv2.imshow('Jisoo', img)
cv2.waitKey(0)

# 讀取影片
cap = cv2.VideoCapture('v1.mp4')
while True:
    ret , frame = cap.read()      # ret bool值, frame 下一偵的圖片
    if ret:
        frame = cv2.resize(frame, (0,0), fx=0.5, fy=0.5)
        cv2.imshow('test', frame)
    else:
        break
    if cv2.waitKey(1) == ord('q'):     #按下鍵盤上q的時候
        break

#讀取視訊鏡頭
cap = cv2.VideoCapture(0)   # 0是預設鏡頭編號
while True:
    ret , frame = cap.read()      
    if ret:
        frame = cv2.resize(frame, (0,0), fx=0.5, fy=0.5)
        cv2.imshow('test', frame)
    else:
        break
    if cv2.waitKey(1) == ord('q'):    
        break