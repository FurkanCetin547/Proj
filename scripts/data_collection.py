import pandas as pd

def fetch_imdb_reviews(movie_id):
    """ Fake function to simulate movie review collection. """
    sample_reviews = [
        "Amazing movie! Best I've seen in years.",
        "Absolutely terrible. Waste of time.",
        "Pretty good, but had some flaws.",
        "Loved the cinematography, but the story was weak.",
        "Horrible acting, but a great concept."
    ]
    return sample_reviews

# 
if __name__ == "__main__":
    reviews = fetch_imdb_reviews("tt0111161")
    df = pd.DataFrame({"review_text": reviews})
    df.to_csv("data/movie_reviews.csv", index=False)
    print("Movie reviews saved.")

