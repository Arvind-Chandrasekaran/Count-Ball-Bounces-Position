import cv2 as cv
import numpy as np 

cap = cv.VideoCapture('C:/yellow_ball.mp4')
ret,frame = cap.read()


bounce_count = 0
prev_center = None
while ret:

        hsv_frame = cv.cvtColor(frame,cv.COLOR_BGR2HSV)


        ball = cv.inRange(hsv_frame,(170,50,50), (180,255,255))
        cv.imshow("mask skin",ball)


        masked = cv.bitwise_and(frame,frame,mask = ball)
        cv.imshow("masked ball",masked)

        
        canny = cv.Canny(masked,125,175)
        cv.imshow("canny of ball",canny)


        contour, hier =   cv.findContours(canny,cv.RETR_EXTERNAL,cv.CHAIN_APPROX_SIMPLE)
        
    
        #Biggest sized object is the ball
        ball = max(contour, key=cv.contourArea)

        #Find the centre and radius of the ball
        (x, y), radius = cv.minEnclosingCircle(ball)
        center = (int(x), int(y))


        #Display the centre
        cent = cv.circle(frame, center, 5 , (255, 255, 255), -1)                   
        final = cv.bitwise_and(hsv_frame,cent)
        cv.imshow("final",final)

        #Check if the ball has changed its direction wrt y coordinate
        if prev_center is not None and center[1] < prev_center[1]:

                if prev_center[1] - center[1] > 62:             
                        bounce_count += 1                       

            


        prev_center = center

        ret,frame = cap.read()

        if cv.waitKey(1) & 0xFF == ord('q'):
                break


print(bounce_count)

cap.release()
cv.destroyAllWindows()


