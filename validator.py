# file: validator.py
"""Module for validating user input"""
def validate_number(input_string):
    """Check if input can be converted to a number"""
    print(f"Validator: checking if '{input_string}' is a valid number")
    try:
        float(input_string)
        return True
    except ValueError:
        return False