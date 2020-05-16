# -*- coding: utf-8 -*-
"""
Created on Wed May  6 17:27:20 2020

@author: bradleyevans
"""

import numpy as np
import cv2

# Read an Image.
img = cv2.imread('Smiley.jpg',1)

# Drawing a Solid Circle.
img = cv2.circle(img,(447,220), 15, (0,255,0), -1)
# Drawing a Clear Circle.
img = cv2.circle(img,(570,187), 15, (0,0,255), 4)
# Drawing a Rectangular Bounding Box.
img = cv2.rectangle(img,(370,86),(632,466),(128,0,128),2)

# Display the Image.
cv2.imshow('Smiley with a Solid Circle, Clear Circle, and a Bounding Box',img)

# This is a keyboard binding function. An infinite wait.
k = cv2.waitKey(0)

if k == 27:         # Wait for ESC key to exit.

    # This command simply destroys all the windows we created.
    cv2.destroyAllWindows()

elif k == ord('s'): # Wait for 's' key to save and exit.
    
    # Use this function to save an image.
    cv2.imwrite('Smiley with a Solid Circle, Clear Circle, and a Bounding Box.png',img)
    
    # This command simply destroys all the windows we created.
    cv2.destroyAllWindows()
