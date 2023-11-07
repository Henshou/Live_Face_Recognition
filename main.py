import threading
import cv2
from deepface import DeepFace
import glob

cam = cv2.VideoCapture(0)


counter = 0

face_match = False

path= glob.glob("C:/Users/Gerrard/Documents/Live_Face_Recognition/Images/*.jpg")#change path name into your path

for file in path:
    reference_img = cv2.imread(file) 
        
def check_face(frame):
    global face_match
    try:
        if DeepFace.verify(frame, reference_img.copy())['verified']:
            face_match = True
        else:
            face_match = False
    except ValueError:
        face_match = False


while True:
    ret, frame= cam.read()

    if ret:
        if counter % 30 == 0:
            try:
                threading.Thread(target=check_face, args=(frame.copy(),)).start()
            except ValueError:
                pass
        counter += 1

        if face_match:
            cv2.putText(frame, "MATCH!", (20,450), cv2.FONT_HERSHEY_SIMPLEX, 2, (0,255,0), 3)
        else:
            cv2.putText(frame, " NO MATCH!", (20,450), cv2.FONT_HERSHEY_SIMPLEX, 2, (0,0,255), 3)

        cv2.imshow("Video", frame)

    key = cv2.waitKey(1)
    if key == ord("q"):
        break
    

cv2.destroyAllWindows()