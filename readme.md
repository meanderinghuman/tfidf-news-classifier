# 📰 TF-IDF News Classifier

A simple Python project that classifies news articles into predefined categories (e.g., **Politics**, **Technology**, **Sports**, **Entertainment**) using **TF-IDF** and **cosine similarity**.

This is a lightweight and interpretable alternative to heavy machine learning models — built entirely from scratch using `scikit-learn`.

---

## 📂 Project Structure

tfidf-news-classifier/
├── classifier/ # Core classification logic
│ ├── init.py
│ └── tfidf_classifier.py
├── data/ # Input data
│ ├── articles.txt # Articles to classify
│ └── categories.json # Category definitions
├── main.py # Entry point
├── requirements.txt # Dependencies
├── .gitignore
└── README.md

## ⚙️ How It Works

1. Predefined categories (like *Politics*, *Sports*) are stored with representative keywords.
2. Articles are vectorized using **TF-IDF**.
3. Similarity between each article and each category is calculated using **cosine similarity**.
4. Top categories are returned as the classification output.

## 🚀 Quick Start

### 1. Clone the repo & navigate

```bash
git clone https://github.com/meanderinghuman/tfidf-news-classifier.git
cd tfidf-news-classifier

2. Setup virtual environment

python3 -m venv venv
source venv/bin/activate

3. Install dependencies

pip install -r requirements.txt

4. Run the classifier

python main.py

Requirements

    Python 3.7+

    scikit-learn

Install via:

pip install -r requirements.txt