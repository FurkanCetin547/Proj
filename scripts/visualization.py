import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

sentiment_data = pd.read_csv("data/processed/reviews_with_sentiment.csv")
meta = pd.read_csv("data/processed/movie_metadata.csv")
merged = pd.merge(sentiment_data, meta, on="title")

def visualize_sentiment_trends():
    year_sentiment = merged.groupby("year")["sentiment_score"].mean().reset_index()
    sns.lineplot(data=year_sentiment, x="year", y="sentiment_score")
    plt.title("Sentiment Trend Over Time")
    plt.savefig("outputs/sentiment_trend.png")

def genre_boxplot():
    genre_df = merged.explode("genres")
    sns.boxplot(data=genre_df, x="genres", y="sentiment_score")
    plt.xticks(rotation=45)
    plt.title("Sentiment Distribution by Genre")
    plt.tight_layout()
    plt.savefig("outputs/sentiment_by_genre.png")

if __name__ == "__main__":
    visualize_sentiment_trends()
    genre_boxplot()
