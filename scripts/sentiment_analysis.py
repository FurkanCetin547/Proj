# sentiment_analysis.py
from textblob import TextBlob
import pandas as pd
import numpy as np

def analyze_sentiment(text):
    """Perform sentiment analysis on a single review"""
    analysis = TextBlob(text)
    return analysis.sentiment.polarity

def add_sentiment_scores(df, text_column='review'):
    """Add sentiment scores to dataframe"""
    df['sentiment'] = df[text_column].apply(analyze_sentiment)
    
    # Categorize sentiment
    df['sentiment_category'] = pd.cut(df['sentiment'],
                                     bins=[-1, -0.1, 0.1, 1],
                                     labels=['negative', 'neutral', 'positive'])
    return df

if __name__ == "__main__":
    df = pd.read_csv('data/collected_reviews.csv')
    df = add_sentiment_scores(df)
    df.to_csv('data/reviews_with_sentiment.csv', index=False)
