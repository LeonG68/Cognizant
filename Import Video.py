import cv2
import os

vid = cv2.VideoCapture(
    r'C:\Users\Leon\Desktop\Cognizant\Videos/Test Video.mkv')
currentframe = 0

if not os.path.exists('data'):
    os.makedirs('data')

while True:
    sucess, frame = vid.read()
    cv2.imshow('Output', frame)
    if currentframe % 60 == 0:
        cv2.imwrite('./data/frame' + str(currentframe) + '.jpg', frame)
    currentframe += 1

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

webCam.release()
cv2.destroyAllWindows()
