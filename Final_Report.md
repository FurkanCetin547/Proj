# 📝 Final Report – Movie Review Sentiment & Genre Classification Analysis  
**Furkan Çetin**

---

## 1. 🎯 Project Motivation

This project focuses on two main predictive tasks:

- **Sentiment Classification**: Can we predict whether a Rotten Tomatoes movie review is “Fresh” or “Rotten” using text data?
- **Genre Classification**: Can we accurately predict whether a movie belongs to the **Action** genre using features such as IMDb average rating, title length, and number of votes?

Understanding how sentiment can be extracted from review content and how genre can be inferred from movie metadata provides valuable insights for recommender systems and media analysis.

---

## 2. 🗂️ Data Sources & Preprocessing

**Datasets Used:**

- `title.basics.tsv.gz` and `title.ratings.tsv.gz` from IMDb (for metadata and ratings)
- Rotten Tomatoes review dataset (text reviews and Fresh/Rotten labels)

**Cleaning & Feature Engineering:**

- Dropped rows with missing values (`genres`, `averageRating`, `numVotes`)
- Converted genre field to lists and used `.explode()` to separate multiple genres
- For **genre classification**, engineered features like:
  - `title_length`: character count of movie titles
  - `word_count`: number of words in movie titles
- For **sentiment analysis**, performed:
  - TF-IDF vectorization on review text
  - Removed punctuation and converted text to lowercase

---

## 3. 📊 Exploratory Data Analysis

- Visualized **average rating per genre** and **vote counts**
- Observed that **Action**, **Adventure**, and **Sci-Fi** genres often had higher vote counts but not always highest ratings.
- Rotten Tomatoes reviews were imbalanced with more “Fresh” than “Rotten” reviews.

---

## 4. 🧪 Hypothesis Testing

**Null Hypothesis (H0):** There is no difference in average IMDb rating between Action and Non-Action movies.

- **Method**: Used permutation testing (resampling-based hypothesis test)
- **Result**: p-value < 0.001 → Reject H0  
  ⇒ Action movies tend to have statistically different ratings from others.

---

## 5. 🧠 Machine Learning Models

### 5.1 Sentiment Classification

| Model                | Accuracy | Notes                                 |
|---------------------|----------|----------------------------------------|
| Naive Bayes         | ~73%     | Baseline model, fast and interpretable |
| Logistic Regression | ~76%     | Better performance with TF-IDF         |
| Random Forest       | ~74%     | Slightly better recall, slower fit     |

➡️ Logistic Regression performed best overall with balanced precision and recall.

---

### 5.2 Genre Classification (Predicting Action Genre)

| Model                | Accuracy | Precision (Action) | Recall (Action) | F1 (Action) |
|---------------------|----------|---------------------|------------------|-------------|
| Logistic Regression | ~68%     | 0.55                | 0.43             | 0.48        |
| Random Forest       | ~72%     | 0.62                | 0.51             | 0.56        |

➡️ Random Forest significantly improved genre classification performance, especially on the minority *Action* class. Additional features like vote count and title length helped boost accuracy.

---

## 6. 📘 Findings / Insights

- **Text-based sentiment analysis** is effective using word-based models like TF-IDF + Logistic Regression.
- **Genre classification** works better with engineered features and ensemble models like Random Forest.
- **Action genre** is harder to predict due to class imbalance and feature similarity with other genres.
- Adding features like review length or genre-specific keywords could further improve prediction performance.

---

## 7. 🔧 Tools & Reproducibility

- Python (pandas, NumPy, scikit-learn, seaborn, matplotlib, VADER)
- Jupyter Notebook environment
- GitHub repository ensures full reproducibility

---

## 8. 🔗 GitHub Repository

📁 [Project Files on GitHub](https://github.com/FurkanCetin547/Proj)
