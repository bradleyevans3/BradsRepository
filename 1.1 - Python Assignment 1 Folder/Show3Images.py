# -*- coding: utf-8 -*-
"""
Created on Mon May  4 17:21:36 2020

@author: bradleyevans
"""

import numpy as np
import cv2

# Read an Image.
img1 = cv2.imread('Daffodils.jpg',0)
img2 = cv2.imread('Six Nations.jpg',0)
img3 = cv2.imread('Smiley.jpg',0)

# Display an Image.
cv2.imshow('Daffodils',img1)
cv2.imshow('Six Nations',img2)
cv2.imshow('Smiley',img3)

# This is a keyboard binding function. An infinite wait.
k = cv2.waitKey(0)

if k == 27:         # Wait for ESC key to exit.

    # This command simply destroys all the windows we created.
    cv2.destroyAllWindows()

elif k == ord('s'): # Wait for 's' key to save and exit.
    
    # Use this function to save an image.
    cv2.imwrite('Daffodils_gray.png',img1)
    cv2.imwrite('Six_Nations_gray.png',img2)
    cv2.imwrite('Smiley_gray.png',img3)
    
    # This command simply destroys all the windows we created.
    cv2.destroyAllWindows()
    