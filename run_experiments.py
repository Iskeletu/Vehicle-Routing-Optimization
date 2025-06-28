"""
Runs multiple simulations using different seed values, saving
the results as CSV files and route plots as PNG images.

Author: Fábio Gandini
Date: June 2025
"""

# Native Modules:
import random
from time import time
from pathlib import Path

# Local Modules:
import routing
import plotting
import config as cfg
import file_handling as fh
from utils import generate_seeds

# External Modules:
import numpy as np
from scipy.spatial.distance import cdist

# Constants:
CONFIG = cfg.load_config()
DECIMAL_DIGITS = 2


def run_experiment(seed:int) -> dict:
    """
    Runs a single simulation using the provided seed.

    Parameters:
        - `seed: int` -> Seed value for reproducibility.

    Returns:
        - A dictiorany type containing the seed, best route, total distance.
    """

    np.random.seed(seed)
    random.seed(seed)

    points = routing.gen_2d_grid(CONFIG['Number_of_Points'], CONFIG['Grid_Size'])
    dist_matrix = cdist(points, points)
    pop = routing.gen_initial_pop(CONFIG['Population_Size'], CONFIG['Number_of_Points'])
    fitness = [routing.evaluate_route(route, dist_matrix) for route in pop]
    best_index = np.argmin(fitness)
    best_route = pop[best_index]
    best_distance = fitness[best_index]

    fig = plotting.plot_route(best_route, points)
    fh.save_plot(CONFIG, fig, str(seed))

    return {
        "seed": seed,
        "route": best_route,
        "distance": round(best_distance, DECIMAL_DIGITS)
    }


def run_all():
    """
    Runs all simulations for the defined seeds and saves the results in a CSV file.
    """

    seed_list:list[int] = generate_seeds(CONFIG['Number_of_Seeds'])
    results:list[dict] = []

    print("Running experiments...")
    for seed in seed_list:
        start = time() # Star time of simulation execution for calculating elapsed time.
        result = run_experiment(seed)
        elapsed = round(time() - start, DECIMAL_DIGITS)
        result["time"] = elapsed # Adds elpased execution time of the simulation to the dict.
        results.append(result)
        
        print(f"\nSeed: '{seed}'.")
        print(f"Best distance: {result['distance']}.")
        print(f"Elapsed time: {elapsed} seconds.")

    fh.save_results_csv(CONFIG, results)
    print("\nResults saved to:", Path(f"{CONFIG['Output_Folder_Name']}\\{CONFIG['CSV_File_Name']}.csv").absolute(), "\n")
    


#This is a script file.
if __name__ == '__main__':
    run_all()
