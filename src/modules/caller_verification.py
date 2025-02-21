# modules/caller_verification.py
# A simple whitelist of trusted caller numbers.
trusted_numbers = {"+18001234567": "Bank A", "+18007654321": "Bank B"}


def is_trusted_number(caller_number):
    """
    Check if the provided caller number is in the trusted list.

    :param caller_number: The incoming caller's phone number.
    :return: True if trusted, False otherwise.
    """
    return caller_number in trusted_numbers


if __name__ == "__main__":
    caller = "+18001234567"
    if is_trusted_number(caller):
        print("Caller is trusted:", trusted_numbers[caller])
    else:
        print("Caller not recognized.")
