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

        # Splits the data set into 2 datasets, train and test
        data = train_test_split(self.df['text'], self.df.label, test_size=0.2, random_state=7)

        # Define training and test dataset variables
        self.x_train = data[0]
        self.x_test = data[1]
        self.y_train = data[2]
        self.y_test = data[3]

    def train(self):
        # TDIFVectorizer:

        # The tfidf vectorizer counts the term frequency (tf) per document and balances it with the inverse of the
        # global frequency of the term, leaving us a weighted list key terms from each document.

        # The two parameters, 1. stop_words='english'  and 2. max_df=0.7, are used to 1. filter out the most commonly
        # used terms ('a', 'the', etc.) and 2. filter out words with a higher document frequency than 0.7.
        self.tfidf_vectorizer = TfidfVectorizer(stop_words='english', max_df=0.7)

        # PassiveAggressiveClassifier:

        # The passive aggressive classifier algorithm remains passive for a correct classification outcome, and turns
        # aggressive in the event of a miscalculation
        self.pac = PassiveAggressiveClassifier(max_iter=50)

        # Load the training input data and run the learning algorithm
        self.tfidf_train = self.tfidf_vectorizer.fit_transform(self.x_train)
        self.pac.fit(self.tfidf_train, self.y_train)

        # Create a test dataset using the tfdif vectorizer
        self.tfidf_test = self.tfidf_vectorizer.transform(self.x_test)

    def predict(self):
        # Test the accuracy of the model
        # Use pac.predict to predict the validity of each article in the dataset
        self.y_pred = self.pac.predict(self.tfidf_test)
        # Compare the predicted output values and the actual values to get an accuracy score
        score = accuracy_score(self.y_test, self.y_pred)


        print(f'Accuracy: {round(score * 100, 2)}%')

        # Build confusion matrix
        conf = confusion_matrix(self.y_test, self.y_pred, labels=['FAKE', 'REAL'])
        print('True positives = {}\nTrue negatives = {}\nFalse positives = {}\nFalse negatives = {}'
              .format(conf[0][0], conf[1][1], conf[1][0], conf[0][1]))


myClassifier = NewsClassifier('news.csv')
myClassifier.train()
myClassifier.predict()
