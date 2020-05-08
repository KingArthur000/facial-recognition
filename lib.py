import face_recognition
import os
import cv2
import numpy


KNOWN_FACES_DIR = 'known_faces'
UNKNOWN_FACES_DIR = 'unknown_faces'
TOLERANCE = 0.6
FRAME_THICKNESS = 3
FONT_THICKNESS = 2
MODEL = 'cnn'  # default: 'hog', other one can be 'cnn' - CUDA accelerated (if available) deep-learning pretrained model

print('Loading known faces...')
known_faces = []
known_names = []
name = 'known_face'

image = face_recognition.load_image_file(str(KNOWN_FACES_DIR)+'/'+str(name)+'/new1.jpg')

encoding = face_recognition.face_encodings(image)[0]
#visualizing what encoding is....
#cv2.imshow("img1",encoding)
#cv2.waitKey(0)
#visualizing the input to the cnn
print(encoding)
#print(numpy.shape(encoding))
cv2.imshow("img",image)
cv2.waitKey(0)
#checking what locations are
locations = face_recognition.face_locations(image, model=MODEL)
print(locations)
cv2.waitKey(0)
cv2.destroyAllWindows()
