"""
Utility functions to handle file interactions.

Author: Fábio Gandini
Date: June 2025
"""

# Native Modules:
import csv
from pathlib import Path

# External Modules:
import matplotlib.pyplot as mpl


def save_plot(config:dict, fig:mpl.Figure, seed:str|None=None) -> None:
    """
    Saves a matplotlib Figure to the path specified in the configuration file as a .PNG image.

    Parameters:
        - `config: dict`    -> Loaded config dictionary.
        - `fig: mpl.Figure` -> The matplotlib figure object to save.
        - `seed: int`       -> String to replace 'seed' file name parameter.
    """

    if seed is None: seed = "Seed_Not_Provided"

    path:Path = Path(f"{config['Output_Folder_Name']}\\{str(config['Image_File_Name']).format(seed=seed)}.png")
    path.parent.mkdir(parents=True, exist_ok=True) # Ensures path is ok.

    fig.savefig(path)
    mpl.close(fig)


def save_results_csv(config:dict, data:list[dict]) -> None:
    """
    Saves a list of result dictionaries to the path specified in the configuration file as a .CSV file.

    Parameters:
        - `config: dict`        -> Loaded config dictionary.
        - `data: list[dict]`    -> List of results, each containing 'seed', 'distance', 'time', and 'route'.
    """

    path:Path = Path(f"{config['Output_Folder_Name']}\\{config['CSV_File_Name']}.csv")
    path.parent.mkdir(parents=True, exist_ok=True) # Ensures path is ok.

    with path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["seed", "distance", "time", "route"])
        writer.writeheader()
        writer.writerows(data)


# This is NOT a script file.
if __name__ == '__main__':
    raise RuntimeError("This module is not a standalone script.")
