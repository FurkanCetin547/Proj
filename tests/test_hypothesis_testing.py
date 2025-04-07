# tests/test_hypothesis_testing.py

import unittest
from src.hypothesis_testing import test_imdb_rt_ratings

class TestHypothesisTesting(unittest.TestCase):

    def test_test_imdb_rt_ratings(self):
        # Test hypothesis testing between IMDb and Rotten Tomatoes ratings
        result = test_imdb_rt_ratings()
        self.assertIsInstance(result, tuple)  # Assuming the result is a tuple (t-statistic, p-value)

if __name__ == '__main__':
    unittest.main()
