"""
Handles reading configuration values from a '.INI' file.

Author: Fábio Gandini  
Date: June 2025
"""

# Native Modules:
import os
import configparser
from pathlib import Path

# Constants:
STANDARD_PATH = Path('.\\config.INI').absolute()


def _validate_config(config:dict) -> None:
    """
    Validates if the configuration values are within acceptable bounds.

    Parameters:
        - `config: dict` -> Configuration dictionary to validate.

    Raises:
        - `ValueError:` If any value is outside acceptable limits.
    """

    if not (config['Number_of_Points'] >= 10):
        raise ValueError("Number_of_Points must be above or equal to 10")
    if not (config['Grid_Size'] >= 100):
        raise ValueError("Grid_Size must be above or equal to 100")
    if not (config['Population_Size'] >= 100):
        raise ValueError("Population_Size must be above or equal to 100")
    if not (config['Number_of_Seeds'] >= 1):
        raise ValueError("Number_of_Seeds must be above or equal to 1")


def load_config(path:Path=STANDARD_PATH) -> dict:
    """
    Loads configuration values from the specified '.INI' file.

    Parameters:
        - `path: str` -> (Optional) Path to the configuration file (default: '{project_directory}\\config.INI').

    Returns:
        - A dictionary containing the following keys:   \n
            `'Number_of_Points': int`                   \n
            `'Grid_Size': int`                          \n
            `'Population_Size': int`                    \n
            `'Output_Folder': str`                      \n
            `'CSV_Name': str`                           \n
            `'Image_Name_Template': str`                \n
            `'Number_of_Seeds': int`

    Raises:
        - `FileNotFoundError`: If the file does not exist.
        - `KeyError`: If a required section is missing.
        - `ValueError`: If any expected key is missing or has the wrong type.
    """
    
    # Validates configuration file existance given the path parameter:
    if not os.path.exists(path):
        raise FileNotFoundError(f"Configuration file not found at: {path}")

    # Reads configuration file:
    configfile:configparser.ConfigParser = configparser.ConfigParser()
    configfile.read(path)

    # Validates configuration file structure integrty:
    if 'PARAMETERS' not in configfile or 'OUTPUT' not in configfile:
        raise KeyError("Missing required sections in the configuration file: [PARAMETERS] and/or [OUTPUT]")

    try:
        config = {
            'Number_of_Points':     int(configfile['PARAMETERS']['Number_of_Points']),
            'Grid_Size':            int(configfile['PARAMETERS']['Grid_Size']),
            'Population_Size':      int(configfile['PARAMETERS']['Population_Size']),
            'Output_Folder_Name':   str(configfile['OUTPUT']['Folder_Name']),
            'CSV_File_Name':        str(configfile['OUTPUT']['CSV_File_Name']),
            'Image_File_Name':      str(configfile['OUTPUT']['Image_File_Name']),
            'Number_of_Seeds':      int(configfile['OUTPUT']['Number_of_Seeds'])
        }
    except KeyError as e:
        raise ValueError(f"Missing configuration key: {e}")
    except ValueError as e:
        raise ValueError(f"Invalid integer value in config file: {e}")

    _validate_config(config) # Validates if values are within valid bounds.
    return config


# This is NOT a script file.
if __name__ == '__main__':
    raise RuntimeError("This module is not a standalone script.")
