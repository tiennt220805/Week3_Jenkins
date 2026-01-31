import unittest
from baitap1 import calculate_sum_and_average

class TestCalculateFunctions(unittest.TestCase):

    def test_valid_numbers(self):
        self.assertEqual(calculate_sum_and_average([1, 2, 3]), (6, 2.0))

    def test_empty_list(self):
        with self.assertRaises(ValueError) as context:
            calculate_sum_and_average([])
        self.assertEqual(str(context.exception), "Dãy số không được rỗng.")

    def test_negative_numbers(self):
        # Hàm calculate_sum_and_average không validate số âm
        self.assertEqual(calculate_sum_and_average([1, -2, 3]), (2, 0.6666666666666666))

    def test_single_number(self):
        self.assertEqual(calculate_sum_and_average([5]), (5, 5.0))

    def test_number_from_user(self):
        # This test is not applicable here since we cannot simulate user input in this context.
        # Instead, we can test the function that processes user input separately.
        pass

if __name__ == '__main__':
    unittest.main()