import unittest

from string_utils import reverse_string, capitalize_string, is_capitalized


class TestStringUtils(unittest.TestCase):
    def test_reverse_string(self):

        self.assertEqual(reverse_string("Alan"), "nalA")
        self.assertEqual(reverse_string("Sushi"), "ihsuS")

    def test_capitalize_string(self):
        self.assertEqual(capitalize_string("alan"), "Alan")
        self.assertEqual(capitalize_string("sushi"), "Sushi")
        self.assertEqual(capitalize_string("Alan"), "Alan")

    def test_is_capitalized(self):
        self.assertTrue(is_capitalized("Alan"))
        self.assertTrue(is_capitalized("Sushi"))
        self.assertFalse(is_capitalized("alan"))
        self.assertFalse(is_capitalized("sushi"))
        self.assertFalse(is_capitalized(""))


if __name__ == "__main__":
    unittest.main()
