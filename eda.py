import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("data/movie_reviews_with_sentiment.csv")

# Histogram of sentiment scores
sns.histplot(df["sentiment_score"], bins=20, kde=True)
plt.title("Sentiment Score Distribution")
plt.xlabel("Sentiment Score")
plt.ylabel("Count")
plt.show()

# Save figure
plt.savefig("visualizations/sentiment_distribution.png")

