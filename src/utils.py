"""
Collenction of shared utility functions:
    - `seed_user_input()`   -> Handles seed user input to allow reproducible execution.
    - `generate_seeds()`    -> Handles generation of list of 32 bit numerical seeds.

Author: Fábio Gandini  
Date: June 2025
"""

# Native Modules:
import random


def seed_user_input() -> int|None:
    """
    Prompts the user for a seed value.

    Returns:
        - An integer seed if the user provides a valid non-zero number.
        - None if the user enters '0' (to indicate random behavior),
        or if the input is invalid (non-integer).
    """
    
    try:
        seed_input = int(input("Enter a seed value (0 for random): "))
        return None if seed_input == 0 else seed_input
    except ValueError:
        print("Invalid input. Using random behavior.")
        return None


def generate_seeds(number_of_seeds:int) -> list[int]:
    """
    Generates a list of random 32 bit integer numerical seeds.

    Parameters:
        - `number_of_seeds: int` -> Size of the list of seeds.

    Return:
        - A list of 32 bit interger seeds.
    """
    
    seed_list:list[int] = []

    for _ in range(number_of_seeds):
        seed_list.append(random.getrandbits(32)) # Generates a random valid 32 bit integer.

    return seed_list


# This is NOT a script file.
if __name__ == '__main__':
    raise RuntimeError("This module is not a standalone script.")