import cv2
import os

video = cv2.VideoCapture(0)
while True:
    ret, frame = video.read()
    cv2.imshow("vid",frame)
    if cv2.waitKey(1) & 0xFF == ord('s'):
        cv2.imwrite("new_faces/sat.jpg",frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video.release()
cv2.destroyAllWindows()