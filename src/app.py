import requests
import json

def get_stackoverflow_questions():
    response = requests.get('https://api.stackexchange.com/2.3/questions?order=desc&sort=activity&site=stackoverflow')
    return response.json()['items']

def my_url():
    response = requests.get('https://api.stackexchange.com/2.3/questions?order=desc&sort=activity&site=stackoverflow')
    return response

# Math operations
def add(a, b):
    """Add two numbers and return the result."""
    return a + b

def subtract(a, b):
    """Subtract b from a and return the result."""
    return a - b

def multiply(a, b):
    """Multiply two numbers and return the result."""
    return a * b

def divide(a, b):
    """Divide a by b and return the result. Raises ValueError if b is zero."""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

def calculate_power(base, exponent):
    """Calculate base raised to the power of exponent."""
    return base ** exponent

# Execute if run directly
if __name__ == "_main_":
    print(get_stackoverflow_questions())