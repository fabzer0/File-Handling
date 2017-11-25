import unittest
import readfiles

class TestReadFiles(unittest.TestCase):
    """
    Class to test the functions on the readfiles module

    Args:
        unittest.TestCase: Class from the unittest module to create unit tests
    """

    text_file = "test.txt"
    def read_file(text_file):
        """
        function that reads a text file and returns the data from the file

        Raises:
            FileNotFoundError: If it cannot the file
        """

        try:
            with open(text_file,"r") as handle:
                data = handle.read()
                return data
        except FileNotFoundError:
            return None

    def test_nonfile(self):
        """
        test to confirm that an exception is raised when a wrong file is inputted
        """
        self.assertEqual(None,readfiles.read_file("tests.txt))

if __name__ == "__main__":
    unittest.main()
