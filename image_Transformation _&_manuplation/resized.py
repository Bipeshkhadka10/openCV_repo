import cv2
image = cv2.imread("human.webp")

if image is None:
    print("could not found image")
else:
    resized = cv2.resize(image,(300,200))
    cv2.imshow("original_image",image)
    cv2.imshow("resized_image",resized)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
