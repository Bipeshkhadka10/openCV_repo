import cv2
image = cv2.imread("Bipesh.jpeg")

if image is None:
    print("could not found image")
else:
    print('Image loaded succesfully')
    text ="Author: Bipesh khadka"
    cv2.putText(image,text,(80,50),cv2.FONT_HERSHEY_SCRIPT_COMPLEX,1.2,(0,255,195),2)
    cv2.imshow("text_added",image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()