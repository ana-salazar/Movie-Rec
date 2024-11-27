import unittest
from movie_rec import Movie, MovieRecommender
    #incomplete
    
class TestFilters(unittest.TestCase):
    def setUp(self):
        self.movies = [
        Movie(rank =1, name = "The Shawshank Redemption", year = 1994, rating = 9.3, genre = 'Drama', certificate = 'R', run_time = '2h 22m'),
        Movie(rank = 3, name="The Dark Knight", year=2008, rating=9.0, genre="Action,Crime,Drama", certificate="PG-13", run_time="2h 32m"),
        Movie(rank = 37, name = "Gladiator", year = 2000, rating = 8.5, genre = "Action,Adventure,Drama" , certificate = "G", run_time= "2h 35"),
        Movie(rank = 51, name = "Alien", year = 1979, rating = 8.5, genre = "Horror,Sci-Fi" , certificate = "G", run_time= "2h 35")         
            
        ]
        
        
    
if __name__ == "__main__":
    unittest.main()
    