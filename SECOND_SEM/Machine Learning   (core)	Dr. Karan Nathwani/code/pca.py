from sklearn.decomposition import PCA

# Sample data for PCA
X = np.array([[1, 2], [2, 3], [3, 4], [4, 5], [5, 6]])

# Create PCA model
pca = PCA(n_components=1)
X_pca = pca.fit_transform(X)
print("PCA result:\n", X_pca)
