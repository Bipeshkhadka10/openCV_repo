import cv2

image = cv2.imread("bip3.jpeg")
image = cv2.resize(image,(560,550))
gaussian_blur = cv2.GaussianBlur(image,(3,3),4)
cv2.imshow("original_image",image)
cv2.imshow("filtered_image",gaussian_blur)
cv2.waitKey(0)
cv2.destroyAllWindows()