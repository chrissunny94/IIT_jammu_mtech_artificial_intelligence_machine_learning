from sklearn.linear_model import Perceptron

# Create perceptron classifier
perceptron = Perceptron()
perceptron.fit(X_train, y_train)

# Predict and evaluate
y_pred = perceptron.predict(X_test)
print("Accuracy:", accuracy_score(y_test, y_pred))
