# tests/test_data_collection.py

import unittest
from src.data_collection import fetch_imdb_data, fetch_rotten_tomatoes_data

class TestDataCollection(unittest.TestCase):

    def test_fetch_imdb_data(self):
        # Test IMDb data collection
        fetch_imdb_data()
        # Check if the data file is created
        self.assertTrue(os.path.exists('data/raw/IMDb/movies_metadata.csv'))
        self.assertTrue(os.path.exists('data/raw/IMDb/movies_reviews.csv'))

    def test_fetch_rotten_tomatoes_data(self):
        # Test Rotten Tomatoes data collection
        fetch_rotten_tomatoes_data()
        # Check if the data file is created
        self.assertTrue(os.path.exists('data/raw/RottenTomatoes/movies_metadata.csv'))

if __name__ == '__main__':
    unittest.main()
