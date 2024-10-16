import sqlite3
import logging
import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import json

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class LanguageDetection:
    def __init__(self, db_path):
        self.db_path = db_path
        self.connection = sqlite3.connect(self.db_path)
        self.model = None
        self.languages = self.load_languages()
        self.train_model()

    def load_languages(self):
        """Load language data from the database."""
        query = "SELECT id, language_name, sample_text FROM languages"
        languages_df = pd.read_sql_query(query, self.connection)
        return languages_df

    def train_model(self):
        """Train a language detection model using Naive Bayes."""
        logging.info("Training language detection model...")
        X = self.languages['sample_text']
        y = self.languages['language_name']

        # Split the data into training and testing sets
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        # Create a pipeline with CountVectorizer and MultinomialNB
        self.model = make_pipeline(CountVectorizer(), MultinomialNB())
        self.model.fit(X_train, y_train)

        # Evaluate the model
        predictions = self.model.predict(X_test)
        accuracy = accuracy_score(y_test, predictions)
        logging.info(f"Model trained with accuracy: {accuracy:.2f}")

    def detect_language(self, text):
        """Detect the language of the given text."""
        logging.info(f"Detecting language for input text: {text}")
        predicted_language = self.model.predict([text])[0]
        logging.info(f"Detected language: {predicted_language}")
        return predicted_language

    def close_connection(self):
        """Close the database connection."""
        self.connection.close()
        logging.info("Database connection closed.")

if __name__ == "__main__":
    # Example usage
    db_path = 'path/to/languages.db'  # Update with the actual path to your database
    language_detector = LanguageDetection(db_path)

    # Input text for language detection
    input_text = "Bonjour, comment ça va?"  # Replace with actual input
    detected_language = language_detector.detect_language(input_text)
    print(f"Detected Language: {detected_language}")

    language_detector.close_connection()
