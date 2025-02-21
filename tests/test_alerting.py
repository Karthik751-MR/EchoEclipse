# tests/test_alerting.py
import unittest
from src.modules.alerting import send_email_alert


class TestAlerting(unittest.TestCase):
    def test_send_email_alert(self):
        # Test email alert by sending to a dummy email address.
        # For unit tests, you might want to mock smtplib.SMTP.
        try:
            send_email_alert(
                "Test Alert",
                "This is a test alert from ScamDetector.",
                "test@example.com",
            )
        except Exception as e:
            self.fail(f"send_email_alert raised an exception: {e}")


if __name__ == "__main__":
    unittest.main()
