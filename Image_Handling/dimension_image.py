import cv2
image = cv2.imread("image.jpeg")

if image is not None:
    h , w, c = image.shape # returns height, width, channel of image
    print(f"image dimension: \nHeight:{h} \nWidth:{w} \nChannel:{c}  ")
else:
    print("failed to load the image")
