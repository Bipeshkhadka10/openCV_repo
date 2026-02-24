import cv2
image = cv2.imread("image.jpeg")

if image is not None:
    success = cv2.imwrite("logo_image.jpeg",image)
    if success:
        print("successfully saved the image")
    else:
        print("Error:failed to save the image")
else:
    print("Error: image cannot be loaded")