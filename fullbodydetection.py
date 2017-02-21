##########################################
#****** ML Height Estimate Project ******#
#** Rahul Rachh    - 1401057 **#
#** Kedar Acharya  - 1401081 **#
#** Janki Desai    - 1401103 **#
#** Shloak Agarwal - 1401105 **#
##########################################

#We can initialize numpy arrays from nested Python lists, and access elements using square brackets.
import numpy as np
#Wraps the python api, and uses numpy arrays for images
import cv2

#'def' is like a 'function' used in c++.A function is a block of organized, reusable code that is used to perform a single, related action.
#The function name is 'inside' with the parameters 'r' & 'q' and the function returns 'true' and 'false' according to the result.
def inside(r, q):
    rx, ry, rw, rh = r
    qx, qy, qw, qh = q
    #def inside returns 'true' or 'false' according to the result of relational operator.
    return rx > qx and ry > qy and rx + rw < qx + qw and ry + rh < qy + qh

#'def' is like a 'function' used in c++.A function is a block of organized, reusable code that is used to perform a single, related action.
#The function name is 'draw_detections' with parameters 'img'(gray scale image/video), 'rects'(rectangle paramters) & thickness(thickness of the border(predefine=2)).
#'draw_detections' draws the rectangle around the human body that is detected with the border thickness = 2.
#Futher the function also detect the height of the human body that is detected.
def draw_detections(img, rects, thickness = 2):
    for x, y, w, h in rects:
        # the HOG detector returns slightly larger rectangles than the real objects.
        # so we slightly shrink the rectangles to get a nicer output.
        pad_w, pad_h = int(0.15*w), int(0.05*h)
        cv2.rectangle(img, (x+pad_w, y+pad_h), (x+w-pad_w, y+h-pad_h), (0, 255, 0), thickness)
        P_ref = 480
        H_ref = 168.544
        P_left = P_ref-(y+h)
        k = (P_ref - (2*P_left))/P_ref
        Height = ((1/k) * ((h*H_ref)/P_ref))
        print (Height + 10);

if __name__ == '__main__':

    hog = cv2.HOGDescriptor()
    hog.setSVMDetector( cv2.HOGDescriptor_getDefaultPeopleDetector() )
    cap=cv2.VideoCapture(0)
    #for seg
    fgbg = cv2.createBackgroundSubtractorMOG2()
    
    while True:
        ret,frame=cap.read()
        #for grayscale
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        #fgmask = fgbg.apply(frame)                
        found,w=hog.detectMultiScale(gray, winStride=(8,8), padding=(32,32), scale=1.05)
        draw_detections(gray,found)
        cv2.imshow('feed',gray)
        
        ch = 0xFF & cv2.waitKey(1)
        if ch == 27:
            break
    
    cv2.release()
    cv2.destroyAllWindows()
