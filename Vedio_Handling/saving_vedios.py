import cv2

vedio = cv2.VideoCapture(0) # capturing video form own laptop\

frame_width = int(vedio.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(vedio.get(cv2.CAP_PROP_FRAME_HEIGHT))



print("enter 'r' to start recoding start and 'q' to quite")
codec = cv2.VideoWriter_fourcc(*'XVID')
recoding = cv2.VideoWriter("recorded_video.avi",codec,30,(frame_width,frame_height))
is_recoding = False
while True:
    success, frame = vedio.read() #reads vedio frams

    if not success:
        print("couldnot read vedio")
        break  
    cv2.imshow("recoding_video",frame)
    
    
    key_value = cv2.waitKey(1) & 0XFF
    if key_value == ord('r'):
        print("start recoding...")
        is_recoding = True

    if key_value == ord('s'):
        print("stop recoding...")
        is_recoding = False

    if is_recoding:
        recoding.write(frame)

    if key_value == ord('q'):
        print('Quiting...')
        break
vedio.release()
recoding.release()
cv2.destroyAllWindows()
