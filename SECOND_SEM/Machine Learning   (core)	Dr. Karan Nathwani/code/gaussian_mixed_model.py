from sklearn.mixture import GaussianMixture

# Sample data for GMM
X = np.array([[1], [2], [3], [4], [5], [6], [7], [8], [9], [10]])

# Create GMM
gmm = GaussianMixture(n_components=2)
gmm.fit(X)

# Predict probabilities
probs = gmm.predict_proba(X)
print("Probabilities:\n", probs)
