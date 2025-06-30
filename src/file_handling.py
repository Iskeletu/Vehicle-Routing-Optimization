"""
Utility functions to handle file interactions.

Author: Fábio Gandini
Date: June 2025
"""

# Native Modules:
import os
import csv
from pathlib import Path
from typing import Literal

# External Modules:
import matplotlib.pyplot as mpl

# Constants:
PROJECT_DIRECTORY = Path(os.path.abspath(__file__)).parent.parent.resolve()


def save_plot(config:dict, fig:mpl.Figure, alg_type:Literal['RIPA', 'EA'], seed:str) -> None:
    """
    Saves a matplotlib Figure to the path specified in the configuration file as a .PNG image.

    Parameters:
        - `config: dict`                    -> Loaded config dictionary.
        - `fig: mpl.Figure`                 -> The matplotlib figure object to save.
        - `alg_type: Literal['RIPA', 'EA']`  -> Indicates whether the plot came from a random population algorithm or the evolutionary algorithm.
        - `seed: int`                       -> String to replace 'seed' file name parameter.
    """

    if str(alg_type) not in ['RIPA', 'EA']:
        raise ValueError(f"Invalid type_of_execution: {alg_type}. Expected 'RIPA' or 'EA'.")

    path:Path = Path(f"{PROJECT_DIRECTORY}\\{config['Output_Folder_Name']}\\{str(config['Image_File_Name']).format(seed=seed)}_{str(alg_type)}.png")
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

    path:Path = Path(f"{PROJECT_DIRECTORY}\\{config['Output_Folder_Name']}\\{config['CSV_File_Name']}.csv")
    path.parent.mkdir(parents=True, exist_ok=True) # Ensures path is ok.

    with path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=[
            "Seed",
            "RIPA_Distance", "RIPA_Time", "RIPA_Route",
            "EA_Distance", "EA_Time", "EA_Route"
        ])
        writer.writeheader()
        for entry in data:
            writer.writerow({
                "Seed": entry["Seed"],
                "RIPA_Distance": entry["RIPA"]["Distance"],
                "RIPA_Time": entry["RIPA"]["Time"],
                "RIPA_Route": entry["RIPA"]["Route"],
                "EA_Distance": entry["EA"]["Distance"],
                "EA_Time": entry["EA"]["Time"],
                "EA_Route": entry["EA"]["Route"]
            })


# This is NOT a script file.
if __name__ == '__main__':
    raise RuntimeError("This module is not a standalone script.")
