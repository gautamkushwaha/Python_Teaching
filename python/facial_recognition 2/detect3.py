import cv2
import face_recognition

import numpy as np
import csv
import os
from datetime import datetime
import exifread
from PIL import Image
from PIL.ExifTags import TAGS, GPSTAGS
import json
from urllib.request import urlopen
from datetime import datetime


if not os.path.exists('captured_images'):
    os.makedirs('captured_images')

# Function to get geotagging information from a photo
def get_geotagging_info(file_path):
    with Image.open(file_path) as img:
        exif_data = img._getexif()
        

        if exif_data is not None:
            # Access Exif GPS information
            gps_info = exif_data.get(34853)  # Exif tag for GPSInfo

            if gps_info is not None:
                latitude = gps_info[2][0] + gps_info[2][1] / 60 + gps_info[2][2] / 3600
                longitude = gps_info[4][0] + gps_info[4][1] / 60 + gps_info[4][2] / 3600

                if gps_info[3] == 'S':
                    latitude = -latitude

                if gps_info[1] == 'W':
                    longitude = -longitude
                
                print(latitude,longitude)

                return latitude, longitude

    return None
# Function to save location information to CSV
def save_location_to_csv(file_path, location_info):
    with open(file_path, 'a', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow([datetime.now(), location_info])

now=datetime.now()
current_date=now.strftime("%Y-%m-%d")


#creating a csv file with the name as current date
f=open(current_date+'.csv','w+',newline='')
lnwrite=csv.writer(f)

# Capturing from webcam
video_capture = cv2.VideoCapture(0)
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




# Getting the current date and time
now = datetime.now()
current_date = now.strftime("%Y-%m-%d")

# Creating a CSV file with the name as the current date
csv_file_path = current_date + '.csv'
with open(csv_file_path, 'w', newline='') as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(['Timestamp', 'Location'])
i=5

while i:
    _, frame = video_capture.read()
    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
    rgb_small_frame = small_frame[:, :, ::-1]

    # Find face locations in the frame
    face_locations = face_recognition.face_locations(rgb_small_frame)
    # face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)
    face_encodings = face_recognition.face_encodings(rgb_small_frame, [face_locations[0]])

    face_names = []

    for face_encoding in face_encodings:
        # Compare the detected face with known faces
        matches = face_recognition.compare_faces(known_face_encoding, face_encoding)
        name = "Unknown"  # Default name if no match is found

        # Check if any known face matches the detected face
        if True in matches:
            first_match_index = matches.index(True)
            name = known_face_names[first_match_index]
            exit
            


        face_names.append(name)
        if name in known_face_names:
                if name in persons:
                    persons.remove(name)
                    print(persons)
                    current_time=now.strftime("%H-%M-%S")
                    lnwrite.writerow([name,current_time])

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

        # Save the captured frame as an image file
        
    cv2.imshow("face_recognition", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    i=i-1

video_capture.release()
cv2.destroyAllWindows()