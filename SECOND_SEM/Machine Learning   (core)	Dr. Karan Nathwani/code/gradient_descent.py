import numpy as np

# Sample data for gradient descent
X = np.array([[1, 1], [1, 2], [2, 2], [2, 3]])
y = np.array([6, 8, 9, 11])
theta = np.random.randn(2)

# Gradient descent parameters
alpha = 0.01
num_iterations = 1000

# Gradient descent algorithm
for _ in range(num_iterations):
    gradient = np.dot(X.T, (np.dot(X, theta) - y)) / len(y)
    theta -= alpha * gradient

print("Learned parameters:", theta)
