from sklearn.linear_model import LinearRegression

# Sample data for regression
X = np.array([[1], [2], [3], [4], [5]])
y = np.array([1, 3, 2, 3, 5])

# Create linear regression model
lr = LinearRegression()
lr.fit(X_train, y_train)

# Predict and evaluate
y_pred = lr.predict(X_test)
print("Mean Squared Error:", np.mean((y_pred - y_test) ** 2))
