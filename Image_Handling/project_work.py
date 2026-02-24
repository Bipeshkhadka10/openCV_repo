import cv2
image_path = input("Enter the image path u want to load:")
try:
    image = cv2.imread(image_path)

    if image is not None:
        h,w,c = image.shape
        print(f"About Image: \nHeight:{h} \nWidth:{w} \nChannel:{c}")
        res = input("Do u want to convert image into grayscale 'y'\'n':")
        if res == 'y':
            gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
            print("Image converted to gray scale")
            ask = input("Do u want to show or save grascale image  'show'\'save':")
            if ask == "show":
                title = input("Give title for the image to show :")
                cv2.imshow(title,gray)
                cv2.waitKey(0)
                cv2.destroyAllWindows() 
                print("successfully shown  image")
            elif ask == "save":
                Img_name = input("Enter the file name:")
                cv2.imwrite(Img_name+".jpeg",gray)
                print("Image saved successfully")
        elif res == 'n':
            Img_name = input("Enter the file name:")
            cv2.imwrite(Img_name+".jpeg",image)
            print("Image saved successfully")
except ValueError:
    print("Error in the path of image")

