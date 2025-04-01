# Sentiment analysis options
SENTIMENT_MODELS = {
    'textblob': TextBlob,
    'vader': SentimentIntensityAnalyzer,  # from nltk.sentiment.vader
    'transformers': 'bert-base-uncased'   # HuggingFace model
}

# Sentiment thresholds (adjust based on your needs)
SENTIMENT_THRESHOLDS = {
    'positive': 0.1,
    'negative': -0.1,
    # Between -0.1 and 0.1 is neutral
}

def analyze_with_vader(text):
    """Alternative sentiment analysis using VADER"""
    from nltk.sentiment.vader import SentimentIntensityAnalyzer
    analyzer = SentimentIntensityAnalyzer()
    return analyzer.polarity_scores(text)['compound']
