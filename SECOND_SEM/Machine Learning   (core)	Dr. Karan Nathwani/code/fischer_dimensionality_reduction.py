from sklearn.discriminant_analysis import LinearDiscriminantAnalysis

# Sample data for classification
X = np.array([[1, 2], [2, 3], [3, 4], [4, 5], [5, 6]])
y = np.array([0, 0, 1, 1, 1])

# Create LDA model
lda = LinearDiscriminantAnalysis()
lda.fit(X, y)

# Transform data
X_transformed = lda.transform(X)
print("Transformed data:\n", X_transformed)
