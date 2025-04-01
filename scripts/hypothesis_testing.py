import pandas as pd
import scipy.stats as stats

# Load dataset
df = pd.read_csv("data/movie_reviews_with_sentiment.csv")

#  Hypothesis 1: Sentiment Trends Over Time
df["year"] = pd.to_datetime(df["release_date"]).dt.year

# Compare older movies (before 2000) vs newer movies (2000+)
old_movies = df[df["year"] < 2000]["sentiment_score"]
new_movies = df[df["year"] >= 2000]["sentiment_score"]

# Perform t-test
t_stat, p_value = stats.ttest_ind(old_movies, new_movies, nan_policy='omit')

print("\n Hypothesis 1: Sentiment Trends Over Time")
print(f"T-statistic: {t_stat:.4f}, P-value: {p_value:.4f}")

if p_value < 0.05:
    print(" Reject H₀: Movie review sentiment HAS changed over time.")
else:
    print("Fail to reject H₀: No significant change in sentiment over time.")


#  Hypothesis 2: Sentiment Differences Across Genres
df.dropna(subset=["genre"], inplace=True)

# Get sentiment scores grouped by genre
genre_groups = [df[df["genre"] == g]["sentiment_score"] for g in df["genre"].unique()]

# Perform ANOVA test
anova_stat, anova_p = stats.f_oneway(*genre_groups)

print("\n Hypothesis 2: Genre-Based Sentiment Differences")
print(f"ANOVA F-statistic: {anova_stat:.4f}, P-value: {anova_p:.4f}")

if anova_p < 0.05:
    print(" Reject H₀: There ARE significant differences in sentiment across genres.")
else:
    print(" Fail to reject H₀: No significant sentiment differences between genres.")

