import cv2
import mediapipe as mp
import csv
import time

# Initialize MediaPipe Hands
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1)
mp_draw = mp.solutions.drawing_utils

# Open webcam
cap = cv2.VideoCapture(0)

# CSV file to store landmark data
csv_file = open('sign_data.csv', mode='a', newline='')
csv_writer = csv.writer(csv_file)
header = ['label'] + [f'{coord}{i}' for i in range(21) for coord in ('x', 'y', 'z')]
csv_writer.writerow(header)  # Write header

# Input the sign label
label = input("Enter the sign label (e.g., Hello, Yes, No): ")

print("Press 's' to start collecting data and 'q' to quit.")

collect_data = False

while cap.isOpened():
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = hands.process(rgb_frame)

    if result.multi_hand_landmarks:
        for hand_landmarks in result.multi_hand_landmarks:
            mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            # Collect data when 's' is pressed
            if collect_data:
                landmarks = []
                for lm in hand_landmarks.landmark:
                    landmarks.extend([lm.x, lm.y, lm.z])
                csv_writer.writerow([label] + landmarks)
                cv2.putText(frame, "Collecting Data...", (10, 50), cv2.FONT_HERSHEY_SIMPLEX,
                            1, (0, 255, 0), 2, cv2.LINE_AA)

    cv2.imshow('Data Collection', frame)

    key = cv2.waitKey(1)
    if key == ord('s'):
        collect_data = True  # Start data collection
    elif key == ord('q'):
        break  # Quit the program

# Cleanup
cap.release()
csv_file.close()
cv2.destroyAllWindows()
