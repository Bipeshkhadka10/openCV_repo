import cv2
image = cv2.imread("image.jpeg")

if image is not None:
    cv2.imshow("Air_wirte_logo",image) # to create window to display image
    cv2.waitKey(0) # to hold the image displaying
    cv2.destroyAllWindows() #to close the image window
else:
    print("Error: failed to load image")
