import cv2
import face_recognition
import numpy as np
import csv
import datetime

# Capturing from webcam
video_capture = cv2.VideoCapture(0)

# Loading images and encoding faces
ravi_image = face_recognition.load_image_file("photos/ravi.jpg")
ravi_encoding = face_recognition.face_encodings(ravi_image)[0]
kalam_image = face_recognition.load_image_file("photos/kalam.jpg")
kalam_encoding = face_recognition.face_encodings(kalam_image)[0]

known_face_encodings = [ravi_encoding, kalam_encoding]
known_face_names = ["ravi", "kalam"]

# Initialize variables for attendance tracking
persons = known_face_names.copy()
face_locations = []
face_encodings = []
face_names = []

# Get current date and time
now = datetime.datetime.now()
current_date = now.strftime("%Y-%m-%d")

# Create CSV file for attendance
with open(current_date + '.csv', 'w+', newline='') as f:
    csv_writer = csv.writer(f)

    while True:
        ret, frame = video_capture.read()
        small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
        rgb_small_frame = small_frame[:, :, ::-1]

        # Find faces and encode them
        face_locations = face_recognition.face_locations(rgb_small_frame)
        face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

        # Match faces with known encodings
        for face_encoding in face_encodings:
            matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
            name = "Unknown"

            if True in matches:
                first_match_index = matches.index(True)
                name = known_face_names[first_match_index]

            face_names.append(name)

            # Write attendance if a known person is recognized
            if name in known_face_names and name in persons:
                persons.remove(name)
                current_time = now.strftime("%H-%M-%S")
                csv_writer.writerow([name, current_time])

        cv2.imshow("Attendance System", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

# Release resources
video_capture.release()
cv2.destroyAllWindows()