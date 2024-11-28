import unittest
from src.main import add


class AnyTestClass(unittest.TestCase):

    def test_add_function(self):
        number_array = [0, 1, 2, 3]
        result = add(number_array)
        self.assertEqual(6, result)