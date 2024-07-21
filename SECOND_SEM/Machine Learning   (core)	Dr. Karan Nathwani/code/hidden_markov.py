import numpy as np
from hmmlearn import hmm

# Define model parameters
num_hidden_states = 3  # Number of hidden states
num_emissions = 5      # Number of possible observations

# Transition probability matrix (A)
# Probability of transitioning from each state to another
A = np.array([
    [0.7, 0.2, 0.1],
    [0.1, 0.6, 0.3],
    [0.2, 0.3, 0.5]
])

# Emission probability matrix (B)
# Probability of emitting each observation symbol from each hidden state
B = np.array([
    [0.4, 0.2, 0.1, 0.2, 0.1],
    [0.1, 0.3, 0.2, 0.2, 0.2],
    [0.2, 0.1, 0.3, 0.2, 0.2]
])

# Initial state probabilities (π)
# Probability of starting in each hidden state
pi = np.array([0.5, 0.3, 0.2])

# Create the HMM model
model = hmm.MultinomialHMM(n_components=num_hidden_states)
model.startprob_ = pi
model.transmat_ = A
model.emissionprob_ = B

# Sample a sequence of hidden states
hidden_states = model.sample(n_samples=10, random_state=42)[0]

# Generate observation sequence based on hidden states
observations = []
for state in hidden_states:
    observation = np.random.choice(num_emissions, p=B[state])
    observations.append(observation)

# Print the generated sequences
print("Hidden states:", hidden_states)
print("Observations:", observations)

# Decode the most likely sequence of hidden states given observations
decoded_states = model.decode(np.array([observations])[0])[1]
print("Decoded hidden states:", decoded_states)

# Alternatively, calculate the probability of the observation sequence
log_prob = model.score(np.array([observations])[0])
print("Log probability of observations:", log_prob)
