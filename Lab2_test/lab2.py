# program.py

def add(x, y):
    return x + y

def is_even(num):
    return num % 2 == 0

def get_user():
    return None

def divide(x, y):
    if y == 0:
        raise ValueError("Cannot divide by zero")
    return x / y