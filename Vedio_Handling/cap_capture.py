import cv2

cap = cv2.VideoCapture(0)  # capture video from laptop camera

while True:
    ret, frame = cap.read()

    if not ret:
        print("Could not read image")
        break
    flipped_frame = cv2.flip(frame,1)
    cv2.imshow("Camera",flipped_frame)  # show the frame

    if cv2.waitKey(1) & 0xFF == ord('q'):
        print("Quitting.....")
        break

cap.release()  # release AFTER loop
cv2.destroyAllWindows()