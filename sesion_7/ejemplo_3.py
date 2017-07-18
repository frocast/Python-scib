
import numpy as np
import cv2

im = cv2.imread("balls.jpg", 1)
h, w, c = im.shape

x1 = int(0.20*w)
y1 = int(0.85*h)

x2 = int(0.75*w)
y2 = int(0.35*h)

#print x1, y1, x2, y2

cv2.line(im, (x1, y1), (x2, y2), (0,0,255), 32)
cv2.imwrite("lineball.png", im)