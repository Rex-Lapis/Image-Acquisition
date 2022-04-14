import numpy as np
import cv2

cap = cv2.VideoCapture(0)        #'0'选择笔记本电脑自带参数，‘1’为USB外置摄像头
print(cap.get(3), cap.get(4))    #查看当前捕获视频的尺寸，默认为640*480
cap.set(propId=3, value=320)     #设置你想捕获的视频的宽度
cap.set(propId=4, value=240)     #设置你想捕获的视频的高度
print(cap.get(3), cap.get(4))    #验证是否设置成功
while (True):
    ret, frame = cap.read()      #读取图像并显示
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()                    #按‘q’键退出后，释放摄像头资源
cv2.destroyAllWindows()
