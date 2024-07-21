import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import Perceptron
from sklearn.svm import SVC, SVR
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import AdaBoostClassifier
from sklearn.mixture import GaussianMixture
from pgmpy.models import BayesianNetwork
from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import VariableElimination
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.decomposition import PCA
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense


# Module 1: Nearest Neighbor (k-NN)
def knn_example():
    X = np.array([[1, 2], [2, 3], [3, 4], [4, 5], [5, 6]])
    y = np.array([0, 0, 1, 1, 1])
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    knn = KNeighborsClassifier(n_neighbors=3)
    knn.fit(X_train, y_train)
    y_pred = knn.predict(X_test)
    print("k-NN Accuracy:", accuracy_score(y_test, y_pred))


# Module 1: Decision Trees
def decision_tree_example():
    X = np.array([[1, 2], [2, 3], [3, 4], [4, 5], [5, 6]])
    y = np.array([0, 0, 1, 1, 1])
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    dt = DecisionTreeClassifier()
    dt.fit(X_train, y_train)
    y_pred = dt.predict(X_test)
    print("Decision Tree Accuracy:", accuracy_score(y_test, y_pred))


# Module 1: Perceptron
def perceptron_example():
    X = np.array([[1, 2], [2, 3], [3, 4], [4, 5], [5, 6]])
    y = np.array([0, 0, 1, 1, 1])
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    perceptron = Perceptron()
    perceptron.fit(X_train, y_train)
    y_pred = perceptron.predict(X_test)
    print("Perceptron Accuracy:", accuracy_score(y_test, y_pred))


# Module 1: Support Vector Machines (SVM)
def svm_example():
    X = np.array([[1, 2], [2, 3], [3, 4], [4, 5], [5, 6]])
    y = np.array([0, 0, 1, 1, 1])
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    svm = SVC(kernel='linear')
    svm.fit(X_train, y_train)
    y_pred = svm.predict(X_test)
    print("SVM Accuracy:", accuracy_score(y_test, y_pred))


# Module 2: Linear Least Squares Regression
def linear_regression_example():
    X = np.array([[1], [2], [3], [4], [5]])
    y = np.array([1, 3, 2, 3, 5])
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    lr = LinearRegression()
    lr.fit(X_train, y_train)
    y_pred = lr.predict(X_test)
    print("Linear Regression Mean Squared Error:", np.mean((y_pred - y_test) ** 2))


# Module 2: Support Vector Regression (SVR)
def svr_example():
    X = np.array([[1], [2], [3], [4], [5]])
    y = np.array([1, 3, 2, 3, 5])
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    svr = SVR(kernel='linear')
    svr.fit(X_train, y_train)
    y_pred = svr.predict(X_test)
    print("SVR Mean Squared Error:", np.mean((y_pred - y_test) ** 2))


# Module 3: Boosting
def boosting_example():
    X = np.array([[1, 2], [2, 3], [3, 4], [4, 5], [5, 6]])
    y = np.array([0, 0, 1, 1, 1])
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    boost = AdaBoostClassifier(n_estimators=100)
    boost.fit(X_train, y_train)
    y_pred = boost.predict(X_test)
    print("Boosting Accuracy:", accuracy_score(y_test, y_pred))


# Module 3: Gaussian Mixture Model (GMM)
def gmm_example():
    X = np.array([[1], [2], [3], [4], [5], [6], [7], [8], [9], [10]])
    gmm = GaussianMixture(n_components=2)
    gmm.fit(X)
    probs = gmm.predict_proba(X)
    print("GMM Probabilities:\n", probs)


# Module 4: Bayesian Networks
def bayesian_network_example():
    model = BayesianNetwork([('A', 'B'), ('B', 'C')])
    cpd_a = TabularCPD(variable='A', variable_card=2, values=[[0.6], [0.4]])
    cpd_b = TabularCPD(variable='B', variable_card=2, values=[[0.7, 0.2], [0.3, 0.8]], evidence=['A'], evidence_card=[2])
    cpd_c = TabularCPD(variable='C', variable_card=2, values=[[0.9, 0.4], [0.1, 0.6]], evidence=['B'], evidence_card=[2])
    model.add_cpds(cpd_a, cpd_b, cpd_c)
    inference = VariableElimination(model)
    result = inference.query(variables=['C'], evidence={'A': 0})
    print(result)


# Module 5: Fisher Discriminant Analysis
def fisher_discriminant_example():
    X = np.array([[1, 2], [2, 3], [3, 4], [4, 5], [5, 6]])
    y = np.array([0, 0, 1, 1, 1])
    lda = LinearDiscriminantAnalysis()
    lda.fit(X, y)
    X_transformed = lda.transform(X)
    print("Fisher Discriminant Analysis Transformed Data:\n", X_transformed)


# Module 5: Principal Component Analysis (PCA)
def pca_example():
    X = np.array([[1, 2], [2, 3], [3, 4], [4, 5], [5, 6]])
    pca = PCA(n_components=1)
    X_pca = pca.fit_transform(X)
    print("PCA Result:\n", X_pca)


# Module 6: Gradient Descent
def gradient_descent_example():
    X = np.array([[1, 1], [1, 2], [2, 2], [2, 3]])
    y = np.array([6, 8, 9, 11])
    theta = np.random.randn(2)
    alpha = 0.01
    num_iterations = 1000
    for _ in range(num_iterations):
        gradient = np.dot(X.T, (np.dot(X, theta) - y)) / len(y)
        theta -= alpha * gradient
    print("Learned Parameters:", theta)


# Module 7: Deep Learning
def deep_learning_example():
    X = np.array([[1, 2], [2, 3], [3, 4], [4, 5], [5, 6]])
    y = np.array([0, 0, 1, 1, 1])
    model = Sequential()
    model.add(Dense(10, input_dim=2, activation='relu'))
    model.add(Dense(1, activation='sigmoid'))
    model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
    model.fit(X, y, epochs=100, verbose=0)
    predictions = model.predict(X)
    print("Deep Learning Predictions:\n", predictions)


# Run all examples
if __name__ == "__main__":
    print("Module 1: Nearest Neighbor (k-NN)")
    knn_example()
    print("\nModule 1: Decision Trees")
    decision_tree_example()
    print("\nModule 1: Perceptron")
    perceptron_example()
    print("\nModule 1: Support Vector Machines (SVM)")
    svm_example()
    print("\nModule 2: Linear Least Squares Regression")
    linear_regression_example()
    print("\nModule 2: Support Vector Regression (SVR)")
    svr_example()
    print("\nModule 3: Boosting")
    boosting_example()
    print("\nModule 3: Gaussian Mixture Model (GMM)")
    gmm_example()
    print("\nModule 4: Bayesian Networks")
    bayesian_network_example()
    print("\nModule 5: Fisher Discriminant Analysis")
    fisher_discriminant_example()
    print("\nModule 5: Principal Component Analysis (PCA)")
    pca_example()
    print("\nModule 6: Gradient Descent")
    gradient_descent_example()
    print("\nModule 7: Deep Learning")
    deep_learning_example()
