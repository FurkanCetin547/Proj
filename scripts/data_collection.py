# src/data_collection.py

import os
import pandas as pd
from imdb import IMDb
import requests
from bs4 import BeautifulSoup

# Create necessary directories
os.makedirs('data/raw/IMDb', exist_ok=True)
os.makedirs('data/raw/RottenTomatoes', exist_ok=True)

# Initialize IMDb object
ia = IMDb()

# List of IMDb movie IDs to scrape
imdb_movie_ids = ['0133093', '1375666', '0468569']  # Example IDs

# Function to fetch IMDb data
def fetch_imdb_data():
    movies_metadata = []
    movies_reviews = []
    for movie_id in imdb_movie_ids:
        movie = ia.get_movie(movie_id)
        metadata = {
            'movie_id': movie_id,
            'title': movie.get('title', ''),
            'year': movie.get('year', ''),
            'genres': ', '.join(movie.get('genres', [])),
            'rating': movie.get('rating', ''),
            'votes': movie.get('votes', ''),
            'plot': movie.get('plot', [''])[0]
        }
        movies_metadata.append(metadata)
        ia.update(movie, 'reviews')
        reviews = movie.get('reviews', [])
        for review in reviews:
            review_data = {
                'movie_id': movie_id,
                'reviewer': review.get('author', ''),
                'date': review.get('date', ''),
                'rating': review.get('rating', ''),
                'text': review.get('text', '')
            }
            movies_reviews.append(review_data)
    metadata_df = pd.DataFrame(movies_metadata)
    reviews_df = pd.DataFrame(movies_reviews)
    metadata_df.to_csv('data/raw/IMDb/movies_metadata.csv', index=False)
    reviews_df.to_csv('data/raw/IMDb/movies_reviews.csv', index=False)

# Function to fetch Rotten Tomatoes data
def fetch_rotten_tomatoes_data():
    url = 'https://www.rottentomatoes.com/top/bestofrt/top_100_action__adventure_movies/'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    movies = soup.select('td.titleColumn')
    movie_data = []
    for movie in movies:
        title = movie.select('a')[0].text
        year = movie.select('span.secondaryInfo')[0].text.strip('()')
        rating = movie.select('span.tMeterScore')[0].text.strip()
        movie_data.append({
            'title': title,
            'year': year,
            'rating': rating
        })
    df = pd.DataFrame(movie_data)
    df.to_csv('data/raw/RottenTomatoes/movies_metadata.csv', index=False)

# Fetch data
fetch_imdb_data()
fetch_rotten_tomatoes_data()
