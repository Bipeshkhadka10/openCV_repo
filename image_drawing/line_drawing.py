import cv2
image = cv2.imread("human.webp")

if image is None:
    print("could not found image")
else:
    cv2.line(image,(50,230),(400,230),(0,255,0),3)  
    cv2.line(image,(50,50),(400,50),(0,255,0),3)
    cv2.line(image,(50,50),(50,230),(0,255,0),3)
    cv2.line(image,(400,50),(400,230),(0,255,0),3)
    cv2.rectangle(image,(40,40),(410,240),(125,255,165),3)# drawing rectangle
    cv2.imshow("line drawn", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()