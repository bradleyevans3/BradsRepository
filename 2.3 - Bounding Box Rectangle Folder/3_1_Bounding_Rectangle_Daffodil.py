# -*- coding: utf-8 -*-
"""
Created on Wed May  6 17:27:20 2020

@author: bradleyevans
"""

import numpy as np
import cv2

# Read an Image.
img = cv2.imread('Daffodils.jpg',1)

# Drawing Rectangle.
# img = cv2.circle(img,(290,344), 135, (0,255,0), 2)
img = cv2.rectangle(img,(64,47),(281,281),(128,128,0),2)

# Display an Image.
cv2.imshow('Daffodil Bounded by a Dark Green Rectangle',img)

# This is a keyboard binding function. An infinite wait.
k = cv2.waitKey(0)

if k == 27:         # Wait for ESC key to exit.

    # This command simply destroys all the windows we created.
    cv2.destroyAllWindows()

elif k == ord('s'): # Wait for 's' key to save and exit.
    
    # Use this function to save an image.
    cv2.imwrite('Daffodil Bounded by a Dark Green Rectangle.png',img)
    
    # This command simply destroys all the windows we created.
    cv2.destroyAllWindows()
    