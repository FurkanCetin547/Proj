# Sample genre list to focus on (modify based on your data)
MAIN_GENRES = [
    'Drama', 'Comedy', 'Action', 
    'Horror', 'Sci-Fi', 'Romance'
]

# Time periods to analyze
TIME_PERIODS = {
    '1990s': (1990, 1999),
    '2000s': (2000, 2009),
    '2010s': (2010, 2019),
    '2020s': (2020, 2023)
}

def plot_sentiment_vs_rating(df):
    """Plot sentiment vs IMDB rating if available"""
    if 'rating' in df.columns:
        plt.figure(figsize=(10, 6))
        sns.regplot(x='rating', y='sentiment', data=df)
        plt.title('Sentiment vs Movie Rating')
        plt.savefig('plots/sentiment_vs_rating.png')
        plt.close()
