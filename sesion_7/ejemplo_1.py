import cv2 

im = cv2.imread('balls.jpg', 0)
cv2.imshow("Balls", im)
cv2.imwrite('balls_g.png', im)
cv2.waitKey(0)
cv2.destroyAllWindows()