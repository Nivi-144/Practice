import numpy as np
from tensorflow import keras
from tensorflow.keras import layers
X = np.array([[0,0],[0,1],[1,0],[1,1]])
y = np.array([0, 1, 1, 0])   # XOR problem
model = keras.Sequential([
    layers.Dense(4, activation='relu', input_shape=(2,)),
    layers.Dense(1, activation='sigmoid')
])
model.compile(optimizer='adam',
              loss='binary_crossentropy',
              metrics=['accuracy'])
model.fit(X, y, epochs=500, verbose=0)
pred = model.predict(X)
print("Predictions:\n", pred)
