# tests/test_data_analysis.py

import unittest
import pandas as pd
from src.data_analysis import analyze_imdb_data, analyze_rt_data, analyze_genres

class TestDataAnalysis(unittest.TestCase):

    def test_analyze_imdb_data(self):
        # Test IMDb data analysis
        result = analyze_imdb_data()
        self.assertIsInstance(result, float)  # Assuming the result is a float (average rating)

    def test_analyze_rt_data(self):
        # Test Rotten Tomatoes data analysis
        result = analyze_rt_data()
        self.assertIsInstance(result, float)  # Assuming the result is a float (average rating)

    def test_analyze_genres(self):
        # Test genre analysis
        result = analyze_genres()
        self.assertIsInstance(result, pd.Series)  # Assuming the result is a pandas Series (genre counts)

if __name__ == '__main__':
    unittest.main()
