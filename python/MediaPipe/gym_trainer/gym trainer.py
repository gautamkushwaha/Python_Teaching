import numpy as np
import cv2
import mediapipe as mp
import time
import humanposemodule as hpm

cap = cv2.VideoCapture("gym.mp4")

previous_time = 0
current_time = 0

posedetect = hpm.poseDetector(detection_confident=0.8)

count = 0
direction = 0  # two directions 0 = up, 100 = down

while True:

    check, frame = cap.read()

    if check == True:

        # frame = cv2.imread("boy_exercise.jpg")
        frame = cv2.resize(frame, (1280, 720))
        frame = posedetect.findpose(frame, draw_landmark=False)
        lmlist = posedetect.findlocation(frame, draw_landmark=False)

        if len(lmlist) != 0:

            # Left arm
            # posedetect.findangle(frame, 11, 13, 15)

            # Right arm
            angle = posedetect.findangle(frame, 12, 14, 16)
            per = np.interp(angle, (180, 340), (0, 100))
            bar = np.interp(angle, (180, 340), (650, 100))

            color = (0, 255, 255)

            # count number of time
            if per == 100:
                color = (0, 0, 255)
                if direction == 0:
                    count += 0.5
                    direction = 1

            if per == 0:
                color = (0, 0, 255)
                if direction == 1:
                    count += 0.5
                    direction = 0

            # Bar
            cv2.rectangle(frame, (1100, 100), (1175, 650), color, 3)
            cv2.rectangle(frame, (1100, int(bar)), (1175, 650), color, cv2.FILLED)
            cv2.putText(frame, str(int(per)) + "%", (1100, 75), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 3)

            # Count
            cv2.rectangle(frame, (0, 450), (250, 720), (0, 255, 255), cv2.FILLED)
            cv2.putText(frame, str(int(count)), (60, 600), cv2.FONT_HERSHEY_PLAIN, 10, (255, 0, 0), 8)

        current_time = time.time()
        fps = 1 / (current_time - previous_time)
        previous_time = current_time

        cv2.putText(frame, "frame rate: " + str(int(fps)), (10, 70), cv2.FONT_HERSHEY_PLAIN, 5, (0, 255, 255), 5)

        cv2.imshow('Gym Trainer', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    else:
        break

cap.release()
cv2.destroyAllWindows()