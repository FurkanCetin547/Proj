# data_collection.py

import os
import pandas as pd
from imdb import IMDb

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

# Fetch data
fetch_imdb_data()



# Function to fetch Rotten Tomatoes data
import requests
from bs4 import BeautifulSoup

def fetch_rotten_tomatoes_data():
    url = 'https://www.rottentomatoes.com/top/bestofrt/'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    movies = soup.find_all('tr', class_='top_movies')
    movie_data = []
    for movie in movies:
        title = movie.find('a', class_='unstyled articleLink').text.strip()
        rating = movie.find('span', class_='tMeterScore').text.strip()
        year = movie.find('span', class_='sc-16ede01-2 fXrQjD').text.strip('()')
        movie_data.append({
            'title': title,
            'year': year,
            'rating': rating
        })
    df = pd.DataFrame(movie_data)
    df.to_csv('data/raw/RottenTomatoes/movies_metadata.csv', index=False)

# Fetch data
fetch_rotten_tomatoes_data()
