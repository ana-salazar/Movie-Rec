import unittest

class TestMovieRuntimeConversion(unittest.TestCase):
    def test_convert_runtime(self):
        # Define test cases as (runtime_string, expected_minutes)
        test_cases = [
            ("2h 30m", 150),  # 2h 30m = 150 mins
            ("1h", 60),       # 1h = 60 mins
            ("45m", 45),      # 45m = 45 mins
            ("Unknown", 0),   # Invalid format = 0 mins
            ("3h 15m", 195),  # 3h 15m = 195 mins
            ("2h 0m", 120),   # 2h 0m = 120 mins
        ]

        for runtime, expected in test_cases:
            with self.subTest(runtime=runtime, expected=expected):
                movie = Movie(1, "Test Movie", 2021, 8.5, "Action", "PG-13", runtime, "A test movie.", 100000, 200000, "Actor A", "Director A", "Writer A")
                self.assertEqual(movie.convert_runtime(), expected)

if __name__ == "__main__":
    unittest.main()
