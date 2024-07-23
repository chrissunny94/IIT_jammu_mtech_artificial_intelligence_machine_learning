import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential, Model
from tensorflow.keras.layers import Dense, Dropout, Flatten, Conv2D, MaxPooling2D, LSTM, Input
from tensorflow.keras.optimizers import SGD, Adam
from tensorflow.keras.callbacks import LearningRateScheduler
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from tensorflow.keras.applications import VGG16
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras import regularizers

# Set random seed for reproducibility
np.random.seed(42)
tf.random.set_seed(42)

# Module 1: Basics and History of Deep Learning Models

## McCulloh Pitts Neuron
def mcculloh_pitts_neuron(inputs, weights, threshold):
    activation = np.sum(inputs * weights) >= threshold
    return activation

## Perceptron Learning (using sklearn for example)
X, y = make_classification(n_samples=100, n_features=5, n_informative=3, n_redundant=1, n_classes=2)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
perceptron = SGD()  # Removed random_state argument
perceptron.fit(X_train, y_train)
y_pred = perceptron.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print("Perceptron Accuracy:", accuracy)

## Multi-layer Perceptron (MLP)
mlp_model = Sequential([
    Dense(64, activation='relu', input_shape=(5,)),  # Adjust input_shape according to your dataset
    Dense(64, activation='relu'),
    Dense(2, activation='softmax')  # Adjust output dimension according to your dataset
])
mlp_model.compile(optimizer='adam',
                  loss='sparse_categorical_crossentropy',
                  metrics=['accuracy'])
mlp_model.summary()

# Module 2: Optimization and Regularisation

## Gradient Descent
optimizer_sgd = SGD(learning_rate=0.01)

## Stochastic Gradient Descent (SGD)
optimizer_sgd_momentum = SGD(learning_rate=0.01, momentum=0.9)

## Adagrad, Adadelta, RMSProp, Adam
optimizer_adam = Adam(learning_rate=0.001)

## Learning Rate Schedulers
def scheduler(epoch, lr):
    if epoch < 10:
        return lr
    else:
        return lr * tf.math.exp(-0.1)

lr_scheduler = LearningRateScheduler(scheduler)

## Bias-Variance Tradeoff, L2 Regularization, Early Stopping, Data Augmentation, Dropout
mlp_model_reg = Sequential([
    Dense(64, activation='relu', kernel_regularizer=regularizers.l2(0.01), input_shape=(5,)),  # Adjust input_shape
    Dropout(0.2),
    Dense(64, activation='relu', kernel_regularizer=regularizers.l2(0.01)),
    Dense(2, activation='softmax')  # Adjust output dimension
])

# Module 3: Convolutional Neural Network (CNN)

## Convolutional Layers, Pooling
cnn_model = Sequential([
    Conv2D(32, (3, 3), activation='relu', input_shape=(28, 28, 1)),
    MaxPooling2D((2, 2)),
    Conv2D(64, (3, 3), activation='relu'),
    MaxPooling2D((2, 2)),
    Flatten(),
    Dense(64, activation='relu'),
    Dense(10, activation='softmax')
])

## Forward and Backward Pass in CNN (handled during training)

## Weight Initialization Methods
from tensorflow.keras.initializers import GlorotNormal

cnn_model_weight_init = Sequential([
    Conv2D(32, (3, 3), activation='relu', kernel_initializer=GlorotNormal(), input_shape=(28, 28, 1)),
    MaxPooling2D((2, 2)),
    Conv2D(64, (3, 3), activation='relu', kernel_initializer=GlorotNormal()),
    MaxPooling2D((2, 2)),
    Flatten(),
    Dense(64, activation='relu', kernel_initializer=GlorotNormal()),
    Dense(10, activation='softmax')
])

# Module 4: Sequence Modelling

## Recurrent Neural Networks (RNNs), Long Short-Term Memory (LSTM)
rnn_model = Sequential([
    LSTM(64, input_shape=(10, 64)),  # Example shape for LSTM input
    Dense(10, activation='softmax')
])

## Transformers: Attention Mechanism (example placeholder)

# Module 5: Special Topics in Deep Learning

## Generative Adversarial Networks (GANs) - Example with Keras

# Generator model
generator_input = Input(shape=(100,))
x = Dense(128, activation='relu')(generator_input)
x = Dense(784, activation='sigmoid')(x)
generator = Model(generator_input, x)

# Discriminator model
discriminator_input = Input(shape=(784,))
y = Dense(128, activation='relu')(discriminator_input)
y = Dense(1, activation='sigmoid')(y)
discriminator = Model(discriminator_input, y)
discriminator.compile(optimizer=Adam(learning_rate=0.0002), loss='binary_crossentropy')

# Combined GAN model
gan_input = Input(shape=(100,))
gan_output = discriminator(generator(gan_input))
gan = Model(gan_input, gan_output)
gan.compile(optimizer=Adam(learning_rate=0.0002), loss='binary_crossentropy')

## Transfer Learning with VGG16
base_model = VGG16(weights='imagenet', include_top=False, input_shape=(224, 224, 3))
# Add your layers on top for fine-tuning

# End of script
