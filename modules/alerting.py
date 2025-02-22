import smtplib
from email.mime.text import MIMEText
import pywhatkit
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()


def send_whatsapp_message(message, phone_number):
    """
    Send a WhatsApp message using pywhatkit.

    Args:
        message (str): The message to send.
        phone_number (str): The recipient's phone number (with country code).

    Returns:
        bool: True if the message was sent successfully, False otherwise.
    """
    try:
        pywhatkit.sendwhatmsg_instantly(
            phone_no=phone_number, message=message, wait_time=15, tab_close=True
        )
        return True
    except Exception as e:
        print(f"WhatsApp Error: {str(e)}")
        return False


def send_sms(message, phone_number, carrier="att"):
    """
    Send an SMS via Email-to-SMS Gateway.

    Args:
        message (str): The message to send.
        phone_number (str): The recipient's phone number.
        carrier (str): The carrier of the recipient (default is "att").

    Returns:
        bool: True if the SMS was sent successfully, False otherwise.
    """
    # Carrier gateways
    carriers = {
        "att": "9159576794@txt.att.net",
        "verizon": "9159576794@vtext.com",
        "tmobile": "@tmomail.net",
        "sprint": "@messaging.sprintpcs.com",
    }

    # Get email credentials from environment variables
    email = os.getenv("ALERT_EMAIL")
    password = os.getenv("ALERT_EMAIL_PASSWORD")

    try:
        # Connect to SMTP server
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(email, password)

        # Create the email message
        msg = MIMEText(message)
        msg["From"] = email
        msg["To"] = f"{phone_number}{carriers[carrier]}"

        # Send the email (SMS)
        server.sendmail(email, [msg["To"]], msg.as_string())
        server.quit()
        return True
    except Exception as e:
        print(f"SMS Error: {str(e)}")
        return False


def send_email(message, recipient_email):
    """
    Send an email alert via SMTP.

    Args:
        message (str): The message to send.
        recipient_email (str): The recipient's email address.

    Returns:
        bool: True if the email was sent successfully, False otherwise.
    """
    # Get email credentials from environment variables
    email = os.getenv("ALERT_EMAIL")
    password = os.getenv("ALERT_EMAIL_PASSWORD")

    try:
        # Connect to SMTP server
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(email, password)

        # Create the email message
        msg = MIMEText(message)
        msg["Subject"] = "Scam Call Alert"
        msg["From"] = email
        msg["To"] = recipient_email

        # Send the email
        server.sendmail(email, [recipient_email], msg.as_string())
        server.quit()
        return True
    except Exception as e:
        print(f"Email Error: {str(e)}")
        return False


def alert_user(risk_score, keywords, user_contact):
    """
    Send alerts to the user via WhatsApp, SMS, and email if the risk score is high.

    Args:
        risk_score (int): The calculated risk score.
        keywords (list): List of detected scam keywords.
        user_contact (dict): User's contact details (email, WhatsApp, phone number).

    Returns:
        None
    """
    # Prepare the alert message
    alert_message = (
        f"🚨 High-Risk Call Detected!\n"
        f"Risk Score: {risk_score}\n"
        f"Keywords: {', '.join(keywords)}"
    )

    # Send WhatsApp message
    if user_contact.get("whatsapp"):
        send_whatsapp_message(alert_message, user_contact["whatsapp"])

    # Send SMS
    if user_contact.get("phone"):
        send_sms(alert_message, user_contact["phone"])

    # Send Email
    if user_contact.get("email"):
        send_email(alert_message, user_contact["email"])
