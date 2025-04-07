import pandas as pd
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import nltk
nltk.download("vader_lexicon")

reviews = pd.read_csv("data/processed/user_reviews.csv")
sid = SentimentIntensityAnalyzer()

def score_sentiment(text):
    return sid.polarity_scores(text)["compound"]

reviews["sentiment_score"] = reviews["review"].apply(score_sentiment)
reviews["sentiment_label"] = reviews["sentiment_score"].apply(
    lambda x: "positive" if x > 0.05 else ("negative" if x < -0.05 else "neutral")
)

reviews.to_csv("data/processed/reviews_with_sentiment.csv", index=False)
