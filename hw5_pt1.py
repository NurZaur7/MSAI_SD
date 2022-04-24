import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.utils import shuffle

from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC

from sklearn.metrics import accuracy_score

random_state = 50


class CreationalPatternName:

    def __init__(self, X_train, y_train):
        self.X_train = X_train
        self.y_train = y_train

    def get_subsample(self, df_share):
        """
        1. Copy train dataset
        2. Shuffle data (don't miss the connection between X_train and y_train)
        3. Return df_share %-subsample of X_train and y_train
        """
        X = self.X_train.copy()
        y = self.y_train.copy()

        X, y = shuffle(X, y, random_state=random_state)

        num_to_take = int(len(y) * df_share / 100.0)

        return X[:num_to_take, :], y[:num_to_take]
  

if __name__ == "__main__":
    """
    1. Load iris dataset
    2. Shuffle data and divide into train / test.
    """
    train_size = 0.7

    X, y = load_iris(return_X_y=True)
    X, y = shuffle(X, y, random_state=random_state)

    num_train = int(len(y) * train_size)

    X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=train_size, random_state=random_state)


    """
    1. Preprocess curr_X_train, curr_y_train in the way you want
    2. Train Linear Regression on the subsample
    3. Save or print the score to check how df_share affects the quality
    """
    clf = make_pipeline(StandardScaler(), SVC(gamma='auto'))

    pattern_item = CreationalPatternName(X_train, y_train)
    for df_share in range(5, 101, 15):
        curr_X_train, curr_y_train = pattern_item.get_subsample(df_share)

        clf.fit(curr_X_train, curr_y_train)

        y_test_pred = clf.predict(X_test)

        accuracy = accuracy_score(y_test, y_test_pred)

        print(f"df_share = {df_share}%, accuracy = {round(accuracy, 4)}")


##################################
#df_share = 5%, accuracy = 0.6222
#df_share = 20%, accuracy = 0.9111
#df_share = 35%, accuracy = 0.8889
#df_share = 50%, accuracy = 0.9556
#df_share = 65%, accuracy = 0.9556
#df_share = 80%, accuracy = 0.9556
#df_share = 95%, accuracy = 0.9556
