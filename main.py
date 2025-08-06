from classifier.tfidf_classifier import TFIDFNewsClassifier

def read_articles(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        return f.read().strip().split('\n\n')  # Split articles by blank lines

if __name__ == "__main__":
    articles = read_articles("data/articles.txt")
    classifier = TFIDFNewsClassifier("data/categories.json")

    for i, article in enumerate(articles):
        result = classifier.classify(article, top_n=2)
        print(f"\n📝 Article {i+1}:")
        for category, score in result:
            print(f"  ➤ {category} (score: {score:.4f})")
