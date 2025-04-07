import unittest
from scripts.data_collection import fetch_imdb_data, fetch_rotten_tomatoes_data

class TestDataCollection(unittest.TestCase):
    def test_fetch_imdb_data(self):
        fetch_imdb_data()
        # Add assertions to verify the data

    def test_fetch_rotten_tomatoes_data(self):
        fetch_rotten_tomatoes_data()
        # Add assertions to verify the data

if __name__ == '__main__':
    unittest.main()
