from data_collection import fetch_imdb_reviews
from sentiment_analysis import analyze_sentiment
import pandas as pd

#  Collect Data
reviews = fetch_imdb_reviews("tt0111161")  # Example: The Shawshank Redemption
df = pd.DataFrame({"review_text": reviews})

#  Sentiment Analysis
df["sentiment_score"] = df["review_text"].apply(analyze_sentiment)

#  Save Data
df.to_csv("data/movie_reviews_with_sentiment.csv", index=False)

print("Analysis complete. Check the 'data' folder for results.")

