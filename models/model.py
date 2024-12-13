import joblib
import logging
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split
import os

def train_model():
    """
    Trains the cyberattack classifier model and saves it
    """
    logging.info('Starting Model Training..')
    # get the absolute path of this directory
    model_dir = os.path.dirname(__file__)
    # get the path to the csv file
    csv_path = os.path.join(model_dir, '../data/attack_data.csv')
    # Load Data.
    try:
        data = pd.read_csv(csv_path)
    except Exception as e:
        logging.error(f'Error loading the csv: {e}')
        return None
    #split into train and test
    X_train,X_test,y_train,y_test = train_test_split(data['description'],data['label'],test_size=0.2)
    # Build the model
    text_clf = Pipeline([
    ('tfidf', TfidfVectorizer()),
    ('clf', MultinomialNB())])
    #train model
    text_clf.fit(X_train,y_train)
    # get path to the model file
    model_path = os.path.join(model_dir, 'cyberattack_classifier.pkl')
    # Save the model
    try:
         joblib.dump(text_clf, model_path)
         logging.info(f'Successfully saved the model to {model_path}')
         return text_clf
    except Exception as e:
        logging.error(f"Error saving model: {e}")
        return None


def load_model():
    """
    Loads the trained model.
    """
    model_dir = os.path.dirname(__file__)
    model_path = os.path.join(model_dir, 'cyberattack_classifier.pkl')
    try:
         model = joblib.load(model_path)
         logging.info(f'Successfully loaded the model from {model_path}')
         return model
    except Exception as e:
        logging.error(f"Error loading model: {e}")
        return None

if __name__ == '__main__':
    # Train and save the model if this script is run directly.
     logging.basicConfig(level=logging.DEBUG)
     train_model()