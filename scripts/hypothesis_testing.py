# hypothesis_testing.py
import pandas as pd
import scipy.stats as stats
import statsmodels.api as sm
from statsmodels.formula.api import ols
import numpy as np

def load_data(file_path='data/reviews_with_sentiment.csv'):
    return pd.read_csv(file_path)

def test_sentiment_trend(df, time_column='year'):
    """Test if sentiment changes significantly over time"""
    # Group by year and get average sentiment
    yearly = df.groupby(time_column)['sentiment'].mean().reset_index()
    
    # Pearson correlation test
    corr, p_value = stats.pearsonr(yearly[time_column], yearly['sentiment'])
    
    print(f"Correlation between year and sentiment: {corr:.3f}")
    print(f"P-value: {p_value:.4f}")
    
    if p_value < 0.05:
        print("Statistically significant correlation found between year and sentiment")
    else:
        print("No significant correlation found between year and sentiment")

def test_genre_differences(df, genre_column='genre'):
    """ANOVA test for sentiment differences across genres"""
    # Select top N genres for meaningful comparison
    top_genres = df[genre_column].value_counts().head(5).index
    genre_subset = df[df[genre_column].isin(top_genres)]
    
    # Perform ANOVA
    model = ols('sentiment ~ C(' + genre_column + ')', data=genre_subset).fit()
    anova_table = sm.stats.anova_lm(model, typ=2)
    
    print("\nANOVA results for genre differences:")
    print(anova_table)
    
    p_value = anova_table['PR(>F)'][0]
    if p_value < 0.05:
        print("\nStatistically significant differences found between genres")
        
        # Post-hoc tests
        print("\nPost-hoc pairwise comparisons (Tukey HSD):")
        from statsmodels.stats.multicomp import pairwise_tukeyhsd
        tukey = pairwise_tukeyhsd(endog=genre_subset['sentiment'],
                                 groups=genre_subset[genre_column],
                                 alpha=0.05)
        print(tukey)
    else:
        print("\nNo significant differences found between genres")

def perform_hypothesis_tests():
    df = load_data()
    
    if 'year' in df.columns:
        test_sentiment_trend(df)
    
    if 'genre' in df.columns:
        test_genre_differences(df)

if __name__ == "__main__":
    perform_hypothesis_tests()
