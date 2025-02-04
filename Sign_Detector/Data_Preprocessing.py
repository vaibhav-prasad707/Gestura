import pandas as pd
from sklearn.preprocessing import MinMaxScaler, LabelEncoder
from sklearn.model_selection import train_test_split
import pickle

# Load the collected CSV data
data = pd.read_csv('sign_data.csv')

# Remove rows where 'label' accidentally appears as a data entry
data = data[data['label'].apply(lambda x: x not in ['label', 'x0', 'y0', 'z0'])]

# Check for missing values and remove them
data = data.dropna()

# Ensure all landmark columns are numeric (excluding 'label')
landmark_features = data.drop('label', axis=1)
landmark_features = landmark_features.apply(pd.to_numeric, errors='coerce')

# Remove any remaining NaN values after conversion
data = data.dropna()

# Normalize landmark coordinates using Min-Max Scaling
scaler = MinMaxScaler()
normalized_data = scaler.fit_transform(landmark_features)

# Convert back to DataFrame
normalized_df = pd.DataFrame(normalized_data, columns=landmark_features.columns)
normalized_df['label'] = data['label'].values

# Encode labels (Hello, I like you, Thank you, Nice, Good Job)
label_encoder = LabelEncoder()
normalized_df['label'] = label_encoder.fit_transform(normalized_df['label'])

# Save the label encoder for decoding predictions later
with open('label_encoder.pkl', 'wb') as f:
    pickle.dump(label_encoder, f)

# Display encoded labels
print("Encoded Labels:", dict(zip(label_encoder.classes_, label_encoder.transform(label_encoder.classes_))))

# Split the dataset into training (80%) and testing (20%) sets
X = normalized_df.drop('label', axis=1)
y = normalized_df['label']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Save the preprocessed data for model training
X_train.to_csv('X_train.csv', index=False)
X_test.to_csv('X_test.csv', index=False)
y_train.to_csv('y_train.csv', index=False)
y_test.to_csv('y_test.csv', index=False)

print("✅ Data preprocessing complete. Ready for model training!")
