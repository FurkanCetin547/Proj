import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
import random

def scrape_rotten_tomatoes(movie_id):
    """
    Scrape reviews from Rotten Tomatoes for a given movie ID
    """
    url = f'https://www.rottentomatoes.com/m/{movie_id}/reviews'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
    }
    
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        
        reviews = []
        for review in soup.select('.review-row'):
            text = review.select_one('.review-text').get_text(strip=True)
            date = review.select_one('.review-date').get_text(strip=True)
            rating = review.select_one('.score-icon')['class'][1].split('-')[-1]
            reviews.append({'text': text, 'date': date, 'rating': rating})
        
        return pd.DataFrame(reviews)
    
    except Exception as e:
        print(f"Error scraping {movie_id}: {e}")
        return pd.DataFrame()

def scrape_multiple_movies(movie_ids, delay=1):
    """
    Scrape multiple movies with delay between requests
    """
    all_reviews = pd.DataFrame()
    for movie_id in movie_ids:
        reviews = scrape_rotten_tomatoes(movie_id)
        reviews['movie_id'] = movie_id
        all_reviews = pd.concat([all_reviews, reviews])
        time.sleep(delay + random.uniform(0, 1))
    
    return all_reviews
