# Feedforward Neural Network over MNIST
# Neural Network and Deep Learning Lab

import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf

from tensorflow.keras.datasets import mnist
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Flatten, Dense
from tensorflow.keras.utils import to_categorical
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay

# --------------------------------------------------
# 1. Load MNIST Dataset
# --------------------------------------------------

(x_train, y_train), (x_test, y_test) = mnist.load_data()

print("Training data shape:", x_train.shape)
print("Testing data shape:", x_test.shape)

# --------------------------------------------------
# 2. Normalize the pixel values
# --------------------------------------------------

x_train = x_train.astype("float32") / 255.0
x_test = x_test.astype("float32") / 255.0

# Convert labels to one-hot encoding
y_train_cat = to_categorical(y_train, 10)
y_test_cat = to_categorical(y_test, 10)

# --------------------------------------------------
# 3. Build Feedforward Neural Network
# --------------------------------------------------

model = Sequential([
    Flatten(input_shape=(28, 28)),
    Dense(128, activation='relu'),
    Dense(64, activation='relu'),
    Dense(10, activation='softmax')
])

# --------------------------------------------------
# 4. Compile the Model
# --------------------------------------------------

model.compile(
    optimizer='adam',
    loss='categorical_crossentropy',
    metrics=['accuracy']
)

# Display model architecture
model.summary()

# --------------------------------------------------
# 5. Train the Model
# --------------------------------------------------

history = model.fit(
    x_train,
    y_train_cat,
    epochs=10,
    batch_size=128,
    validation_split=0.1,
    verbose=1
)

# --------------------------------------------------
# 6. Evaluate on Test Dataset
# --------------------------------------------------

test_loss, test_accuracy = model.evaluate(
    x_test,
    y_test_cat,
    verbose=0
)

print("\nTest Loss:", test_loss)
print("Test Accuracy:", test_accuracy)

# --------------------------------------------------
# 7. Plot Training and Validation Accuracy
# --------------------------------------------------

plt.figure(figsize=(8, 5))

plt.plot(
    history.history['accuracy'],
    label='Training Accuracy'
)

plt.plot(
    history.history['val_accuracy'],
    label='Validation Accuracy'
)

plt.title('Training and Validation Accuracy')
plt.xlabel('Epochs')
plt.ylabel('Accuracy')
plt.legend()
plt.grid(True)

plt.show()

# --------------------------------------------------
# 8. Plot Training and Validation Loss
# --------------------------------------------------

plt.figure(figsize=(8, 5))

plt.plot(
    history.history['loss'],
    label='Training Loss'
)

plt.plot(
    history.history['val_loss'],
    label='Validation Loss'
)

plt.title('Training and Validation Loss')
plt.xlabel('Epochs')
plt.ylabel('Loss')
plt.legend()
plt.grid(True)

plt.show()

# --------------------------------------------------
# 9. Generate Predictions
# --------------------------------------------------

y_pred_prob = model.predict(x_test)

y_pred = np.argmax(y_pred_prob, axis=1)

# --------------------------------------------------
# 10. Generate Confusion Matrix
# --------------------------------------------------

cm = confusion_matrix(y_test, y_pred)

disp = ConfusionMatrixDisplay(
    confusion_matrix=cm,
    display_labels=np.arange(10)
)

plt.figure(figsize=(8, 8))

disp.plot(cmap='Blues', values_format='d')

plt.title('Confusion Matrix - MNIST Test Dataset')

plt.show()
