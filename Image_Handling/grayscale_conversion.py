import cv2
image = cv2.imread("image.jpeg")

if image is not None:
    gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY) 
    if gray is not None:
        cv2.imshow("gray_image",gray)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        print("successfully converted to gray image")
    else:
        print("error on converting to gray")
else:
    print("error in loading image")