import cv2
image = cv2.imread("image.jpeg")
if image is None:
    print("Error: falied to read image")
else:
    print("successfully image read")