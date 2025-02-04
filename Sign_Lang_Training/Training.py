# Step 1: Install required packages
# pip install tensorflow opencv-python numpy matplotlib

# Step 2: Import necessary libraries
import tensorflow as tf
from tensorflow.keras import layers, models
from tensorflow.keras.preprocessing.image import ImageDataGenerator
import numpy as np
import cv2
import os

# Step 3: Set parameters
IMG_SIZE = (224, 224)
BATCH_SIZE = 32
EPOCHS = 20
NUM_CLASSES = 6  # Update with your number of classes
TRAIN_PATH = "Sign_Lang_Training\Data"  # Update path
VALIDATION_PATH = "Sign_Lang_Training\Data"  # Update path

# Step 4: Create data generators with augmentation
train_datagen = ImageDataGenerator(
    rescale=1./255,
    rotation_range=20,
    width_shift_range=0.2,
    height_shift_range=0.2,
    shear_range=0.2,
    zoom_range=0.2,
    horizontal_flip=True,
    fill_mode='nearest'
)

val_datagen = ImageDataGenerator(rescale=1./255)

train_generator = train_datagen.flow_from_directory(
    TRAIN_PATH,
    target_size=IMG_SIZE,
    batch_size=BATCH_SIZE,
    class_mode='sparse'
)

validation_generator = val_datagen.flow_from_directory(
    VALIDATION_PATH,
    target_size=IMG_SIZE,
    batch_size=BATCH_SIZE,
    class_mode='sparse'
)

# Step 5: Create the model using transfer learning
base_model = tf.keras.applications.MobileNetV2(
    input_shape=(224, 224, 3),
    include_top=False,
    weights='imagenet'
)

base_model.trainable = True

model = models.Sequential([
    base_model,
    layers.GlobalAveragePooling2D(),
    layers.Dense(256, activation='relu'),
    layers.Dropout(0.5),
    layers.Dense(NUM_CLASSES, activation='softmax')
])

# Step 6: Compile the model
model.compile(
    optimizer=tf.keras.optimizers.Adam(learning_rate=1e-4),
    loss='sparse_categorical_crossentropy',
    metrics=['accuracy']
)

# Step 7: Train the model
history = model.fit(
    train_generator,
    epochs=EPOCHS,
    validation_data=validation_generator,
    verbose=1
)

# Step 8: Save the model
model.save('sign_language_model.h5')

# Step 9: Real-time detection
class_names = sorted(os.listdir(TRAIN_PATH))  # Get class names from directory

# Load the trained model
model = tf.keras.models.load_model('sign_language_model.h5')

# Initialize webcam
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break
    
    # Preprocess frame
    resized = cv2.resize(frame, IMG_SIZE)
    normalized = resized / 255.0
    input_tensor = np.expand_dims(normalized, axis=0)
    
    # Make prediction
    predictions = model.predict(input_tensor)
    predicted_class = np.argmax(predictions[0])
    confidence = np.max(predictions[0])
    
    # Display results
    label = f"{class_names[predicted_class]} ({confidence:.2f})"
    cv2.putText(frame, label, (10, 30), 
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    cv2.imshow('Sign Language Detection', frame)
    
    # Exit on 'q' press
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()