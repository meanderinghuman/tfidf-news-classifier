# 📰 TF-IDF News Classifier 🚀

A lightweight and interpretable news article classifier that categorizes articles using **TF-IDF** and **Cosine Similarity**. This project offers a simple, no-training-needed alternative to complex machine learning models, built from scratch with Python and `scikit-learn`.

![GitHub language count](https://img.shields.io/github/languages/count/meanderinghuman/tfidf-news-classifier?style=for-the-badge)
![GitHub top language](https://img.shields.io/github/languages/top/meanderinghuman/tfidf-news-classifier?style=for-the-badge)
![GitHub license](https://img.shields.io/github/license/meanderinghuman/tfidf-news-classifier?style=for-the-badge&cache_bust=1)
---

## ✨ Features

* **Keyword-Based Classification**: Categorizes articles based on representative keywords you define.
* **Lightweight & Interpretable**: No heavy models or complex training pipelines. The logic is straightforward and easy to understand.
* **Zero Training**: Classifies articles on-the-fly without any pre-training phase.
* **Easily Configurable**: Add, remove, or modify categories and their keywords by editing a simple JSON file.
* **Standard Tooling**: Built with Python and the popular `scikit-learn` library.

---

## ⚙️ How It Works

The classification process is elegant in its simplicity:

1.  **✍️ Define Categories**: You define your categories (e.g., *Politics*, *Technology*, *Sports*) and a list of representative keywords for each in the `data/categories.json` file.
2.  **🔢 Vectorize Content**: Both the input articles and the category keywords are transformed into numerical vectors using the **Term Frequency-Inverse Document Frequency (TF-IDF)** algorithm. This process highlights words that are most significant to a document.
    
3.  **📐 Calculate Similarity**: The **Cosine Similarity** metric is used to measure the angle between each article's vector and each category's vector. A smaller angle implies a higher similarity in content.
4.  **🏆 Classify**: The article is assigned to the category with the highest similarity score.

---

## 🚀 Getting Started

Follow these steps to get the project up and running on your local machine.

### Prerequisites

* Python 3.7+
* Git

### Installation & Setup

```bash
# 1. Clone the repository
git clone [https://github.com/meanderinghuman/tfidf-news-classifier.git](https://github.com/meanderinghuman/tfidf-news-classifier.git)
cd tfidf-news-classifier

# 2. Create and activate a virtual environment (recommended)
python3 -m venv venv
source venv/bin/activate
# On Windows, use: venv\Scripts\activate

# 3. Install the required dependencies
pip install -r requirements.txt

🕹️ Usage
To classify the articles defined in data/articles.txt, simply run the main script:

Bash

python main.py

📂 Project Structure
tfidf-news-classifier/
├── classifier/              # Core classification logic
│   ├── __init__.py
│   └── tfidf_classifier.py
├── data/                    # Input data
│   ├── articles.txt         # Articles to classify (one per line)
│   └── categories.json      # Category definitions with keywords
├── main.py                  # Entry point to run the classifier
├── requirements.txt         # Project dependencies
├── .gitignore
└── README.md
🤝 Contributing
Contributions are welcome! If you have suggestions for improvements or want to add new features, feel free to create an issue or submit a pull request.

📄 License
This project is licensed under the MIT License. See the LICENSE file for details.