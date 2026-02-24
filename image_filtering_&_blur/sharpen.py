import cv2
import numpy as np
image = cv2.imread("gausssian.jpeg")
image = cv2.resize(image,(560,550))
kernel = np.array([[0,-1,0],[-1,5,-1],[0,-1,0]])
sharpen_image = cv2.filter2D(image,-1,kernel)
cv2.imshow("sharpen_image",sharpen_image)
cv2.imshow("original_image",image)
cv2.waitKey(0)
cv2.destroyAllWindows()