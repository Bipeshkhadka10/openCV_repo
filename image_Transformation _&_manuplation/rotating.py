import cv2
image = cv2.imread("human.webp")

if image is None:
    print("could not found image")
else:
    h,w,c = image.shape
    print(f"image info: \nHeight:{h} \nWidth:{w} \nChannel:{c}")
    formula = cv2.getRotationMatrix2D((333//2,500//2),90,2) #rotating by 90 anticlock and scale by 2
    rotated_img = cv2.warpAffine(image,formula,(300,400))
    flipped_img = cv2.flip(image,1) #flipped horizontal
    cv2.imshow("original_image",image)
    cv2.imshow("rotated_image",rotated_img)
    cv2.imshow("flipped_image",flipped_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()