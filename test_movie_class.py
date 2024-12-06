import unittest
import sqlite3
import csv
from movie_rec import Movie, MovieDatabase, MovieRecommender

class TestMovieFilters(unittest.TestCase):
    
    def setUp(self):
    
        self.movie = Movie(rank = 3, name="The Dark Knight", year=2008, rating=9.0, genre="Action,Crime,Drama", certificate="PG-13", run_time="2h 32m", tagline = "Why So Serious?", budget =185000000, box_office = 1006234167, casts = "Christian Bale, Heath Ledger", directors = "Christopher Nolan", writers = "Jonathan Nolan, Christopher Nolan, David S. Goyer")
        self.recommender = MovieRecommender(self.movie)
        
    def test_movie_initialization(self):
        """
        Test that the Movie class initializes attributes properly.
        """
        # Check each attribute
        self.assertEqual(self.movie.rank, 3)
        self.assertEqual(self.movie.name, "The Dark Knight")
        self.assertEqual(self.movie.year, 2008)
        self.assertEqual(self.movie.rating, 9.0)
        self.assertEqual(self.movie.genre, "Action,Crime,Drama")
        self.assertEqual(self.movie.certificate, "PG-13")
        self.assertEqual(self.movie.run_time, "2h 32m")
        self.assertEqual(self.movie.tagline, "Why So Serious?")
        self.assertEqual(self.movie.budget, 185000000)
        self.assertEqual(self.movie.box_office, 1006234167)
        self.assertEqual(self.movie.casts,"Christian Bale, Heath Ledger")
        self.assertEqual(self.movie.directors, "Christopher Nolan")
        self.assertEqual(self.movie.writers, "Jonathan Nolan, Christopher Nolan, David S. Goyer")

    
    def test_convert_runtime(self):
        self.assertEqual(self.movie.convert_runtime(), 152, "Runtime isnt converted to 152 minutes")
    
    
    def test_matches_filters(self):
        #test rank
        self.assertTrue(self.movie.matches_filters(rank=3), "Rank filter Failed")
        self.assertFalse(self.movie.matches_filters(rank=10), "Rank filter failed for incorrect rank")

        #test genre and min_rating
        self.assertTrue(self.movie.matches_filters(genre='Action', min_rating = 8.5), "Filter Failed")
        self.assertFalse(self.movie.matches_filters(genre = "Romance", min_rating = 7.0), "Filter Failed")
        #test year
        self.assertTrue(self.movie.matches_filters(year=2008), "Filter by year failed")
        self.assertFalse(self.movie.matches_filters(year=2020), "Filter with incorrect year failed")
        #test runtime
        self.assertTrue(self.movie.matches_filters(max_runtime =180),"Runtime failed")
        self.assertFalse(self.movie.matches_filters(max_runtime=130), "Runtime filter failed")
        #test cast
        self.assertTrue(self.movie.matches_filters(casts = 'Christian Bale'), 'Cast filter failed')
        self.assertFalse(self.movie.matches_filters(casts = 'Ayo Edebiri'), 'Cast filter failed')
        #test director
        self.assertTrue(self.movie.matches_filters(directors='Christopher Nolan'), 'Director filter failed')
        self.assertFalse(self.movie.matches_filters(directors='Greta Gerwig'), "Director filter failed"  )      
        #test decade
        self.assertTrue(self.movie.matches_filters(decade=2000), "Decade filter failed for 2000s")
        self.assertFalse(self.movie.matches_filters(decade=1980), "Decade filter dailed for 1990s")
        #test certificate
        self.assertTrue(self.movie.matches_filters(certificate='PG-13'), "Certificate filter failed")
        self.assertFalse(self.movie.matches_filters(certificate='R'), "Certificate filter failed for incorrect option")



if __name__ == "__main__":
    unittest.main()    
       