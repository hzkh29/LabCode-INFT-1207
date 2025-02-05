# test_program.py

import unittest
from program import add, is_even, get_user, divide

class TestSimpleFunctions(unittest.TestCase):

    # 1. assertEqual: Checks if two values are equal
    def test_add(self):
        self.assertEqual(add(5, 5), 10)

    # 2. assertTrue: Checks if a value evaluates to True
    def test_is_even(self):
        self.assertTrue(is_even(4))

    # 3. assertFalse: Checks if a value evaluates to False
    def test_is_not_even(self):
        self.assertFalse(is_even(5))

    # 4. assertIs: Checks if two variables refer to the same object
    def test_same_object(self):
        result = add(2, 3)
        expected_result = 5
        self.assertIs(result, expected_result)

    # 5. assertIsNone: Checks if a value is None
    def test_is_none(self):
        self.assertIsNone(get_user())

    # 6. assertIsNotNone: Checks if a value is not None
    def test_is_not_none(self):
        user = "Alice"
        self.assertIsNotNone(user)

    # 7. assertIn: Checks if a value is in a container (e.g., list)
    def test_item_in_list(self):
        my_list = [1, 2, 3, 4, 5]
        self.assertIn(3, my_list)

    # 8. assertNotIn: Checks if a value is not in a container
    def test_item_not_in_list(self):
        my_list = [1, 2, 3, 4, 5]
        self.assertNotIn(6, my_list)

    # 9. assertRaises: Checks if a specific exception is raised
    def test_divide_by_zero(self):
        self.assertRaises(ValueError, divide, 10, 0)

    # 10. assertAlmostEqual: Checks if two values are approximately equal (useful for floating-point numbers)
    def test_approximate_equal(self):
        result = divide(10, 3)
        self.assertAlmostEqual(result, 3.33, places=2)

if __name__ == '__main__':
    unittest.main()