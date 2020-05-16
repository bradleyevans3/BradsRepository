# -*- coding: utf-8 -*-
"""
Created on Wed May  6 17:27:20 2020

@author: bradleyevans
"""

import numpy as np
import cv2

# Read an Image.
img = cv2.imread('Daffodils.jpg',1)

# Drawing a Solid Circle.
img = cv2.circle(img,(446,234), 120, (128,128,128), -1)
# Drawing a Clear Circle.
img = cv2.circle(img,(290,344), 135, (0,255,0), 2)
# Drawing a Rectangular Bounding Box.
img = cv2.rectangle(img,(64,47),(281,281),(128,128,0),2)

# Display an Image.
title = 'Daffodils Covered by a Solid Circle, Clear Circle, and a Box'
print(title)
print(title+'.png')
cv2.imshow(title,img)

# This is a keyboard binding function. An infinite wait.
k = cv2.waitKey(0)

if k == 27:         # Wait for ESC key to exit.

    # This command simply destroys all the windows we created.
    cv2.destroyAllWindows()

elif k == ord('s'): # Wait for 's' key to save and exit.
    
    # Use this function to save an image.
    cv2.imwrite(title+'.png',img)
    
    # This command simply destroys all the windows we created.
    cv2.destroyAllWindows()
    