import pandas as pd
from scipy import stats

# Load data
imdb_metadata = pd.read_csv('data/raw/IMDb/movies_metadata.csv')
imdb_reviews = pd.read_csv('data/raw/IMDb/movies_reviews.csv')
rt_metadata = pd.read_csv('data/raw/RottenTomatoes/movies_metadata.csv')

# Example: Test if the average IMDb rating is different from Rotten Tomatoes rating
merged_data = pd.merge(imdb_metadata, rt_metadata, on='title', suffixes=('_imdb', '_rt'))
t_stat, p_value = stats.ttest_1samp(merged_data['rating_imdb'] - merged_data['rating_rt'], 0)

print(f'T-statistic: {t_stat}, P-value: {p_value}')
