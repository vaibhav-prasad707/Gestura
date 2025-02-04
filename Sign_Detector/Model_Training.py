from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import LabelEncoder
import numpy as np
import pandas as pd
import cv2
import mediapipe as mp
import pickle

# MediaPipe setup
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1)
mp_draw = mp.solutions.drawing_utils

# Load dataset
data = pd.read_csv('sign_data.csv')

# Data preprocessing
if 'label' not in data.columns:
    raise ValueError("The 'label' column is missing from the CSV.")

landmark_features = data.drop('label', axis=1).apply(pd.to_numeric, errors='coerce')
clean_data = pd.concat([landmark_features, data['label']], axis=1).dropna()

# Features and Labels
X = clean_data.drop('label', axis=1).values
y = clean_data['label'].values

# Label Encoding
label_encoder = LabelEncoder()
y_encoded = label_encoder.fit_transform(y)

# Train KNN Model
knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(X, y_encoded)

# Save Model and Label Encoder
with open('knn_sign_model.pkl', 'wb') as f:
    pickle.dump(knn, f)
with open('label_encoder.pkl', 'wb') as f:
    pickle.dump(label_encoder, f)

# Display Label Encodings
print("✅ Model training complete!")
print("Label Encodings:", dict(zip(label_encoder.classes_, label_encoder.transform(label_encoder.classes_))))

# Open Webcam
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("❌ Error: Could not open webcam.")
    exit()

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        print("❌ Error: Failed to capture frame.")
        break

    frame = cv2.flip(frame, 1)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = hands.process(rgb_frame)

    if result.multi_hand_landmarks:
        for hand_landmarks in result.multi_hand_landmarks:
            mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            # Extract landmarks
            landmarks = []
            for lm in hand_landmarks.landmark:
                landmarks.extend([lm.x, lm.y, lm.z])

            try:
                # Check if landmark dimensions match model input
                if len(landmarks) != X.shape[1]:
                    print(f"⚠️ Landmark mismatch: Expected {X.shape[1]}, got {len(landmarks)}")
                    continue

                # Predict Sign
                prediction = knn.predict([landmarks])
                predicted_label = label_encoder.inverse_transform(prediction)[0]

                # Display Prediction
                cv2.putText(frame, predicted_label, (10, 50), cv2.FONT_HERSHEY_SIMPLEX,
                            1, (255, 0, 0), 2, cv2.LINE_AA)
            except Exception as e:
                print(f"❌ Prediction Error: {e}")
                continue

    cv2.imshow('Sign Detection', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release Resources
cap.release()
cv2.destroyAllWindows()
