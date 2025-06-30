"""
Main script file, the project should be executed from this file.

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
import routing
import plotting
import config as cfg
import genetic_evolution

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

    # Seeds the plot point generation and population:
    if seed is None:
        print("No seed provided, using random behavior.\n")
        seed = utils.generate_seeds(1)[0] # Generates a random 32 bit numerical seed.
    np.random.seed(seed)
    random.seed(seed)
    print(f"Seed set to: '{seed}'.\n")

    # Generate points and distance matrix:
    points = routing.gen_2d_grid(CONFIG['Number_of_Points'], CONFIG['Grid_Size'])
    dist_matrix = cdist(points, points)

    # Random Initial Population Algorithm (RIPA):
    RIPA_population = routing.gen_initial_pop(CONFIG['Population_Size'], CONFIG['Number_of_Points'])
    RIPA_evaluation = [routing.evaluate_route(r, dist_matrix) for r in RIPA_population]
    best_RIPA_idx = np.argmin(RIPA_evaluation)
    best_RIPA_route = RIPA_population[best_RIPA_idx]
    best_RIPA_distance = RIPA_evaluation[best_RIPA_idx]

    # Evolutionary Algorithm (EA):
    EA_result = genetic_evolution.run_evolutionary_experiment(CONFIG, points, seed)

    # Display both random initial population and evolutionary results:
    print(
        "=== RANDOM INITIAL POPULATION ===\n"
        f"Best route: {best_RIPA_route}\n"
        f"Total distance: {round(best_RIPA_distance, DECIMAL_DIGITS)}\n"
    )

    print(
        "=== EVOLUTIONARY ALGORITHM ===\n"
        f"Best route: {EA_result['route']}\n"
        f"Total distance: {round(EA_result['distance'], DECIMAL_DIGITS)}\n"
    )

    # Plot final results from each type of evaluation:
    plotting.display_route(plotting.plot_route(best_RIPA_route, points, "Random Initial Population"))
    plotting.display_route(plotting.plot_route(EA_result['route'], points, "Evolutionary Result"))

    # Summary:
    print(
        "Summary:\n"
        f"  - Number of points: {CONFIG['Number_of_Points']} points.\n"
        f"  - Population Size: {CONFIG['Population_Size']} idividuals.\n"
        f"  - Number of generations: {CONFIG['Number_of_Generations']} generations.\n"
        f"  - Seed: '{seed}'.\n"
    )


#This is a script file.
if __name__ == '__main__':
    main(utils.seed_user_input())
