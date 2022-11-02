from keras.datasets import mnist
from sklearn import svm, preprocessing
import joblib
import pickle

from sklearn.neural_network import MLPClassifier

(X_train, y_train), (X_test, y_test) = mnist.load_data()

X_train = X_train.reshape(X_train.shape[0], -1)
X_test = X_test.reshape(X_test.shape[0], -1)

# X_train = preprocessing.normalize(X_train)
# X_test = preprocessing.normalize(X_test)

def train_model():
    clf = MLPClassifier(alpha=1, max_iter=1000)
    clf.fit(X_train, y_train)

    joblib.dump(clf, "trained_model.joblib")

    return clf
