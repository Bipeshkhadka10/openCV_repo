import cv2
image = cv2.imread("Bipesh.jpeg")

if image is None:
    print("could not found image")
else:
    print('Image loaded succesfully')
    center =(500//2 , 333//2)
    radius = 130
    thickness = 3
    cv2.circle(image,center,radius,(255,0,0),thickness)
    cv2.imshow('circle_draw',image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()