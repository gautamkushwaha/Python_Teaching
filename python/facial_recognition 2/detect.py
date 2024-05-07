import cv2
import face_recognition
import numpy as np
import csv
import os
import glob
from datetime import datetime

#capturing from webcam
video_catpture=cv2.VideoCapture(0)

#loading image from the path and encoding the features of the first face detected
ravi_image=face_recognition.load_image_file("photos/ravi.jpg")
ravi_encoding=face_recognition.face_encodings(ravi_image)[0]
kalam_image=face_recognition.load_image_file("photos/kalam.jpg")
kalam_encoding=face_recognition.face_encodings(kalam_image)[0]




#storing the encoding and assign names to the encodings

known_face_encoding=[
    ravi_encoding,
    kalam_encoding
]

known_face_names=[
    "ravi",
    "kalam"
]

#make a copy of face encodings
persons=known_face_names.copy()
print(persons)

face_locations=[]
face_encodings=[]
face_names=[]
s=True



#getting the current date and time
now=datetime.now()
current_date=now.strftime("%Y-%m-%d")


#creating a csv file with the name as current date
f=open(current_date+'.csv','w+',newline='')
lnwrite=csv.writer(f)

while True:
    _,frame=video_catpture.read()
    small_frame=cv2.resize(frame,(0,0),fx=0.25,fy=0.25)
    rgb_small_frame=small_frame[:,:,::-1]
    if s:
        face_locations=face_recognition.face_locations(rgb_small_frame)
        face_encodings=face_recognition.face_encodings(rgb_small_frame,face_locations)
        face_names=[]
        for face_encoding in face_encodings:
            matches=face_recognition.compare_faces(known_face_encoding,face_encoding)
            name=""
            face_distance=face_recognition.face_distance(known_face_encoding,face_encoding)
            best_match_index=np.argmin(face_distance)
            if matches[best_match_index]:
                name=known_face_names[best_match_index]
            face_names.append(name)
            if name in known_face_names:
                if name in persons:
                    persons.remove(name)
                    print(persons)
                    current_time=now.strftime("%H-%M-%S")
                    lnwrite.writerow([name,current_time])
                    
    cv2.imshow("attendence_system",frame)
    if cv2.waitKey(1)&0XFF==ord('q'):
        break
video_catpture.release()
cv2.destroyAllWindows()
f.close()






