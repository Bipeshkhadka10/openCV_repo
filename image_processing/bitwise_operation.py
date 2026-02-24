import cv2
import numpy as np

img1 = np.zeros((300,300),dtype="uint8")
img2 = np.zeros((300,300),dtype="uint8")

cv2.circle(img1,(250,250),50,255,-1)
cv2.rectangle(img2,(100,100),(250,250),255,-1)
AND = cv2.bitwise_and(img1,img2) 
OR = cv2.bitwise_or(img1,img2) 
NOT = cv2.bitwise_not(img2) 
cv2.imshow('circle',img1)
cv2.imshow('rectangle',img2)
cv2.imshow('AND',AND)
cv2.imshow('OR',OR)
cv2.imshow('NOT',NOT)
cv2.waitKey(0)
cv2.destroyAllWindows()
