"""Test."""

import unittest
import pytest
from number_list import NumberList


class Test(unittest.TestCase):
    """Test class."""

    @classmethod
    def setUpClass(cls) -> None:
        cls.not_list = ''
        cls.empty_list = []
        cls.not_int_list = ['a']
        cls.average_one_element = NumberList.get_average([1])
        cls.average_1 = NumberList.get_average([1, 1, 1])
        cls.average_2 = NumberList.get_average([1, 2, 3, 4])

    def test_not_list(self):
        """Test not a list passed"""
        with pytest.raises(TypeError):
            NumberList.get_average(self.not_list)

    def test_incorrect_list_data(self):
        """Test incorrect list data"""
        with pytest.raises(ValueError):
            NumberList.get_average(self.not_int_list)

    def test_empty_list(self):
        """Test empty list."""
        self.assertEqual(NumberList.get_average(self.empty_list), 0)

    def test_correct_list(self):
        """Test correct list."""
        self.assertEqual(self.average_one_element, 1)

    def test_compare_values_equal(self):
        """Test compare equal values."""
        self.assertEqual(NumberList.compare_values(
            self.average_one_element, self.average_1),
            'The average values are equal.')

    def test_compare_values_first(self):
        """Test compare average values where the first is greater than
        the second."""
        self.assertEqual(NumberList.compare_values(
            self.average_2, self.average_1),
            'The first list has a larger average value.')

    def test_compare_values_second(self):
        """Test compare average values where the second is greater than
        the first."""
        self.assertEqual(NumberList.compare_values(
            self.average_1, self.average_2),
            'The second list has a larger average value.')


if __name__ == '__main__':
    pytest.main()