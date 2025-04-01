# Sample IMDB dataset URL (from Kaggle)
IMDB_DATASET_URL = "https://www.kaggle.com/datasets/lakshmi25npathi/imdb-dataset-of-50k-movie-reviews"

# Rotten Tomatoes API (you'll need an API key)
RT_API_URL = "https://www.rottentomatoes.com/api/private/v2.0/search/"
RT_API_KEY = "your_api_key_here"  # Register at developer.rottentomatoes.com

# TMDB API for movie metadata
TMDB_API_URL = "https://api.themoviedb.org/3/"
TMDB_API_KEY = "your_tmdb_api_key"  # Register at themoviedb.org

# Sample movie URLs for scraping (if needed)
SAMPLE_MOVIE_URLS = [
    "https://www.imdb.com/title/tt0111161/",  # Shawshank Redemption
    "https://www.rottentomatoes.com/m/the_shawshank_redemption",
    "https://www.imdb.com/title/tt0068646/"   # The Godfather
]

def get_imdb_data():
    """Load IMDB data from CSV or download from Kaggle"""
    try:
        # Option 1: Load from local CSV
        return pd.read_csv("data/imdb_reviews.csv")
    except FileNotFoundError:
        # Option 2: Download from Kaggle (requires kaggle API)
        from kaggle.api.kaggle_api_extended import KaggleApi
        api = KaggleApi()
        api.authenticate()
        api.dataset_download_files('lakshmi25npathi/imdb-dataset-of-50k-movie-reviews', path='data', unzip=True)
        return pd.read_csv("data/IMDB Dataset.csv")
