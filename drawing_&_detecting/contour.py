import cv2
import numpy as np

file_path = input("Provide the image path: ")

try:
    image = cv2.imread(file_path)

    if image is None:
        raise Exception("Image not found")

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # _,edges= cv2.threshold(gray, 120, 255, cv2.THRESH_BINARY)
    edges = cv2.Canny(gray, 120, 250)

    contours, hierarchy = cv2.findContours(edges, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    for contour in contours:

        approx = cv2.approxPolyDP(contour, 0.01 * cv2.arcLength(contour, True), True)

        corner = len(approx)

        if corner == 3:
            shape_name = "Triangle"

        elif corner == 4:
            shape_name = "Rectangle"

        elif corner == 5:
            shape_name = "Pentagon"

        elif corner > 5:
            shape_name = "Circle"

        else:
            shape_name = "Unknown"

        cv2.drawContours(image, [approx], 0, (0,255,0), 2)

        x = approx.ravel()[0]
        y = approx.ravel()[1] - 10

        cv2.putText(image, shape_name, (x,y),
                    cv2.FONT_HERSHEY_COMPLEX,
                    0.6, (0,0,255), 2)

    cv2.imshow("Contour", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

except Exception:
    print("Failed to load image from given path")