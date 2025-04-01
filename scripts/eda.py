# eda.py
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime

def load_data(file_path='data/reviews_with_sentiment.csv'):
    return pd.read_csv(file_path)

def basic_eda(df):
    """Perform basic exploratory data analysis"""
    print("Data shape:", df.shape)
    print("\nData types:\n", df.dtypes)
    print("\nMissing values:\n", df.isnull().sum())
    print("\nBasic statistics:\n", df.describe())

def plot_sentiment_over_time(df, time_column='year'):
    """Plot sentiment trends over time"""
    plt.figure(figsize=(12, 6))
    sns.lineplot(data=df, x=time_column, y='sentiment', ci=None)
    plt.title('Sentiment Trends Over Time')
    plt.ylabel('Average Sentiment Score')
    plt.xlabel('Year')
    plt.grid(True)
    plt.savefig('plots/sentiment_over_time.png')
    plt.close()

def plot_genre_sentiment(df, genre_column='genre'):
    """Compare sentiment across genres"""
    plt.figure(figsize=(12, 6))
    sns.boxplot(data=df, x=genre_column, y='sentiment')
    plt.title('Sentiment Distribution by Genre')
    plt.xticks(rotation=45)
    plt.savefig('plots/genre_sentiment.png')
    plt.close()

def perform_eda():
    df = load_data()
    basic_eda(df)
    
    # Ensure proper datetime format if needed
    if 'date' in df.columns:
        df['year'] = pd.to_datetime(df['date']).dt.year
    
    plot_sentiment_over_time(df)
    
    if 'genre' in df.columns:
        plot_genre_sentiment(df)

if __name__ == "__main__":
    perform_eda()
