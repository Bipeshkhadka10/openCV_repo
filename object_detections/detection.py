import cv2
import numpy as np

face_cascade = cv2.CascadeClassifier(
"object_detections/haarcascade_frontalface_default.xml")

eye_cascade = cv2.CascadeClassifier(
"object_detections/haarcascade_eye.xml")

smile_cascade = cv2.CascadeClassifier(
"object_detections/haarcascade_smile.xml")


cap = cv2.VideoCapture(0)

while True:

    success, frame = cap.read()

    if not success:
        print("Cannot read frame")
        break

    frame = cv2.flip(frame, 1)

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    for (x,y,w,h) in faces:

        # Face rectangle
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,255),2)

        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]

        # Eye detection
        eyes = eye_cascade.detectMultiScale(roi_gray,1.7,20)

        if len(eyes) > 0:

            cv2.putText(frame,
                        "Eyes Open",
                        (x,y-10),
                        cv2.FONT_HERSHEY_COMPLEX_SMALL,
                        1,
                        (0,255,0),
                        2)
        else:

            cv2.putText(frame,
                        "Eyes Closed",
                        (x,y-10),
                        cv2.FONT_HERSHEY_COMPLEX_SMALL,
                        1,
                        (0,0,255),
                        2)


        # Smile detection
        smiles = smile_cascade.detectMultiScale(roi_gray,1.7,10)

        if len(smiles) > 0:

            cv2.putText(frame,
                        "Smiling 😊",
                        (x,y+h+30),
                        cv2.FONT_HERSHEY_COMPLEX_SMALL,
                        1,
                        (255,255,0),
                        2)
        else:

            cv2.putText(frame,
                        "Not Smiling",
                        (x,y+h+30),
                        cv2.FONT_HERSHEY_COMPLEX_SMALL,
                        1,
                        (255,0,0),
                        2)


        # Face label
        cv2.putText(frame,
                    "Face Detected",
                    (x,y+h+60),
                    cv2.FONT_HERSHEY_COMPLEX_SMALL,
                    1,
                    (0,255,255),
                    2)


    cv2.imshow("Smart Face Detection System", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        print("Quitting...")
        break


cap.release()

cv2.destroyAllWindows()