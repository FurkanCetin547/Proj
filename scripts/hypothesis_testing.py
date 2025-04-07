import pandas as pd
from scipy.stats import ttest_ind

data = pd.read_csv("data/processed/reviews_with_sentiment.csv")

def genre_vs_sentiment():
    df = pd.read_csv("data/processed/movie_metadata.csv")
    merged = pd.merge(data, df, on="title")
    genres = merged.explode("genres")

    # Compare Drama vs Comedy sentiment
    drama = genres[genres["genres"] == "Drama"]["sentiment_score"]
    comedy = genres[genres["genres"] == "Comedy"]["sentiment_score"]
    stat, p = ttest_ind(drama, comedy, nan_policy='omit')
    print(f"T-test between Drama and Comedy sentiment: p={p:.4f}")

if __name__ == "__main__":
    genre_vs_sentiment()
