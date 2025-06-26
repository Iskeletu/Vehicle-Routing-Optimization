"""
Handles reading configuration values from a '.ini' file.

Author: Fábio Gandini  
Date: June 2025
"""

# Native Modules:
import configparser
import os


def load_config(path:str='./config.ini') -> dict:
    """
    Loads configuration values from the specified '.ini' file.

    Parameters:
        - path: str -> (Optional) Path to the configuration file (default: './config.ini').

    Returns:
        - A dictionary containing the following keys:
            'Number_of_Points': int
            'Grid_Size': int
            'Population_Size': int

    Raises:
        - FileNotFoundError: If the file does not exist.
        - KeyError: If the 'PARAMETERS' section is missing.
        - ValueError: If any expected key is missing or not an integer.
    """
    
    if not os.path.exists(path):
        raise FileNotFoundError(f"Configuration file not found at: {path}")

    configfile = configparser.ConfigParser()
    configfile.read(path)

    if 'PARAMETERS' not in configfile:
        raise KeyError("Missing [PARAMETERS] section in config file.")

    try:
        return {
            'Number_of_Points': int(configfile['PARAMETERS']['Number_of_Points']),
            'Grid_Size': int(configfile['PARAMETERS']['Grid_Size']),
            'Population_Size': int(configfile['PARAMETERS']['Population_Size']),
        }
    except KeyError as e:
        raise ValueError(f"Missing configuration key: {e}")
    except ValueError as e:
        raise ValueError(f"Invalid integer value in config file: {e}")


# This is NOT a script file.
if __name__ == '__main__':
    raise RuntimeError("This module is not a standalone script.")
