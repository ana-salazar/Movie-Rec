import unittest
from movie_rec import Movie, MovieRecommender

class TestFilters(unittest.TestCase):
    def setUp(self):
        # Initialize movies with only the fields used in testing
        self.movies = [
            Movie(rank=1, name="The Shawshank Redemption", year=1994, rating=9.3, genre="Drama", certificate="R", run_time="2h 22m",
                  tagline="", budget=0, box_office=0, casts="", directors="", writers=""),
            Movie(rank=3, name="The Dark Knight", year=2008, rating=9.0, genre="Action,Crime,Drama", certificate="PG-13", run_time="2h 32m",
                  tagline="", budget=0, box_office=0, casts="", directors="", writers=""),
            Movie(rank=37, name="Gladiator", year=2000, rating=8.5, genre="Action,Adventure,Drama", certificate="R", run_time="2h 35m",
                  tagline="", budget=0, box_office=0, casts="", directors="", writers=""),
            Movie(rank=51, name="Alien", year=1979, rating=8.5, genre="Horror,Sci-Fi", certificate="R", run_time="1h 57m",
                  tagline="", budget=0, box_office=0, casts="", directors="", writers=""),
        ]
        self.recommender = MovieRecommender(self.movies)

    def test_convert_runtime(self):
        """Test runtime conversion to minutes."""
        self.assertEqual(self.movies[0].convert_runtime(), 142)  # 2h 22m
        self.assertEqual(self.movies[1].convert_runtime(), 152)  # 2h 32m
        self.assertEqual(self.movies[2].convert_runtime(), 155)  # 2h 35m
        self.assertEqual(self.movies[3].convert_runtime(), 117)  # 1h 57m

    def test_filter_by_genre(self):
        """Test filtering movies by genre."""
        filtered = [movie for movie in self.movies if movie.matches_filters(genre="Action")]
        self.assertEqual(len(filtered), 2)  # "The Dark Knight" and "Gladiator"

    def test_filter_by_rating(self):
        """Test filtering movies by minimum rating."""
        filtered = [movie for movie in self.movies if movie.matches_filters(min_rating=9.0)]
        self.assertEqual(len(filtered), 2)  # "The Shawshank Redemption" and "The Dark Knight"

    def test_filter_by_certificate(self):
        """Test filtering movies by certificate."""
        filtered = [movie for movie in self.movies if movie.matches_filters(certificate="R")]
        self.assertEqual(len(filtered), 2)  # "The Shawshank Redemption", "Gladiator", and "Alien"

    def test_recommender(self):
        """Test the recommender's ability to recommend movies."""
        recommendations = self.recommender.recommend_movies(min_rating=8.5, genre="Drama", certificate="R")
        self.assertEqual(len(recommendations), 2)  # "The Shawshank Redemption", "Gladiator"

    def test_sort_by_rating(self):
        """Test sorting recommendations by rating."""
        recommendations = self.recommender.recommend_movies(genre="Action", sort_by="rating")
        self.assertEqual(recommendations[0].name, "The Dark Knight")  # Highest rating in Action genre

if __name__ == "__main__":
    unittest.main()

    
