import cv2
import face_recognition
import os
import numpy as np

DIR = 'ex_faces'

for file in os.listdir(DIR):
    image = face_recognition.load_image_file(f'{DIR}/{file}')
    face_location = face_recognition.face_locations(image,model = 'cnn')
    face_encoding = face_recognition.face_encodings(image,num_jitters = 1)
    print(len(face_encoding[0]))
    cv2.imshow("win",image)
    cv2.waitKey(0)

cv2.destroyAllWindows()