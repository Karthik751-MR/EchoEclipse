import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import pywhatkit as kt
import datetime


def send_email_alert(risk_score, keywords, user_email):
    # SMTP configuration (using Gmail's free SMTP server as an example)
    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    smtp_user = "your_email@gmail.com"  # update with your email address
    smtp_password = "your_app_password"  # update with your app password

    subject = "Scam Call Alert!"
    message = (
        f"Scam Alert! Suspicious call detected (Risk Score: {risk_score}).\n"
        f"Keywords: {', '.join(keywords) if keywords else 'None'}."
    )

    # Compose the email
    msg = MIMEMultipart()
    msg["From"] = smtp_user
    msg["To"] = user_email
    msg["Subject"] = subject
    msg.attach(MIMEText(message, "plain"))

    try:
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()  # Secure the connection
            server.login(smtp_user, smtp_password)
            server.send_message(msg)
        print(f"Email alert sent to {user_email}")
    except Exception as e:
        print(f"Error sending email: {e}")


def send_whatsapp_alert(risk_score, keywords, user_phone):
    # Construct the message
    message = (
        f"Scam Alert! Suspicious call detected (Risk Score: {risk_score}).\n"
        f"Keywords: {', '.join(keywords) if keywords else 'None'}."
    )
    # pywhatkit requires a scheduled time at least 1 minute in the future.
    now = datetime.datetime.now()
    send_hour = now.hour
    send_minute = now.minute + 1  # schedule for next minute

    try:
        # pywhatkit.sendwhatmsg expects the phone number in international format,
        # e.g. "+1234567890"
        kt.sendwhatmsg(
            user_phone, message, send_hour, send_minute, wait_time=20, tab_close=True
        )
        print(f"WhatsApp alert scheduled for {user_phone}")
    except Exception as e:
        print(f"Error sending WhatsApp message: {e}")


def alert_user(risk_score, keywords, user_contact):
    """
    Sends alerts to the user via email and WhatsApp.
    The user_contact parameter should be a dict with keys "email" and "whatsapp".
    Example:
        user_contact = {
            "email": "user@example.com",
            "whatsapp": "+1234567890"
        }
    """
    if "email" in user_contact and user_contact["email"]:
        send_email_alert(risk_score, keywords, user_contact["email"])
    if "whatsapp" in user_contact and user_contact["whatsapp"]:
        send_whatsapp_alert(risk_score, keywords, user_contact["whatsapp"])
