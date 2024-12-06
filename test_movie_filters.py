import unittest
import sqlite3
import csv
from movie_rec import Movie, MovieDatabase, MovieRecommender
#unfinished

class TestMovieRecommendation(unittest.TestCase):
    
    def setUp(self):
    
        self.movie = Movie(rank = 3, name="The Dark Knight", year=2008, rating=9.0, genre="Action,Crime,Drama", certificate="PG-13", run_time="2h 32m", tagline = "Why So Serious?", budget =185000000, box_office = 1006234167, casts = "Christian Bale, Heath Ledger", directors = "Christopher Nolan", writers = "Jonathan Nolan, Christopher Nolan, David S. Goyer")
        
        
        self.recommender = MovieRecommender(self.movie)
        
    def test_convert_runtime(self):
        self.assertEqual(self.movie.convert_runtime(), 152, "Runtime isnt converted to 152 minutes")
    
    def test_movie_intialization(self):
        self.assertEqual(self.movie.name, "The Dark Knight", "Wrong name")
        self.assertEqual(self.movie.year, 2008, "Wrong year")
        self.assertEqual(self.movie.rating, 9.0, "Wrong rating")
        self.assertEqual(self.movie.run_time, "2h 32m", "Wrong runtime" )
    def test_matches_filters(self):
        self.assertTrue(self.movie.matches_filters(genre='Action', min_rating = 8.5), "Filter Failed")
        self.assertFalse(self.movie.matches_filters(genre = "Romance", min_rating = 7.0), "Filter Failed")
        self.assertTrue(self.movie.matches_filters(year=2008), "Filter by year failed")
                
    
    

if __name__ == "__main__":
    unittest.main()    
       