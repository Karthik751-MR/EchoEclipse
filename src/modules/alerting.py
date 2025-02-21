# modules/alerting.py
import smtplib
from email.mime.text import MIMEText
from src.config import EMAIL_ADDRESS, EMAIL_PASSWORD


def send_email_alert(subject, message, to_email):
    """
    Send an email alert using Gmail's SMTP server.

    :param subject: The email subject.
    :param message: The email message content.
    :param to_email: Recipient's email address.
    """
    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    from_email = EMAIL_ADDRESS

    msg = MIMEText(message)
    msg["Subject"] = subject
    msg["From"] = from_email
    msg["To"] = to_email

    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    server.login(from_email, EMAIL_PASSWORD)
    server.send_message(msg)
    server.quit()


def send_sms_alert_via_email(message, phone_number, carrier_gateway):
    """
    Send an SMS alert using the carrier's email-to-SMS gateway.

    :param message: The SMS message content.
    :param phone_number: The recipient's phone number (digits only).
    :param carrier_gateway: The carrier's SMS gateway domain (e.g., "txt.att.net" for AT&T).
    """
    # Construct the recipient email address for SMS.
    to_email = f"{phone_number}@{carrier_gateway}"
    # No subject is required for SMS alerts.
    send_email_alert("", message, to_email)


if __name__ == "__main__":
    # Test email alert.
    send_email_alert(
        "Test Email Alert",
        "This is a test email from ScamDetector.",
        "recipient@example.com",
    )
    print("Test email alert sent!")

    # To test SMS alert via email-to-SMS gateway, uncomment and update the line below:
    # send_sms_alert_via_email("Test SMS from ScamDetector.", "1234567890", "txt.att.net")
    # print("Test SMS alert sent via email!")
