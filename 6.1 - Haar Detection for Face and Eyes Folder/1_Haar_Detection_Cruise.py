# -*- coding: utf-8 -*-
"""
Created on Mon May 11 20:25:48 2020

@author: bradleyevans
"""


# Let's create a face and eye detector with OpenCV.
import numpy as np
import cv2



# First, we need to load the required XML classifiers.


# Solution 14a:
face_cascade = cv2.CascadeClassifier('C:\\opencv\\build\\etc\\haarcascades\\haarcascade_frontalface_default.xml')

# Solution 14b:
# face_cascade = cv2.CascadeClassifier('C:\\Users\\bradleyevans\\Desktop\\haarcascade_frontalface_default.xml')

# Solution 14d:
# face_cascade = cv2.CascadeClassifier('C:/Users/bradleyevans/Desktop/haarcascade_frontalface_default.xml')

# Solution 7:
# new_path = 'C:/Users/bradleyevans/Anaconda/Library/etc/haarcascades/'
# face_cascade = cv2.CascadeClassifier(new_path + 'haarcascade_frontalface_default.xml')

# Solution 4a:
# face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# Solution 4b:
# face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Solution 4c:
# face_cascade = cv2.CascadeClassifier(cv2.haarcascades + 'haarcascade_frontalface_default.xml')

# Solution 3a:
# r'C:\Desktop\haarcascade_frontalface_default.xml'

# Solution 3b:
# new_path = 'C:/Users/bradleyevans/Anaconda/Lib/site-packages/cv2/data/haarcascades/'
# face_cascade = cv2.CascadeClassifier(new_path + 'haarcascade_frontalface_default.xml')

# Solution 3c:
# new_path = 'C:\Users\bradleyevans\Desktop\Anaconda\Lib\site-packages\cv2\data\'
# face_cascade = cv2.CascadeClassifier(new_path + 'haarcascade_frontalface_default.xml')

# Solution 2:
# import pkg_resources
# haar_xml = pkg_resources.resource_filename(
#    'cv2', 'data/haarcascade_frontalface_default.xml')


# Solution 14a:
eye_cascade = cv2.CascadeClassifier('C:\\opencv\\build\\etc\\haarcascades\\haarcascade_eye.xml')

# Solution 14b:
# eye_cascade = cv2.CascadeClassifier('C:\\Users\\bradleyevans\\Desktop\\haarcascade_eye.xml')

# Solution 14d:
# eye_cascade = cv2.CascadeClassifier('C:/Users/bradleyevans/Desktop/haarcascade_eye.xml')

# Solution 7:
# new_path = 'C:/Users/bradleyevans/Anaconda/Library/etc/haarcascades/'
# face_cascade = cv2.CascadeClassifier(new_path + 'haarcascade_eye.xml')

# Solution 4a:
# eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

# Solution 4b:
# eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')

# Solution 4c:
# eye_cascade = cv2.CascadeClassifier(cv2.haarcascades + 'haarcascade_eye.xml')

# Solution 3a:
# r'C:\Desktop\haarcascade_eye.xml'

# Solution 3b:
# new_path = 'C:/Users/bradleyevans/Anaconda/Lib/site-packages/cv2/data/haarcascades/'
# face_cascade = cv2.CascadeClassifier(new_path + 'haarcascade_eye.xml')

# Solution 3c:
# new_path = 'C:\Users\bradleyevans\Desktop\Anaconda\Lib\site-packages\cv2\data\'
# face_cascade = cv2.CascadeClassifier(new_path + 'haarcascade_eye.xml')

# Solution 2:
# import pkg_resources
# haar_xml = pkg_resources.resource_filename(
#    'cv2', 'data/haarcascade_eye.xml')



# Then, load our input image in grayscale mode.
img = cv2.imread('Smiley.jpg')

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# classifier = cv2.CascadeClassifier(haar_xml)
# faces = classifier.detectMultiScale(img)

# Now, we find the faces in the image.
# If faces are found, it returns the positions
# of detected faces as Rect(x,y,w,h).
# Once we get these locations, we can create
# a ROI (Region of Interest) for the face
# and apply eye detection on this ROI
# (since eyes are always on the face!!!).
faces = face_cascade.detectMultiScale(gray, 1.3, 5)

for (x,y,w,h) in faces:
    img = cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
    roi_gray = gray[y:y+h, x:x+w]
    roi_color = img[y:y+h, x:x+w]
    eyes = eye_cascade.detectMultiScale(roi_gray)
    for (ex,ey,ew,eh) in eyes:
        cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)


title = 'Please detect Tom Cruise.'
cv2.imshow(title,img)

# This is a keyboard binding function - an infinite wait.
k = cv2.waitKey(0)

if k == 27:         # Wait for ESC key to exit.

    # This command simply destroys all the windows we created.
    cv2.destroyAllWindows()

elif k == ord('s'): # Wait for 's' key to save and exit.
    
    # Use this function to save an image.
    cv2.imwrite(title+'.png',img)
    
    # This command simply destroys all windows that have been created.
    cv2.destroyAllWindows()
