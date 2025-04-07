# src/hypothesis_testing.py

import pandas as pd
from scipy import stats

# Load data
imdb_metadata_df = pd.read_csv('data/raw/IMDb/movies_metadata.csv')
rt_metadata_df = pd.read_csv('data/raw/RottenTomatoes/movies_metadata.csv')

# Hypothesis testing functions
def test_imdb_rt_ratings():
    # Example: Test if there's a significant difference between IMDb and Rotten Tomatoes ratings
    imdb_ratings = imdb_metadata_df['rating'].dropna()
    rt_ratings = rt_metadata_df['rating'].dropna()
    t_stat, p_value = stats.ttest_ind(imdb_ratings, rt_ratings)
    print(f'T-test between IMDb and Rotten Tomatoes ratings: t-statistic = {t_stat}, p-value = {p_value}')

# Perform hypothesis testing
test_imdb_rt_ratings()
