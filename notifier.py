import smtplib
from email.mime.text import MIMEText
import os
from dotenv import load_dotenv

load_dotenv()

def send_email_notification(subject, body, to_email):
    sender_email = os.getenv("GMAIL_USER")
    sender_password = os.getenv("GMAIL_PASS")

    if not sender_email or not sender_password:
        raise ValueError("Gmail user not found! did you setup .env file?")

    # creating email
    msg = MIMEText(body, "plain")
    msg["Subject"] = subject
    msg["From"] = sender_email
    msg["To"] = to_email

    #connecting to gmail smtp
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(sender_email, sender_password)

        #sending email
        server.sendmail(sender_email, to_email, msg.as_string())
        server.quit()

        print("email sent successfully")

    except Exception as e:
        print("error handling email:", e)


