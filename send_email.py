import smtplib
import sys
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(to_email, subject, body):
    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    sender_email = "cwbdayi@gmail.com"
    password = "gncgcncvzvnkkitg"

    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = to_email
    msg['Subject'] = subject

    msg.attach(MIMEText(body, 'plain'))

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
    if len(sys.argv) < 4:
        print("Usage: python3 send_email.py <to> <subject> <body>")
        sys.exit(1)
    
    to = sys.argv[1]
    subject = sys.argv[2]
    body = sys.argv[3]
    
    if send_email(to, subject, body):
        print("Email sent successfully!")
    else:
        print("Failed to send email.")
