from sklearn.ensemble import AdaBoostClassifier

# Create AdaBoost classifier
boost = AdaBoostClassifier(n_estimators=100)
boost.fit(X_train, y_train)

# Predict and evaluate
y_pred = boost.predict(X_test)
print("Accuracy:", accuracy_score(y_test, y_pred))
