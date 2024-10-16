import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from inferenceRules import InferenceRules

class PragmaticInference:
    def __init__(self, inference_rules):
        self.inference_rules = inference_rules
        self.vectorizer = TfidfVectorizer()
        self.lemmatizer = WordNetLemmatizer()
        self.stop_words = set(stopwords.words('english'))

    def preprocess_text(self, text):
        tokens = word_tokenize(text)
        tokens = [token for token in tokens if token.isalpha()]
        tokens = [token for token in tokens if token not in self.stop_words]
        tokens = [self.lemmatizer.lemmatize(token) for token in tokens]
        return ' '.join(tokens)

    def calculate_similarity(self, text1, text2):
        vector1 = self.vectorizer.fit_transform([text1])
        vector2 = self.vectorizer.transform([text2])
        return cosine_similarity(vector1, vector2)[0][0]

    def infer_meaning(self, text, context):
        preprocessed_text = self.preprocess_text(text)
        context_vector = self.vectorizer.fit_transform([context])
        text_vector = self.vectorizer.transform([preprocessed_text])
        similarity = cosine_similarity(context_vector, text_vector)[0][0]
        if similarity > 0.5:
            return self.inference_rules.get_inferred_meaning(text, context)
        else:
            return "No inferred meaning found"

    def get_inferred_meaning(self, text, context):
        inferred_meaning = self.infer_meaning(text, context)
        if inferred_meaning:
            return inferred_meaning
        else:
            return "No inferred meaning found"

# Load inference rules from database
inference_rules = InferenceRules()
inference_rules.load_rules()

# Create pragmatic inference engine
pragmatic_inference = PragmaticInference(inference_rules)

# Test pragmatic inference engine
text = "Zhrak zhilak, my friend!"
context = "Formal greeting in the morning"
inferred_meaning = pragmatic_inference.get_inferred_meaning(text, context)
print(inferred_meaning)
