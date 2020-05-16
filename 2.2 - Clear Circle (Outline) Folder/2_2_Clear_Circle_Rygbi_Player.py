# -*- coding: utf-8 -*-
"""
Created on Wed May  6 17:27:20 2020

@author: bradleyevans
"""

import numpy as np
import cv2

# Read an Image.
img = cv2.imread('Six Nations.jpg',1)

# Drawing Circle.
img = cv2.circle(img,(229,102), 50, (255,0,0), 2)

# Display an Image.
cv2.imshow('Rygbi Players Face Covered by a Blue, Clear Circle',img)

# This is a keyboard binding function. An infinite wait.
k = cv2.waitKey(0)

if k == 27:         # Wait for ESC key to exit.

    # This command simply destroys all the windows we created.
    cv2.destroyAllWindows()

elif k == ord('s'): # Wait for 's' key to save and exit.
    
    # Use this function to save an image.
    cv2.imwrite('Rygbi Players Face Covered by a Blue, Clear Circle.png',img)
    
    # This command simply destroys all the windows we created.
    cv2.destroyAllWindows()
    