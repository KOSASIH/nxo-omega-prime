import sqlite3
import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.preprocessing import LabelEncoder
import json
import logging

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class DialectRecognition:
    def __init__(self, db_path):
        self.db_path = db_path
        self.connection = sqlite3.connect(self.db_path)
        self.vectorizer = TfidfVectorizer()
        self.dialect_profiles = self.load_dialect_profiles()
        self.dialect_features = self.load_dialect_features()

    def load_dialect_profiles(self):
        query = "SELECT id, dialect_name, phonetic_profile, lexical_profile, grammatical_profile FROM dialect_profiles"
        return pd.read_sql_query(query, self.connection)

    def load_dialect_features(self):
        query = "SELECT dialect_id, feature_type, feature_name, feature_description FROM dialect_features"
        return pd.read_sql_query(query, self.connection)

    def preprocess_input(self, input_text):
        # Preprocess the input text (tokenization, normalization, etc.)
        return input_text.lower()

    def recognize_dialect(self, input_text):
        processed_text = self.preprocess_input(input_text)
        logging.info(f"Processing input text: {processed_text}")

        # Create a TF-IDF matrix for the dialect profiles
        tfidf_matrix = self.vectorizer.fit_transform(self.dialect_profiles['phonetic_profile'])
        input_vector = self.vectorizer.transform([processed_text])

        # Calculate cosine similarity
        similarities = cosine_similarity(input_vector, tfidf_matrix).flatten()
        best_match_index = np.argmax(similarities)

        # Get the best matching dialect
        best_dialect = self.dialect_profiles.iloc[best_match_index]
        logging.info(f"Best matching dialect: {best_dialect['dialect_name']} with similarity score: {similarities[best_match_index]}")

        return best_dialect

    def get_dialect_features(self, dialect_id):
        features = self.dialect_features[self.dialect_features['dialect_id'] == dialect_id]
        return features.to_dict(orient='records')

    def close_connection(self):
        self.connection.close()

if __name__ == "__main__":
    # Example usage
    db_path = 'path/to/dialectProfiles.db'  # Update with the actual path to your database
    recognizer = DialectRecognition(db_path)

    input_text = "Your input text here"  # Replace with actual input
    best_dialect = recognizer.recognize_dialect(input_text)

    # Fetch and display features of the recognized dialect
    dialect_features = recognizer.get_dialect_features(best_dialect['id'])
    print(json.dumps(dialect_features, indent=4))

    recognizer.close_connection()
