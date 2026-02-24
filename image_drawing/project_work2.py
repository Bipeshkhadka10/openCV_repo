import cv2

file_path = input("enter the file path: ")
try:
    image = cv2.imread(file_path)
    if image is not None:
        choice = input("enter what u want to draw 'line','circle','rectangle','text': ")
        match choice:
            case 'line':
                pt1 = tuple(map(int,input("enter the start point: ").split()))
                pt2 = tuple(map(int,input("enter the end point: ").split()))
                cv2.line(image,pt1,pt2,color=(255,0,167),thickness=3)
                cv2.imshow("line_draw",image)
                cv2.waitKey(0)
                cv2.destroyAllWindows()
            case 'rectangle':
                pt1 = tuple(map(int,input("enter the start point of rectangle: ").split()))
                pt2 = tuple(map(int,input("enter the end point of rectangle: ").split()))
                cv2.rectangle(image,pt1,pt2,color=(255,0,167),thickness=3)
                cv2.imshow("rectangle_draw",image)
                cv2.waitKey(0)
                cv2.destroyAllWindows()
            case 'circle':
                center = tuple(map(int,input("enter the center point (x,y) of circle: ").split()))
                radius = int(input("enter the radius of circle: "))
                cv2.circle(image,center,radius,color=(255,0,167),thickness=3)
                cv2.imshow("circle_draw",image)
                cv2.waitKey(0)
                cv2.destroyAllWindows() 
            case 'text':
                text = input("enter the text you want to add: ")
                point = tuple(map(int,input("enter the point where you want to add text: ").split()))
                scale = float(input("enter scale value: "))
                cv2.putText(image,text,point,cv2.FONT_HERSHEY_COMPLEX_SMALL,scale,color=(255,0,167),thickness=3)
                cv2.imshow("circle_draw",image)
                cv2.waitKey(0)
                cv2.destroyAllWindows() 
            case _:
                print("invalid choice") 
    else:
        print("failed to load image")

except ValueError:
    print("failed to load image invalid file path")