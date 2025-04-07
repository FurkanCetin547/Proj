import os
import pandas as pd
from imdb import IMDb
from bs4 import BeautifulSoup
import requests

ia = IMDb()

def fetch_movie_metadata(title):
    results = ia.search_movie(title)
    if not results:
        return None
    movie = ia.get_movie(results[0].movieID)
    return {
        "title": movie.get("title"),
        "year": movie.get("year"),
        "genres": movie.get("genres"),
        "rating": movie.get("rating"),
        "votes": movie.get("votes"),
        "directors": [d['name'] for d in movie.get("directors", [])],
        "plot": movie.get("plot outline")
    }

def scrape_rt_reviews(url, max_reviews=50):
    headers = {"User-Agent": "Mozilla/5.0"}
    page = requests.get(url, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')
    reviews = [r.get_text(strip=True) for r in soup.find_all("p", class_="review-text")[:max_reviews]]
    return reviews

def save_data():
    movie_titles = ["The Godfather", "Parasite", "Avengers: Endgame", "Titanic"]
    metadata = [fetch_movie_metadata(title) for title in movie_titles if title]
    pd.DataFrame(metadata).to_csv("data/processed/movie_metadata.csv", index=False)

    reviews = []
    for title in movie_titles:
        rt_url = f"https://www.rottentomatoes.com/m/{title.lower().replace(' ', '_')}/reviews?type=user"
        user_reviews = scrape_rt_reviews(rt_url)
        for r in user_reviews:
            reviews.append({"title": title, "review": r})
    
    pd.DataFrame(reviews).to_csv("data/processed/user_reviews.csv", index=False)

if __name__ == "__main__":
    save_data()
