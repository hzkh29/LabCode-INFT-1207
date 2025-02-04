# Project Name:         ICE2 - Temperature Sensor Processing
# Author:               Hezekiah Cua
# Student No.:          100964164
# Date:                 January 2025
# Description:          Implement a Python program to process temperature sensor readings,
#                       ensuring validation and correct calculations using
#                       Boundary Value Analysis (BVA) and Robustness Testing.

import statistics


def validate_temperature(value):
    # It validates the temperature entered by the user
    # to make the value entered only ranges from -50 to 150)
    try:
        # Convert the temperature into a float
        temp = float(value)
        # If the temperature is within -50 and 150, it returns the value
        if -50 <= temp <= 150:
            return temp
        # If the value is not between -50 and 150, it returns nothing
    except ValueError:
        pass
    return None

def process_temperatures(temp_list):
    # It analyzes the list of temperatures and returns the min, max, and avg values
    # It will display an error if the input is invalid
    validated_temps = [validate_temperature(t) for t in temp_list]
    # We use a for loop to iterate each given temperature in the list of user's inputs
    if None in validated_temps:
        # If the user did not enter any value
        return "An invalid input was provided."

    valid_temps = [temp for temp in validated_temps if temp is not None]
    # This is the list that checks if the list of inputs provided by the user has a None

    if not valid_temps:
        # If the has a None even though the user entered other values,
        # It will still tell the user that there was no valid input provided
        return "An invalid input was provided."

    min_temp = min(valid_temps)
    # Gets the minimum temperature
    max_temp = max(valid_temps)
    # Gets the maximum temperature
    avg_temp = round(statistics.mean(valid_temps), 2)
    # Get the average temperature

    # Returns the results if all the inputs are valid
    return f"Min: {min_temp}°C, Max: {max_temp}°C, Avg: {avg_temp}°C"


def get_user_input():
    # Now we prompt thhe user to enter the temperatures separated by commas
    input_string = input("Please enter temperatures (in C) separated by commas (e.g., -50, 0, 100, 150): ")
    # So this will analyze the temperatures entered by the user
    # It enables the program to read the inputs as separated elements in a list
    temp_list = input_string.split(",")
    # Then returns to temp_list
    return temp_list

# Main execution flow
user_temperatures = get_user_input()
# Collect temperatures from user input
result = process_temperatures(user_temperatures)
# Filter and validate temperatures
print(result)
# Displays the result



