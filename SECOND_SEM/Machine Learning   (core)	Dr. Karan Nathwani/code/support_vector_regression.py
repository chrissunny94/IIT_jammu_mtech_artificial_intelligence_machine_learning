from sklearn.svm import SVR

# Create SVR model
svr = SVR(kernel='linear')
svr.fit(X_train, y_train)

# Predict and evaluate
y_pred = svr.predict(X_test)
print("Mean Squared Error:", np.mean((y_pred - y_test) ** 2))
