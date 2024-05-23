# -*- coding: utf-8 -*-
"""
Created on Fri Apr 19 18:59:07 2024

@author: okyaybariss
"""

import numpy as np
import os
import tensorflow as tf
from sklearn.model_selection import train_test_split
from tensorflow.keras.utils import plot_model


# Load and preprocess audio data
data_directory = "/content/drive/MyDrive/dataset1"
target_length = 130000  # Adjust this to your desired fixed length

def load_audio_data(data_directory, target_length=None, chunk_size=2048):
    classes = os.listdir(data_directory)
    audio_data = []
    labels = []

    class_to_label = {class_name: i for i, class_name in enumerate(classes)}

    for class_name in classes:
        class_directory = os.path.join(data_directory, class_name)
        if os.path.isdir(class_directory):
            for filename in os.listdir(class_directory):
                if filename.endswith(".wav"):
                    file_path = os.path.join(class_directory, filename)

                    # Load the audio file
                    audio = np.fromfile(file_path, dtype=np.int16)

                    # Convert to floating point representation
                    audio_float = audio.astype(np.float32)

                    # Normalize the audio data
                    normalized_audio = (audio_float - np.mean(audio_float)) / np.std(audio_float)

                    # Fix the length of the audio if specified
                    if target_length is not None:
                        if len(normalized_audio) < target_length:
                            normalized_audio = np.pad(normalized_audio, (0, target_length - len(normalized_audio)), mode='constant')
                        elif len(normalized_audio) > target_length:
                            normalized_audio = normalized_audio[:target_length]

                    audio_data.append(normalized_audio)
                    labels.append(class_to_label[class_name])  # Use integer label

    audio_data = np.array(audio_data)
    labels = np.array(labels)
    return audio_data, labels

# Load audio data and labels
audio_data, labels = load_audio_data(data_directory, target_length=target_length)

# Convert labels to one-hot encoded vectors
num_classes = len(set(labels))
labels = tf.keras.utils.to_categorical(labels, num_classes=num_classes)

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(audio_data, labels, test_size=0.2, random_state=42)

# Reshape the input data to include the timestep dimension
X_train_reshaped = np.reshape(X_train, (X_train.shape[0], X_train.shape[1], 1))
X_test_reshaped = np.reshape(X_test, (X_test.shape[0], X_test.shape[1], 1))

# Define LSTM model architecture
model = tf.keras.Sequential([
    tf.keras.layers.LSTM(256, input_shape=(X_train_reshaped.shape[1], X_train_reshaped.shape[2])),
    tf.keras.layers.Dropout(0.2),
    tf.keras.layers.Dense(num_classes, activation='softmax')
])

# Compile the model
model.compile(optimizer='adam',
              loss='categorical_crossentropy',
              metrics=['accuracy'])

# Train the model
model.fit(X_train_reshaped, y_train, epochs=10, batch_size=16, validation_data=(X_test_reshaped, y_test))
plot_model(model, to_file='model_plot.png', show_shapes=True, show_layer_names=True)
# Save the trained model
model.save('my_model.keras')
# Evaluate the model
loss, accuracy = model.evaluate(X_test_reshaped, y_test)
print(f'Test Loss: {loss}, Test Accuracy: {accuracy}')