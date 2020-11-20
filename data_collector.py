import cv2
import numpy as np

facecascade=cv2.CascadeClassifier("C:/Users/Chirag/PycharmProjects/biometric_ass/venv/Lib/site-packages/cv2/data/haarcascade_frontalface_default.xml")
path="C:/Users/Chirag/Pictures/Camera Roll/1530538904171.jpg"


def face_extr(img):
    global cropped_face
    faces=facecascade.detectMultiScale(img,1.3,5)
    if faces is ():
        return None
    for (x,y,w,h) in faces:
        x=x-10
        y=y-10
        cropped_face=img
    return cropped_face


cap=cv2.VideoCapture(0)
count=0
while True:
    success,img=cap.read()
    if face_extr(img) is not None:
        count+=1
        face=cv2.resize(face_extr(img),(400,400))
        file_name_path='C:/Users/Chirag/PycharmProjects/biometric_ass/Images/'+str(count)+'.jpg'
        cv2.imwrite(file_name_path,face)
        cv2.putText(face,str(count),(50,50),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),2)
        cv2.imshow("Face",face)
    else:
        print("Face not found")
        pass
    if cv2.waitKey(1)==13 or count==10:
        break
cap.release()
cv2.destroyAllWindows()
print("Data collection complete")
