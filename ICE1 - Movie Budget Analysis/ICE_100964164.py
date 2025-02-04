# Author: Hezekiah Cua
# Student ID: 100964164
# Description: Analyze movie budgets and save results to a file.


# Define the function that will add the movies to the file
def add_movies_to_file(file_name):
    # Ask the user to enter how many movies they want to add
    number_of_movies = int(input("How many movies would you like to add? "))
    # Open the file using the with statement
    with open(file_name, "a") as file:
        # Use a for loop to keep asking the user to enter the movie names
        # and budget of the movies as per the value of the number_of_movies entered
        for _ in range(number_of_movies):
            # Ask for the user enter the name of the movie
            movie_name = input("Enter the movie name: ")
            # Ask the user to enter how much the movie budget is
            movie_budget = input("Enter the movie budget (in dollars): ")
            # Add the newly entered movie and its budget to the movieList.txt
            file.write(f"\n{movie_name}, {movie_budget}")

# Write analysis results to a file, sorted by movie name
def write_results_to_file(file_name, average_budget, high_budget_movies):
    # Sort the movies by name in ascending order
    sorted_movies = sorted(high_budget_movies, key=lambda movie: movie[1])

    # Open the file using the with statement
    with open(file_name, "w") as file:
        # Add the average budget output.txt
        file.write(f"Average Budget: ${average_budget:,.2f}\n")
        # Add the high budget movies
        file.write("Movies with Budgets Higher than Average:\n")
        # Loop through the sorted movies to identify which movies are above
        for name, budget in sorted_movies:
            # Create a difference variable to
            # calculate the difference of the over budget movie from the average
            difference = budget - average_budget
            # Show the list of the movies that are higher than
            # the average budget from the movies with average budgets
            file.write(f"{name}: ${budget:,} (higher by ${difference:,})\n")

# Set a condition that the function will only execute when
# the script is being executed directly
if __name__ == "__main__":
    add_movies_to_file("movieList.txt")

# Starter code:

def calculate_average_budget(movies):
    """Calculate the average budget of all movies."""
    budgets = [budget for _, budget in movies]
    return sum(budgets) / len(budgets)

def find_high_budget_movies(movies, average_budget):
    """Find movies with budgets higher than the average."""
    return [(name, budget) for name, budget in movies if budget > average_budget]

def read_movies_from_file(file_name):
    """Read movies from a file."""
    movies = []
    with open(file_name, "r") as file:
        lines = file.readlines()[1:]  # Skip header
        for line in lines:
            name, budget = line.strip().split(", ")
            movies.append((name, int(budget)))
    return movies

def write_results_to_file(file_name, average_budget, high_budget_movies):
    """Write analysis results to a file."""
    with open(file_name, "w") as file:
        file.write(f"Average Budget: ${average_budget:,.2f}\n")
        file.write("Movies with Budgets Higher than Average:\n")
        for name, budget in high_budget_movies:
            file.write(f"{name}: ${budget:,}\n")


if __name__ == "__main__":
    # Read movies from file
    movies = read_movies_from_file("MovieList.txt")

    # Display all movies
    #print("Full Movie List:")
    #for name, budget in movies:
    #    print(f"  {name}: ${budget:,}")

    # Calculate average budget
    average_budget = calculate_average_budget(movies)

    # Find high-budget movies
    high_budget_movies = find_high_budget_movies(movies, average_budget)

    # Print results
    print(f"Average Budget: ${average_budget:,.2f}")
    print("Movies with Budgets Higher than Average:")
    for name, budget in high_budget_movies:
        print(f"  {name}: ${budget:,}")

    # Write results to output file
    write_results_to_file("Output.txt", average_budget, high_budget_movies)
    print("Results saved to 'Output.txt'.")