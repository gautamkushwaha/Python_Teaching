import cv2

# Initialize the camera
cap = cv2.VideoCapture(1)

# Check if camera opened successfully
if not cap.isOpened():
    print("Error opening camera!")
    exit(1)

# Capture a frame
ret, frame = cap.read()

# Check if frame captured successfully
if not ret:
    print("Error capturing frame!")
    exit(1)

# Display the captured frame
cv2.imshow("Camera", frame)
cv2.waitKey(0)  # Wait for a key press before proceeding

# Save the captured frame as an image
cv2.imwrite("Gautam2.jpg", frame)

# Release the camera
cap.release()

# Destroy all windows
cv2.destroyAllWindows()

print("Image captured and saved successfully!")
