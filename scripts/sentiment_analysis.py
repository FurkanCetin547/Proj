from textblob import TextBlob
import pandas as pd

def analyze_sentiment(text):
    """ Returns sentiment score (-1 to 1) for a given text. """
    return TextBlob(text).sentiment.polarity

# Apply sentiment analysis to dataset
if __name__ == "__main__":
    df = pd.read_csv("data/movie_reviews.csv")
    df["sentiment_score"] = df["review_text"].apply(analyze_sentiment)
    df.to_csv("data/movie_reviews_with_sentiment.csv", index=False)
    print("Sentiment analysis complete. Results saved.")

