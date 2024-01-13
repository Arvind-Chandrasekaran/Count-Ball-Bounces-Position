import cv2 as cv
import numpy as np 

cap = cv.VideoCapture(0)
ret,frame = cap.read()



while ret:

        hsv_frame = cv.cvtColor(frame,cv.COLOR_BGR2HSV)


        skin = cv.inRange(hsv_frame,(0, 10, 60), (20, 150, 255))	#HSV range from skin
        cv.imshow("mask skin",skin)

        not_skin= cv.bitwise_not(skin)			
        cv.imshow("masked not skin",not_skin)

        masked = cv.bitwise_and(frame,frame,mask = not_skin)
        cv.imshow("masked not skin",masked)

       


        ret,frame = cap.read()

        if cv.waitKey(1) & 0xFF == ord('q'):
                break
        

cap.release()
cv.destroyAllWindows()
