import json

# Cache the trusted numbers so that the file is not reloaded on every call
_TRUSTED_NUMBERS_CACHE = None


def load_trusted_numbers():
    global _TRUSTED_NUMBERS_CACHE
    if _TRUSTED_NUMBERS_CACHE is None:
        try:
            with open("config/trusted_numbers.json", "r") as file:
                _TRUSTED_NUMBERS_CACHE = json.load(file)
        except Exception as e:
            _TRUSTED_NUMBERS_CACHE = {}
            print(f"Error loading trusted numbers: {e}")
    return _TRUSTED_NUMBERS_CACHE


def is_trusted_number(caller_number):
    trusted_numbers = load_trusted_numbers()
    return trusted_numbers.get(caller_number, None)
