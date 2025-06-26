"""
Main script file, the project should be run from this file.

Creates a 2D grid with N points with random coordinates, simulating collection locations 
for the vehicle routing problem. The points are uniformly distributed within a defined 
range (e.g., 0 to 100 on both axes), and their pairwise distances are used to construct 
a distance matrix for optimization algorithms.

Author: Fábio Gandini
Date: June 2025
"""

# Native Modules:
import random

# Internal Modules:
import utils
import config as cfg
import routing
import plotting

# External Modules:
from scipy.spatial.distance import cdist
import numpy as np

# Constants:
CONFIG = cfg.load_config()
NUM_POINTS = CONFIG['Number_of_Points']
GRID_SIZE = CONFIG['Grid_Size']
POPULATION_SIZE = CONFIG['Population_Size']


def main(seed: int | None) -> None:
    """
    Script entry point.

    Parameters:
        - seed: int | None -> Numerical seed for reproducibility, None type will result in random behavior.
    """
    if seed is not None:
        np.random.seed(seed); random.seed(seed)
        print(f"Seed set to: '{seed}'.\n")
    else:
        print("No seed provided, using random behavior.\n")

    points = routing.gen_2d_grid(NUM_POINTS, GRID_SIZE)
    distance_matrix = cdist(points, points)
    population = routing.gen_initial_pop(POPULATION_SIZE, NUM_POINTS)
    fitness_scores = [routing.evaluate_route(route, distance_matrix) for route in population]

    best_index = np.argmin(fitness_scores)
    best_route = population[best_index]
    best_distance = fitness_scores[best_index]

    print("Best route found (initial population):", best_route)
    print("Total distance:", round(best_distance, 2))
    plotting.plot_route(best_route, points)
    print(f"\nSummary: {NUM_POINTS} points, population size = {POPULATION_SIZE}, seed: '{seed}'.")

#This is a script file.
if __name__ == '__main__':
    main(utils.seed_user_input())
