import os
import cv2
import numpy as np

NEW_FACES_DIR = 'new_faces'

i=0

for name in os.listdir(NEW_FACES_DIR):
    if name == 'new':
        for file in os.listdir(f'{NEW_FACES_DIR}/{name}'):
            image = cv2.imread(f'{NEW_FACES_DIR}/{name}/{file}')
            img = cv2.resize(image,(480,640))
            i = i + 1
            cv2.imwrite(f'{NEW_FACES_DIR}/{name}/{name}{i}.jpg',img)
        i=0
#for file in os.listdir(UNKNOWN_FACES_DIR):
#    image = cv2.imread(str(UNKNOWN_FACES_DIR) + '/' + str(file))
#    img = cv2.resize(image,(480,640))
#    i = i + 1
#    cv2.imwrite(str(UNKNOWN_FACES_DIR) + '/' + str(i) + '.jpg',img)
cv2.waitKey(0)