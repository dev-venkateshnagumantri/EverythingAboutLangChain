from dotenv import load_dotenv
import smtplib
from email.message import EmailMessage
import os

load_dotenv()

DEFAULT_FROM_EMAIL = os.getenv("DEFAULT_FROM_EMAIL")
EMAIL_HOST = os.getenv("EMAIL_HOST")
EMAIL_PORT = int(os.getenv("EMAIL_PORT", "587"))
EMAIL_HOST_USER = os.getenv("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = os.getenv("EMAIL_HOST_PASSWORD")

if not all((DEFAULT_FROM_EMAIL, EMAIL_HOST, EMAIL_HOST_USER, EMAIL_HOST_PASSWORD)):
    raise RuntimeError("One or more email settings are missing")

def send_email(subject: str, to_mail: str, body: str) -> str:
    from_mail = DEFAULT_FROM_EMAIL
    msg = EmailMessage()
    msg["Subject"] = subject
    msg["From"] = from_mail
    msg["To"] = to_mail
    msg.set_content(body)
    try:
        with smtplib.SMTP(EMAIL_HOST, EMAIL_PORT) as server:
            server.starttls()
            server.login(EMAIL_HOST_USER, EMAIL_HOST_PASSWORD)
            server.send_message(msg)
    except Exception as exc:
        return f"Failed to send email: {exc}"

    print("email sent! Status: Success.")
    return "Email sent successfully!"

if __name__ == '__main__':
    print('testing the helper module')
    send_email('test', 'venkateshnagumantri11@gmail.com', 'testbody')


