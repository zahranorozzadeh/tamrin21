import cv2
import numpy as np

img = np.zeros((400, 400, 3), np.uint8)
alarm = True
m = img.shape[0]//8
n = img.shape[1]//8

for i in range(0, img.shape[0], m):
    for j in range(0, img.shape[1], n):
        if not alarm:
            img[i:i+m, j:j + n] = 255
            alarm = True
        else:
            img[i:i+m, j:j+n] = 0
            alarm = False
    if alarm:
        alarm = False
    else:
        alarm = True

cv2.imshow('norozzadeh1', img)
cv2.waitKey()