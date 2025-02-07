# Project Name:     Lab 2 - Test Case Design
# Authors:          Hezekiah Cua - 100964164
#                   Spencer DaSilva
# Date:             February 2025
# Description:      A program that can store and retrieve information related
#                   to a user's reading list.

import csv

# Function to add a book to the reading list
def add_book(title, author, year):
    with open('books.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([title, author, year])


# Function to list all books
def list_books():
    with open('books.csv', mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            print(f'Title: {row[0]}, Author: {row[1]}, Year: {row[2]}')

def delete_book(row):
    with open('books.csv', mode='r') as file:
        writer = csv.writer(file)
        reader = csv.reader(writer)
        rows = list(reader)
        del rows[row]
    with open('books.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(rows)


# Function to search for a book by title
def search_book(title):
    with open('books.csv', mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0].lower() == title.lower():
                print(f'Found: Title: {row[0]}, Author: {row[1]}, Year: {row[2]}')
                return
        print('Book not found')


# Menu loop
def menu():
    while True:
        print("\n1. Add Book\n2. List Books\n3. Search Book\n4. Quit\n5. Delete Book")
        choice = input("Select an option: ")

        if choice == '1':
            title = input("Enter book title: ")
            author = input("Enter author name: ")
            year = input("Enter year of publication: ")
            add_book(title, author, year)
        elif choice == '2':
            list_books()
        elif choice == '3':
            title = input("Enter book title to search: ")
            search_book(title)
        elif choice == '4':
            break
        elif choice =='5':
            try:
                user_input = int(input("Which row do you want to delete?: "))
                delete_book(user_input)
            except:
                print("Not a real row")
        else:
            print("Invalid choice. Try again.")


# Run the program
if __name__ == "__main__":
    menu()
