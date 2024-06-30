import numpy as np

def sigmoid(z):
    return 1 / (1 + np.exp(-z))

# Assign weights
w0 = -1
w1 = 2
w2 = 4
w3 = -1

# Function to compute the output of the sigmoid unit
def compute_output(x1, x2, x3):
    z = w0 + w1*x1 + w2*x2 + w3*x3
    return sigmoid(z)

# Test all possible input combinations
inputs = [(0, 0, 0), (0, 0, 1), (0, 1, 0), (0, 1, 1),
          (1, 0, 0), (1, 0, 1), (1, 1, 0), (1, 1, 1)]

print("x1 x2 x3 | Output")
print("-----------------")
for (x1, x2, x3) in inputs:
    output = compute_output(x1, x2, x3)
    print(f"{x1}  {x2}  {x3}  | {output:.2f}")
