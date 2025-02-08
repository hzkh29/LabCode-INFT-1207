import unittest
import csv
from Program import add_book, list_books, search_book, delete_book, menu


class TestFunctions(unittest.TestCase):

    def test_a_add_book(self):
        """Test adding a book."""
        add_book("Test Book", "Author Name", "2022")
        with open("books.csv", "r") as file:
            reader = csv.reader(file)
            rows = list(reader)
        self.assertIn(["Test Book", "Author Name", "2022"], rows)


    def test_b_search_book(self):
        """Test searching for an existing book."""
        output_result = search_book("Test Book")  # Now it returns a value
        expected_output = "Found: Title: Test Book, Author: Author Name, Year: 2022"
        self.assertEqual(output_result, expected_output, "search_book did not return the expected output.")

    def test_c_list_books(self):
        output_result = search_book("Test Book")  # Now it returns a value
        expected_output = "Found: Title: Test Book, Author: Author Name, Year: 2022"
        self.assertEqual(output_result, expected_output, "search_book did not return the expected output.")

    def test_d_delete_book(self):
        """Test deleting a book"""
        output_result = delete_book("Test Book")
        expected_output = "Test Book successfully deleted"
        self.assertEqual(output_result, expected_output, "delete_book did not delete the book")


if __name__ == '__main__':
    unittest.main()