import numpy as np
import pandas as pd
import itertools
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import PassiveAggressiveClassifier
from sklearn.metrics import accuracy_score, confusion_matrix


class NewsClassifier:

    def __init__(self, dataset):
        # Set up the dataframe with the input dataset
        self.df = pd.read_csv(dataset)

        # Splits the data set into training and test data
        data = train_test_split(self.df['text'], self.df.label, test_size=0.2, random_state=7)
        self.x_train = data[0]
        self.x_test = data[1]
        self.y_train = data[2]
        self.y_test = data[3]

    def train(self):
        # Initialize the TDIFVectorizer
        self.tfidf_vectorizer = TfidfVectorizer(stop_words='english', max_df=0.7)
        # Transform and fit the test and train x data
        self.tfidf_train = self.tfidf_vectorizer.fit_transform(self.x_train)
        self.tfidf_test = self.tfidf_vectorizer.transform(self.x_test)

        # Initialize a PassiveAggressiveClassifier
        self.pac = PassiveAggressiveClassifier(max_iter=50)
        self.pac.fit(self.tfidf_train, self.y_train)

    def predict(self):
        # Predict on the test set and calculate accuracy
        self.y_pred = self.pac.predict(self.tfidf_test)
        score = accuracy_score(self.y_test, self.y_pred)
        print(f'Accuracy: {round(score * 100, 2)}%')

        # Build confusion matrix
        print(confusion_matrix(self.y_test, self.y_pred, labels=['FAKE', 'REAL']))


myClassifier = NewsClassifier('news.csv')
myClassifier.train()
myClassifier.predict()
