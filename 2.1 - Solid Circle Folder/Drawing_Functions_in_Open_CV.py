# -*- coding: utf-8 -*-
"""
Created on Wed May  6 17:27:20 2020

@author: bradleyevans
"""

import numpy as np
import cv2

# Drawing Line.
# Create a black, background image.
img = np.zeros((512,512,3), np.uint8)

# Draw a diagonal blue line with thickness of 5 px.
img = cv2.line(img,(0,0),(511,511),(255,0,0),5)

# Drawing Rectangle.
img = cv2.rectangle(img,(384,0),(510,128),(0,255,0),3)

# Drawing Circle.
img = cv2.circle(img,(447,63), 63, (0,0,255), -1)

# Drawing Ellipse.
img = cv2.ellipse(img,(256,256),(100,50),0,0,180,255,-1)

# Drawing Polygon.
pts = np.array([[10,5],[20,30],[70,20],[50,10]], np.int32)
pts = pts.reshape((-1,1,2))
img = cv2.polylines(img,[pts],True,(0,255,255))

# Adding Text to Images.
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img,'OpenCV',(10,500), font, 4,(255,255,255),2,cv2.LINE_AA)

# Display an Image.
cv2.imshow('Drawing Functions in Open CV',img)

# This is a keyboard binding function. An infinite wait.
k = cv2.waitKey(0)

if k == 27:         # Wait for ESC key to exit.

    # This command simply destroys all the windows we created.
    cv2.destroyAllWindows()

elif k == ord('s'): # Wait for 's' key to save and exit.
    
    # Use this function to save an image.
    cv2.imwrite('Drawing_Functions_in_Open_CV.png',img)
    
    # This command simply destroys all the windows we created.
    cv2.destroyAllWindows()
    