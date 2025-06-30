"""
Executes multiple simulations with different seed values,
comparing a standard random population against an evolutionary genetic approach.

Author: Fábio Gandini
Date: June 2025
"""

# Native Modules:
import random
from time import time
from pathlib import Path

# External Modules:
import numpy as np
from scipy.spatial.distance import cdist

# Internal Modules:
import utils
import routing
import plotting
import config as cfg
import genetic_evolution
import file_handling as fh

# Constants:
CONFIG = cfg.load_config()
DECIMAL_DIGITS = 2


def _run_comparative(seed:int) -> dict:
    """
    Private local function: Runs a single simulation comparison between the Random Initial Population Algorithm
    (RIPA) and the Evolutionary Algoritm (EA) using the provided seed.

    Parameters:
        - `seed: int` -> Seed value for reproducibility.

    Returns:
        - A dictionary type containing the following keys: \n
            `'seed'`: int        -> Seed used for both RIPA and EA Algorithms.
            `'RIPA'`: dict       -> RIPA results.
                `'Distance'`: dict   -> RIPA best distance.
                `'Time'`: dict       -> RIPA elapsed time.
                `'Route'`: dict      -> RIPA best route.
            `'EA'`: dict         -> EA results.
                `'Distance'`: dict   -> EA distance.
                `'Time'`: dict       -> EA elapsed time.
                `'Route'`: dict      -> EA route.
    """

    # Seeds the plot point generation and population:
    np.random.seed(seed)
    random.seed(seed)

    # Generate points and distance matrix:
    points = routing.gen_2d_grid(CONFIG['Number_of_Points'], CONFIG['Grid_Size'])
    dist_matrix = cdist(points, points)

    # Random Initial Population Algorithm (RIPA):
    RIP_start_time = time()
    RIP_population = routing.gen_initial_pop(CONFIG['Population_Size'], CONFIG['Number_of_Points'])
    RIP_evaluation = [routing.evaluate_route(route, dist_matrix) for route in RIP_population]
    rand_best_idx = np.argmin(RIP_evaluation)
    best_RIP_route = RIP_population[rand_best_idx]
    best_RIP_distance = round(RIP_evaluation[rand_best_idx], DECIMAL_DIGITS)
    RIP_elapsed_time = round(time() - RIP_start_time, DECIMAL_DIGITS)

    # Evolutionary Algorithm (EA):
    EA_start_time = time()
    EA_result = genetic_evolution.run_evolutionary_experiment(CONFIG, points, seed)
    best_EA_distance = round(EA_result['distance'], DECIMAL_DIGITS)
    EA_elapsed_time = round(time() - EA_start_time, DECIMAL_DIGITS)

    # Save RIPA and EA route plots:
    fh.save_plot(CONFIG, plotting.plot_route(best_RIP_route, points, f"{seed} - Random Initial Population Algorithm"), "RIPA", str(seed))
    fh.save_plot(CONFIG, plotting.plot_route(EA_result['route'], points, f"{seed} - Evolutionary Algorithm"), "EA", str(seed))
    
    return {
        "Seed": seed,
        "RIPA": {
            "Distance": best_RIP_distance,
            "Time": RIP_elapsed_time,
            "Route": best_RIP_route
        },
        "EA": {
            "Distance": best_EA_distance,
            "Time": EA_elapsed_time,
            "Route": EA_result['route']
        }
    }


def run_all():
    """
    Runs all simulations and stores results.
    """

    print("Running comparative simulations...\n")
    seed_list:list[int] = utils.generate_seeds(CONFIG['Number_of_Seeds'])
    results:list[dict] = []

    for seed in seed_list:
        result = _run_comparative(seed)
        results.append(result)

        print(
            f"Seed: '{seed}'.\n"

            "Random Initial Population Algorithm:\n"
            f"  -Distance: {result['RIPA']['Distance']}.\n"
            f"  -Elapsed Time: {result['RIPA']['Time']}s.\n"
            
            "Evolutionary Algorithm:\n"
            f"  -Distance: {result['EA']['Distance']}.\n"
            f"  -Elapsed Time: {result['EA']['Time']}s.\n"
        )

    # Save results to CSV file:
    fh.save_results_csv(CONFIG, results)
    print("\nResults saved to:", Path(f"{CONFIG['Output_Folder_Name']}\\{CONFIG['CSV_File_Name']}.csv").absolute(), "\n")


#This is a script file.
if __name__ == '__main__':
    run_all()
