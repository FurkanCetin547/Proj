import pandas as pd

# Load data
imdb_metadata = pd.read_csv('data/raw/IMDb/movies_metadata.csv')
imdb_reviews = pd.read_csv('data/raw/IMDb/movies_reviews.csv')
rt_metadata = pd.read_csv('data/raw/RottenTomatoes/movies_metadata.csv')

# Example analysis: Merge IMDb metadata with Rotten Tomatoes metadata
merged_data = pd.merge(imdb_metadata, rt_metadata, on='title', suffixes=('_imdb', '_rt'))

# Display merged data
print(merged_data.head())
