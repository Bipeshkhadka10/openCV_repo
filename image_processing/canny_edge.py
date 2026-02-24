import cv2
image = cv2.imread("bip3.jpeg",cv2.IMREAD_GRAYSCALE)
image = cv2.resize(image,(560,550))
edged = cv2.Canny(image , 50 ,150)
cv2.imshow("orignial",image)
cv2.imshow("canny",edged)
cv2.waitKey(0)
cv2.destroyAllWindows()