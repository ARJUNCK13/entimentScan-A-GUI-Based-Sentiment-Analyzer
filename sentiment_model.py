import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline
import joblib


def train_model():
    # Load the dataset
    data = pd.read_csv("data.csv")

    # Create a pipeline (Vectorizer + Classifier)
    model = make_pipeline(CountVectorizer(), MultinomialNB())

    # Train the model
    model.fit(data['text'], data['label'])

    # Save the model
    joblib.dump(model, "sentiment_model.pkl")
    print("Model trained and saved as 'sentiment_model.pkl'")


def load_model():
    return joblib.load("sentiment_model.pkl")
