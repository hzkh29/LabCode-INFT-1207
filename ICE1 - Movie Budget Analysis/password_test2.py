import random
import string

def get_user_input(prompt, min_value, max_value):
    try:
        value = int(input(prompt))
        if min_value <= value <= max_value:
            return value
        else:
            print(f"Please enter a value between {min_value} and {max_value}.")
    except ValueError:
        print("Invalid input; please enter a valid number.")
    return get_user_input(prompt, min_value, max_value)  # Recursive call if validation fails

def generate_password(length, num_letters, num_digits, num_specials):
    if num_letters + num_digits + num_specials > length:
        print("Error: The sum of specified characters exceeds the total password length.")
        return None  # Ensure total requested characters do not exceed length

    # Generate the characters for the password
    letters = random.choices(string.ascii_letters, k=num_letters)
    digits = random.choices(string.digits, k=num_digits)
    specials = random.choices(string.punctuation, k=num_specials)
    remaining = length - (num_letters + num_digits + num_specials)
    others = random.choices(string.ascii_letters, k=remaining)  # Fill remaining with letters

    # Create password list and shuffle
    password_list = letters + digits + specials + others
    random.shuffle(password_list)

    # Join list into a string to form the final password
    return ''.join(password_list)

def main():
    print("\n--- Secure Password Generator ---\n")
    # Step 1: Get user inputs for password length and character distribution
    total_length = get_user_input("Enter the total length of the password: ", 8, 20)
    num_letters = get_user_input("Enter the number of letters in the password: ", 0, total_length)
    num_digits = get_user_input("Enter the number of digits in the password: ", 0, total_length - num_letters)
    num_specials = get_user_input("Enter the number of special characters: ", 0, total_length - num_letters - num_digits)

    # Generate the password
    password = generate_password(total_length, num_letters, num_digits, num_specials)
    if password is None:
        return  # Exit if password could not be generated due to invalid specifications

    # Step 4: Display the generated password
    print(f"\nGenerated Password: {password}")

    # Optional Step 5: Save password to file
    with open("password.txt", "w") as file:
        file.write(password)
    print("Password saved to 'password.txt'.")

if __name__ == "__main__":
    main()
