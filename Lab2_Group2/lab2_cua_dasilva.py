# Project Name:     Lab 2 - Test Case Design
# Authors:          Hezekiah Cua - 100964164
#                   Spencer DaSilva
# Date:             February 2025
# Description:      A program that can store and retrieve information related
#                   to a user's reading list.



def add_book():
    title = input("Title: ").strip().title()
    author = input("Author: ").strip().title()
    year = input("Year of publication: ").strip()

    with open("books.csv", "a") as reading_list:
        reading_list.write(f"{title},{author},{year}\n")

def find_books():
    reading_list = get_all_books()
    matching_books = []

    search_term = input("Please enter a book title to search for: ").strip().lower()

    for book in reading_list:
        if search_term in book["title"].lower():
            matching_books.append(book)

    return matching_books

# Helper function for retrieving data from the csv file
def get_all_books():
    books = []

    with open("books.csv", "r") as reading_list:
        for book in reading_list:
            # Extracts the values from the CSV data
            title, author, year = book.strip().split(",")

            # Creates a dictionary from the csv data and adds it to the books list
            books.append({
                "title": title,
                "author": author,
                "year": year
            })

    return books

def show_books(books):
    # Adds an empty line before the output
    print()

    for book in books:
        print(f"{book['title']}, by {book['author']} ({book['year']})")

    print()

menu_prompt = """Please enter one of the following options:

- 'a' to add a book
- 'l' to list the books
- 's' to search for a book
- 'q' to quit

What would you like to do? """

# Get a selection from the user
selected_option = input(menu_prompt).strip().lower()

# Run the loop until the user selected 'q'
while selected_option != "q":
    if selected_option == "a":
        add_book()
    elif selected_option == "l":
        # Retrieves the whole reading list for printing
        reading_list = get_all_books()

        # Check that reading_list contains at least one book
        if reading_list:
            show_books(reading_list)
        else:
            print("Your reading list is empty.")
    elif selected_option == "s":
        matching_books = find_books()

        # Checks that the seach returned at least one book
        if matching_books:
            show_books(matching_books)
        else:
            print("Sorry, we didn't find any books for that search term.")
    else:
        print(f"Sorry, '{selected_option}' isn't a valid option.")

    # Allow the user to change their selection at the end of each iteration
    selected_option = input(menu_prompt).strip().lower()

