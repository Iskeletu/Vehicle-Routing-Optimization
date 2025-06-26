"""
Provides core functions for grid generation, population creation, and route evaluation
used in vehicle routing optimization problems.

This module defines functions to:
- Generate a 2D grid of randomly placed points.
- Create a population of random routes (permutations of the points).
- Evaluate the total distance of a route based on a distance matrix.

Author: Fábio Gandini  
Date: June 2025
"""

# Native Modules:
import random

# External Modules:
import numpy as np


def gen_2d_grid(n_points: int, grid_size: int = 100) -> np.ndarray:
    """
    Generates a 2D grid with N randomly placed points.

    Parameters:
        - n_points: int -> Number of points to generate.
        - grid_size: int -> Maximum coordinate value for both X and Y (default: 100).

    Returns:
        - np.ndarray: An array of shape (n_points, 2), where each row is a (x, y) coordinate.
    """
    
    return np.random.uniform(0, grid_size, size=(n_points, 2))


def gen_initial_pop(pop_size: int, num_points: int) -> list[list[int]]:
    """
    Generates an initial population of random routes (permutations of point indices).

    Parameters:
        - pop_size: int -> Number of individuals (routes) in the population.
        - num_points: int -> Number of collection points in each route.

    Returns:
        - list of lists: Each inner list is a unique permutation representing a route.
    """

    population = []

    for _ in range(pop_size):
        route = list(range(num_points))
        random.shuffle(route)
        population.append(route)
    
    return population


def evaluate_route(route: list[int], distance_matrix: np.ndarray) -> float:
    """
    Calculates the total distance of a closed-loop route.

    Parameters:
        - route: list[int] -> Sequence of point indices representing the route.
        - distance_matrix: np.ndarray -> Matrix of pairwise distances between points.

    Returns:
        - float: Total distance traveled when following the route and returning to the start.
    """

    total_distance = 0.0

    for i in range(len(route)):
        origin = route[i]
        destination = route[(i + 1) % len(route)]  # Ensures the route closes.
        total_distance += distance_matrix[origin, destination]

    return total_distance


# This is NOT a script file.
if __name__ == '__main__':
    raise RuntimeError("This module is not a standalone script.")