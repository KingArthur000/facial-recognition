import cv2
import face_recognition
import os
import numpy as np

DIR = 'ex_faces'

for file in os.listdir(DIR):
    image = face_recognition.load_image_file(f'{DIR}/{file}')
    face_location = face_recognition.face_locations(image,model = 'cnn')
    print(np.shape(face_location))
    for i in range(np.shape(face_location)[0]):
        top_left = (face_location[i][3], face_location[i][0])
        bottom_right = (face_location[i][1], face_location[i][2])
        cv2.rectangle(image,top_left,bottom_right,[0,255,0],1)
    cv2.imshow("win",image)
    cv2.waitKey(0)

cv2.destroyAllWindows()