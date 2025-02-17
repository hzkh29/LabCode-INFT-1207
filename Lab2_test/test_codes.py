import csv
import unittest


class TestReadingList(unittest.TestCase):
    def search_book(title):
        with open('books.csv', mode='r') as file:
         reader = csv.reader(file)
        for row in reader:
              if row[0].lower() == title.lower():
                result = f'Found: Title: {row[0]}, Author: {row[1]}, Year: {row[2]}'
                print(result)
                return result
        return 'Book not found'


        pass