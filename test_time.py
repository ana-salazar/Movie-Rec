import unittest
from movie_rec import convert_runtime

class TestConvertRuntime(unittest.TestCase):
    def test_convert_runtime(self):
        """
        Test the runtime conversion function with various formats.
        """
        # test full runtime format (hours and minutes)
        self.assertEqual(convert_runtime("2h 30m"), 150, "Should convert '2h 30m' to 150 minutes")
        self.assertEqual(convert_runtime("1h 45m"), 105, "Should convert '1h 45m' to 105 minutes")
        
        # test runtime with only hours
        self.assertEqual(convert_runtime("3h"), 180, "Should convert '3h' to 180 minutes")
        
        # test runtime with only minutes
        self.assertEqual(convert_runtime("45m"), 45, "Should convert '45m' to 45 minutes")
        
        # test edge cases (empty string, invalid formats)
        self.assertEqual(convert_runtime(""), 0, "Should return 0 for an empty string")
        self.assertEqual(convert_runtime("invalid"), 0, "Should return 0 for invalid format")

if __name__ == "__main__":
    unittest.main()
