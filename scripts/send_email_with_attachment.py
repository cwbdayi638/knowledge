import smtplib
import sys
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

def send_email_with_attachment(to_email, subject, body, file_path):
    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    sender_email = os.getenv('SENDER_EMAIL_NEW')
    password = os.getenv('CWBDAYI_EMAIL_PASSWORD')
    
    if not sender_email or not password:
        print("Error: Email credentials not found in environment variables.")
        print("Please set SENDER_EMAIL_NEW and CWBDAYI_EMAIL_PASSWORD")
        return False

    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = to_email
    msg['Subject'] = subject

    msg.attach(MIMEText(body, 'plain'))

    if os.path.exists(file_path):
        filename = os.path.basename(file_path)
        with open(file_path, "rb") as attachment:
            part = MIMEBase("application", "octet-stream")
            part.set_payload(attachment.read())
        
        encoders.encode_base64(part)
        part.add_header(
            "Content-Disposition",
            f"attachment; filename={filename}",
        )
        msg.attach(part)

    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(sender_email, password)
        text = msg.as_string()
        server.sendmail(sender_email, to_email, text)
        server.quit()
        return True
    except Exception as e:
        print(f"Error: {e}")
        return False

if __name__ == "__main__":
    if len(sys.argv) < 5:
        print("Usage: python3 send_email_with_attachment.py <to> <subject> <body> <file_path>")
        sys.exit(1)
    
    to = sys.argv[1]
    subject = sys.argv[2]
    body = sys.argv[3]
    file_path = sys.argv[4]
    
    if send_email_with_attachment(to, subject, body, file_path):
        print("Email with attachment sent successfully!")
    else:
        print("Failed to send email.")
