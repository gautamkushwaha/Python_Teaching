import cv2
import face_recognition
import numpy as np
import csv
import os
import glob
from datetime import datetime

#capturing from webcam
video_capture=cv2.VideoCapture(0)

#loading image from the path and encoding the features of the first face detected
ravi_image=face_recognition.load_image_file("photos/ravi.jpg")
ravi_encoding=face_recognition.face_encodings(ravi_image)[0]
kalam_image=face_recognition.load_image_file("photos/kalam.jpg")
kalam_encoding=face_recognition.face_encodings(kalam_image)[0]
ratan_image=face_recognition.load_image_file("photos/ratantata.jpg")
ratan_encoding=face_recognition.face_encodings(ratan_image)[0]




#storing the encoding and assign names to the encodings

known_face_encoding=[
    ravi_encoding,
    kalam_encoding,
    ratan_encoding
]

known_face_names=[
    "ravi",
    "kalam",
    "ratan"
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
    _, frame = video_capture.read()
    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
    rgb_small_frame = small_frame[:, :, ::-1]

    # Find face locations in the frame
    face_locations = face_recognition.face_locations(rgb_small_frame)
    face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)
    face_names = []

    for face_encoding in face_encodings:
        # Compare the detected face with known faces
        matches = face_recognition.compare_faces(known_face_encoding, face_encoding)
        name = "Unknown"  # Default name if no match is found

        # Check if any known face matches the detected face
        if True in matches:
            first_match_index = matches.index(True)
            name = known_face_names[first_match_index]

        face_names.append(name)

    # Draw bounding boxes and display names
    for (top, right, bottom, left), name in zip(face_locations, face_names):
        top *= 4
        right *= 4
        bottom *= 4
        left *= 4

        # Draw a box around the face
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

        # Display the name below the face
        cv2.putText(frame, name, (left + 6, bottom - 6), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)


        
        cv2.imshow("face_recognition",frame)
    if cv2.waitKey(1)&0XFF==ord('q'):
        break
video_capture.release()
cv2.destroyAllWindows()
f.close()

