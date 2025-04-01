# Project configuration
CONFIG = {
    'data_sources': {
        'imdb': True,
        'rotten_tomatoes': False,  # Needs API
        'tmdb_metadata': True      # Needs API
    },
    'analysis_years': (1990, 2023),
    'main_genres': ['Drama', 'Comedy', 'Action', 'Horror', 'Sci-Fi']
}

def main():
    print("Starting movie sentiment analysis pipeline...")
    
    # 1. Data Collection
    print("\n=== Data Collection ===")
    df = data_collection.collect_data()
    
    # 2. Sentiment Analysis
    print("\n=== Sentiment Analysis ===")
    df = sentiment_analysis.add_sentiment_scores(df)
    
    # 3. EDA
    print("\n=== Exploratory Data Analysis ===")
    eda.perform_eda(df)
    
    # 4. Hypothesis Testing
    print("\n=== Hypothesis Testing ===")
    hypothesis_testing.perform_hypothesis_tests(df)
    
    print("\nAnalysis complete! Check the plots/ and data/ folders for results.")

if __name__ == "__main__":
    main()
