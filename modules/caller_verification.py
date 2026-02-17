import json
import os
from pathlib import Path

# Cache the trusted numbers so that the file is not reloaded on every call
_TRUSTED_NUMBERS_CACHE = None
TRUSTED_NUMBERS_PATH = Path(__file__).resolve().parent.parent / "config" / "trusted_numbers.json"


def load_trusted_numbers():
    """
    Load trusted numbers from a JSON file and cache them.

    Returns:
        dict: A dictionary of trusted numbers with metadata.
    """
    global _TRUSTED_NUMBERS_CACHE
    if _TRUSTED_NUMBERS_CACHE is None:
        try:
            # Ensure the config directory exists
            os.makedirs(TRUSTED_NUMBERS_PATH.parent, exist_ok=True)

            # Load trusted numbers from the JSON file
            with open(TRUSTED_NUMBERS_PATH, "r", encoding="utf-8") as file:
                _TRUSTED_NUMBERS_CACHE = json.load(file)
        except FileNotFoundError:
            print("Trusted numbers file not found. Creating an empty one.")
            _TRUSTED_NUMBERS_CACHE = {}
            # Create an empty JSON file if it doesn't exist
            with open(TRUSTED_NUMBERS_PATH, "w", encoding="utf-8") as file:
                json.dump(_TRUSTED_NUMBERS_CACHE, file)
        except json.JSONDecodeError:
            print("Error decoding JSON. The file may be corrupted.")
            _TRUSTED_NUMBERS_CACHE = {}
        except Exception as e:
            print(f"Error loading trusted numbers: {e}")
            _TRUSTED_NUMBERS_CACHE = {}
    return _TRUSTED_NUMBERS_CACHE


def is_trusted_number(caller_number):
    """
    Check if a caller number is trusted.

    Args:
        caller_number (str): The caller's phone number.

    Returns:
        bool: True if the number is trusted, False otherwise.
    """
    trusted_numbers = load_trusted_numbers()
    return caller_number in trusted_numbers
