import cv2
import time

name = input("Masukkan nama: ")

cam = cv2.VideoCapture(0) 
 
desired_frame = 5
currentframe = 0
img_counter = 1
frame_delay = 0.5

while currentframe < desired_frame:
    ret, frame = cam.read()

    if ret:
        img_name = "C:/Users/Gerrard/Documents/Live_Face_Recognition/Images/{}_{}.jpg".format(name, img_counter)

        cv2.imwrite(img_name, frame)

        currentframe += 1
        img_counter += 1

        time.sleep(frame_delay)
