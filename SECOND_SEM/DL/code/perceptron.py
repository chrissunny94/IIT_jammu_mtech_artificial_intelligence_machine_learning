import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Set random seed for reproducibility
np.random.seed(42)
tf.random.set_seed(42)

# Generate synthetic data
X, y = make_classification(n_samples=100, n_features=5, n_informative=3, n_redundant=1, n_classes=2, random_state=42)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Define perceptron model
perceptron_model = Sequential([
    Dense(1, activation='sigmoid', input_shape=(5,))
])

# Compile the model
perceptron_model.compile(optimizer='sgd',
                         loss='binary_crossentropy',
                         metrics=['accuracy'])

# Print model summary
perceptron_model.summary()

# Train the model
perceptron_model.fit(X_train, y_train, epochs=50, batch_size=1, verbose=1)

# Evaluate the model
y_pred = perceptron_model.predict(X_test)
y_pred = (y_pred > 0.5).astype(int)
accuracy = accuracy_score(y_test, y_pred)
print("Perceptron Accuracy:", accuracy)
