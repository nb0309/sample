# file: storage.py
"""Module for storing results"""
def save_result(result):
    """Save a result to a file"""
    print(f"Storage: saving result '{result}'")
    with open("results.txt", "a") as file:
        file.write(result + "\n")
    print("Result saved successfully!")