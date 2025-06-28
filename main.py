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
import routing
import plotting
import config as cfg
from utils import seed_user_input, generate_seeds

# External Modules:
import numpy as np
from scipy.spatial.distance import cdist

# Constants:
CONFIG = cfg.load_config()
DECIMAL_DIGITS = 2


def main(seed:int|None) -> None:
    """
    Script entry point.

    Parameters:
        - `seed: int | None` -> Numerical seed for reproducibility, `None` type will result in random behavior.
    """

    if seed is None:
        print("No seed provided, using random behavior.\n")
        seed = generate_seeds(1)[0] # Generates a random 32 bit numerical seed.

    
    # Seeds the plot point generation and population:
    np.random.seed(seed)
    random.seed(seed)
    print(f"Seed set to: '{seed}'.\n")



    points = routing.gen_2d_grid(CONFIG['Number_of_Points'], CONFIG['Grid_Size']) # Generate random (or seeded) collection of points.
    distance_matrix = cdist(points, points) # Compute paiwise distances.
    population = routing.gen_initial_pop(CONFIG['Population_Size'], CONFIG['Number_of_Points']) # Generate initial population.
    fitness_scores = [routing.evaluate_route(route, distance_matrix) for route in population] # Evaluate each route.

    # Select the best route based on the shortest total distance:
    best_index = np.argmin(fitness_scores)
    best_route = population[best_index]
    best_distance = fitness_scores[best_index]

    # Displays plotted route:
    plotting.display_route(plotting.plot_route(best_route, points))

    print(f"Best route found (initial population): {best_route}.")
    print(f"Total distance: {round(best_distance, DECIMAL_DIGITS)}.")
    print(f"\nSummary: {CONFIG['Number_of_Points']} points, population size = {CONFIG['Population_Size']}, seed: '{seed}'.\n")


#This is a script file.
if __name__ == '__main__':
    main(seed_user_input())
