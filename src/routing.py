"""
Provides core functions for grid generation, population creation, and route evaluation
used in VRO problems.

Author: Fábio Gandini  
Date: June 2025
"""

# Native Modules:
import random

# External Modules:
import numpy as np


def gen_2d_grid(n_points:int, grid_size:int) -> np.ndarray:
    """
    Generates a 2D grid with N randomly placed points.

    Parameters:
        - `n_points: int`   -> Number of points to generate within the 2D grid.
        - `grid_size: int`  -> Maximum coordinate value for both X and Y.

    Returns:
        - An array of shape (n_points, 2), where each row is a (x, y) coordinate as an `numpy.ndarray` object.
    """
    
    return np.random.uniform(0, grid_size, size=(n_points, 2))


def gen_initial_pop(pop_size: int, num_points: int) -> list[list[int]]:
    """
    Generates an initial population of random routes (permutations of point indices).

    Parameters:
        - `pop_size: int`   -> Number of individuals (routes) in the population.
        - `num_points: int` -> Number of collection points in each route.

    Returns:
        - A list of lists with each inner list as a unique permutation representing a route.
    """

    population:list[list[int]] = []

    for _ in range(pop_size):
        route = list(range(num_points))
        random.shuffle(route)
        population.append(route)
    
    return population


def evaluate_route(route: list[int], distance_matrix: np.ndarray) -> float:
    """
    Calculates the total distance of a closed-loop route.

    Parameters:
        - `route: list[int]`                -> Sequence of point indices representing the route.
        - `distance_matrix: numpy.ndarray`  -> Matrix of pairwise distances between points.

    Returns:
        - Total distance traveled when following the route and returning to the start.
    """

    total_distance:float = 0.0

    for i in range(len(route)):
        origin = route[i]
        destination = route[(i + 1) % len(route)]  # Ensures the route closes.
        total_distance += distance_matrix[origin, destination]

    return total_distance


# This is NOT a script file.
if __name__ == '__main__':
    raise RuntimeError("This module is not a standalone script.")