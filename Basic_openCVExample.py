import cv2

# Open the default camera (0)
camera = cv2.VideoCapture(0)

# Check if the camera opened successfully
if not camera.isOpened():
    print("Error: Could not open camera.")
    exit()

# Your name
name = "Ishaan Jain"
Date = "03-02-3035"

while True:
    # Capture frame-by-frame
    ret, frame = camera.read()
    
    if not ret:
        print("Failed to grab frame")
        break

    # Add your name to the frame
    cv2.putText(frame, name, (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)
    
    # frame, date, (x,y) access, font, font scale, color rgb, thickness, edges.
    cv2.putText(frame, Date, (100, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)

    # Display the resulting frame
    cv2.imshow('Camera Feed', frame)

    # Press 'q' to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the camera and close windows
camera.release()
cv2.destroyAllWindows()