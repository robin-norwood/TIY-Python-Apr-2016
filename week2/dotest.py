import unittest

def is_palindrome(strng):
    """Return true if the given string is the same backward as forward, case insensitive"""
    return strng.lower() == strng.lower()[::-1]

class TestWordUtilities(unittest.TestCase):

    def test_is_palindrome(self):
        self.assertTrue(is_palindrome('anna'))
        self.assertFalse(is_palindrome('kerenina'))
        self.assertTrue(is_palindrome("Anna"))

    def test_nothing(self):
        self.assertTrue(True)

    def test_string_capitalize(self):
        self.assertEqual("Joe", "joe".capitalize())


if __name__ == '__main__':
    unittest.main()
