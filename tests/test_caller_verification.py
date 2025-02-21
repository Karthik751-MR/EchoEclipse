# tests/test_caller_verification.py
import unittest
from src.modules.caller_verification import is_trusted_number


class TestCallerVerification(unittest.TestCase):
    def test_trusted_number(self):
        # Using a number from our trusted list
        self.assertTrue(is_trusted_number("+18001234567"))

    def test_untrusted_number(self):
        self.assertFalse(is_trusted_number("+12345678900"))


if __name__ == "__main__":
    unittest.main()
