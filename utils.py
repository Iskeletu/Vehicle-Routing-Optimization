"""
Handles seed input from the user to allow reproducible execution.

Author: Fábio Gandini  
Date: June 2025
"""

def seed_user_input() -> int | None:
    """
    Prompts the user for a seed value.

    Returns:
        - An integer seed if the user provides a valid non-zero number.
        - None if the user enters 0 (to indicate random behavior),
          or if the input is invalid (non-integer).
    """
    
    try:
        seed_input = int(input("Enter a seed value (0 for random): "))
        return None if seed_input == 0 else seed_input
    except ValueError:
        print("Invalid input. Using random behavior.")
        return None


# This is NOT a script file.
if __name__ == '__main__':
    raise RuntimeError("This module is not a standalone script.")