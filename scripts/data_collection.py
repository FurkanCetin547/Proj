# src/data_collection.py

import os
import pandas as pd
from imdb import IMDb
from crawlbase import CrawlingAPI
from bs4 import BeautifulSoup

# Initialize the IMDb and Crawlbase API
ia = IMDb()
crawling_api = CrawlingAPI({'token': 'YOUR_CRAWLBASE_TOKEN'})

# List of movie IDs and titles
movie_ids = ['0133093', '1375666', '0468569']
movie_titles = ['Inception', 'The Dark Knight', 'Interstellar']

# Create directories to store the raw data
os.makedirs('data/raw/IMDb', exist_ok=True)
os.makedirs('data/raw/RottenTomatoes', exist_ok=True)

# Function to fetch IMDb data
def fetch_imdb_data():
    movies_metadata = []
    movies_reviews = []
    for movie_id in movie_ids:
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
    movies_metadata = []
    for title in movie_titles:
        search_url = f'https://www.rottentomatoes.com/search?search={title}'
        response = crawling_api.get(search_url)
        if response['headers']['pc_status'] == '200':
            soup = BeautifulSoup(response['body'].decode('utf-8'), 'html.parser')
            movie_link = soup.find('a', class_='unstyled articleLink')
            if movie_link:
                movie_url = 'https://www.rottentomatoes.com' + movie_link['href']
                movie_page_response = crawling_api.get(movie_url)
                if movie_page_response['headers']['pc_status'] == '200':
                    movie_soup = BeautifulSoup(movie_page_response['body'].decode('utf-8'), 'html.parser')
                    metadata = {
                        'title': title,
                        'url': movie_url,
                        'rating': movie_soup.find('span', class_='sc-16ede01-2').text if movie_soup.find('span', class_='sc-16ede01-2') else '',
                        'synopsis': movie_soup.find('span', class_='sc-16ede01-3').text if movie_soup.find('span', class_='sc-16ede01-3') else '',
                        'genres': ', '.join([genre.text for genre in movie_soup.find_all('span', class_='sc-16ede01-4')]),
                        'release_date': movie_soup.find('span', class_='sc-16ede01-5').text if movie_soup.find('span', class_='sc-16ede01-5') else ''
                    }
                    movies_metadata.append(metadata)
    metadata_df = pd.DataFrame(movies_metadata)
    metadata_df.to_csv('data/raw/RottenTomatoes/movies_metadata.csv', index=False)

# Fetch data
fetch_imdb_data()
fetch_rotten_tomatoes_data()
