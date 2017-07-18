import cv2 

im = cv2.imread('balls.jpg', 0)

cv2.imshow("Balls", im)    
k = cv2.waitKey(0)

if k == 27:
    cv2.destroyAllWindows()
elif k == ord('s'):
    cv2.imwrite('balls_g.png', im)

