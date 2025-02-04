import cv2
import time
from cvzone.HandTrackingModule import HandDetector
from roboflow import Roboflow

# Initialize Roboflow
rf = Roboflow(api_key="YOUR_API_KEY")
project = rf.workspace().project("signlanguageclassifier")
model = project.version(1).model

# Initialize Webcam
cap = cv2.VideoCapture(0)
detector = HandDetector(maxHands=1)
last_capture_time = time.time()
interval = 2  # Capture every 2 seconds

while True:
    success, img = cap.read()
    hands, img = detector.findHands(img)
    
    # Display live feed
    cv2.imshow("Live Feed", img)
    
    # Capture at intervals
    current_time = time.time()
    if current_time - last_capture_time > interval and hands:
        last_capture_time = current_time
        hand = hands[0]
        x, y, w, h = hand['bbox']
        
        # Crop and preprocess the hand region (same as Method 1)
        # ... (your existing code)
        
        # Classify
        cv2.imwrite("temp.jpg", imgWhite)
        prediction = model.predict("temp.jpg").json()
        predicted_class = prediction['predictions'][0]['class']
        print(f"Detected Sign: {predicted_class}")
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()