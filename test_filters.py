import unittest
from movie_rec import Movie 
    #NEED TO EDIT fix the decades and check on ratings
    #INCOMPLETE
class TestFilters(unittest.TestCase):
    
    def setUp(self):
        self.movie1 = Movie(rank = 3, name="The Dark Knight", year=2008, rating=9.0, genre="Action,Crime,Drama", certificate="PG-13", run_time="2h 32m", tagline="Why So Serious?")
        self.movie2 = Movie(rank = 37, name = "Gladiator", year = 2000, rating = 8.5, genre = "Action,Adventure,Drama" , certificate = "G", run_time= "2h 35", tagline = "Father of a murdered son, husband to a murdered wife and I shall have my vengeance in this life or the next" )
        self.movie3 = Movie(rank = 51, name = "Alien", year = 1979, rating = 8.5, genre = "Horror,Sci-Fi" , certificate = "G", run_time= "2h 35", tagline = "Father of a murdered son, husband to a murdered wife and I shall have my vengeance in this life or the next" )

    def test_genre(self):
        self.assertTrue(self.movie1.matches_filters(genre="Action"))  # dark knight has action
        self.assertTrue(self.movie2.matches_filters(genre="Adventure"))  # adventure is in gladiator
        self.assertFalse(self.movie3.matches_filters(genre="Action"))  # action is not in alien
        

    def test_decade(self):
        #FIX 2000S
        self.assertTrue(self.movie1.matches_filters(decade=2000)) #dark night is from 2000s
        self.assertTrue(self.movie2.matches_filters(decade=2000)) #gladiator is from the 2000s
        self.assertFalse(self.movie3.matches_filters(decade=1960)) #alien is not from the 1960s
    
    def test_min_rating(self):
        self.assertTrue(self.movie1.matches_filters(min_rating=8.0))
        self.assertTrue(self.movie2.matches_filters(min_rating=8.0))  
        self.assertFalse(self.movie3.matches_filters(min_rating=9.0)) 
    
    def test_certificate(self):
        pass
    
    def test_run_time(self):
        pass
if __name__ == "__main__":
    unittest.main()
    