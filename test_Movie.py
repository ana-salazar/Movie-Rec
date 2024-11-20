import unittest
from movie_rec import Movie

class TestMovieClass(unittest.TestCase):
    def setUp(self):
        """
        Create a sample Movie object for testing.
        """
        self.sample_movie = Movie(
            rank=1,
            name="The Test Movie",
            year=2024,
            rating=8.5,
            genre="Drama",
            certificate="PG-13",
            run_time=120,
            tagline="This is a test movie."
        )

    def test_movie_initialization(self):
        """
        Test that the Movie class initializes attributes properly.
        """
        # Check each attribute
        self.assertEqual(self.sample_movie.rank, 1, "Rank should be 1")
        self.assertEqual(self.sample_movie.name, "The Test Movie", "Name should be 'The Test Movie'")
        self.assertEqual(self.sample_movie.year, 2024, "Year should be 2024")
        self.assertEqual(self.sample_movie.rating, 8.5, "Rating should be 8.5")
        self.assertEqual(self.sample_movie.genre, "Drama", "Genre should be 'Drama'")
        self.assertEqual(self.sample_movie.certificate, "PG-13", "Certificate should be 'PG-13'")
        self.assertEqual(self.sample_movie.run_time, 120, "Run time should be 120")
        self.assertEqual(self.sample_movie.tagline, "This is a test movie.", "Tagline should match")

if __name__ == "__main__":
    unittest.main()
