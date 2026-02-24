import cv2
image = cv2.imread("human.webp")

if image is None:
    print("could not found image")
else:
    cropped_image = image[50:400, 50:200]
    cv2.imshow("original_img",image)
    cv2.imshow("cropped_img",cropped_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
