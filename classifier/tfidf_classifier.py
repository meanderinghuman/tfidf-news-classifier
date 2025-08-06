import json
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

class TFIDFNewsClassifier:
    def __init__(self, categories_file):
        # Load category descriptions from JSON
        with open(categories_file, 'r', encoding='utf-8') as f:
            self.categories = json.load(f)

        # Setup vectorizer and fit on category descriptions
        self.vectorizer = TfidfVectorizer(stop_words='english')
        self.category_names = list(self.categories.keys())
        self.category_texts = list(self.categories.values())
        self.category_vectors = self.vectorizer.fit_transform(self.category_texts)

    def classify(self, article_text, top_n=1):
        # Transform input article
        article_vector = self.vectorizer.transform([article_text])

        # Compute cosine similarity with all categories
        similarity = cosine_similarity(article_vector, self.category_vectors).flatten()

        # Return top-n most similar categories
        ranked_indices = similarity.argsort()[::-1][:top_n]
        return [(self.category_names[i], similarity[i]) for i in ranked_indices]
