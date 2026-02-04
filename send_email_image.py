import smtplib
import sys
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
import os

def send_email_with_image(to_email, subject, body, image_path=None):
    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    sender_email = "cwbdayi@gmail.com"
    password = "gncgcncvzvnkkitg"

    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = to_email
    msg['Subject'] = subject

    msg.attach(MIMEText(body, 'plain'))

    # Attach image if provided
    if image_path and os.path.exists(image_path):
        with open(image_path, 'rb') as f:
            img_data = f.read()
        image = MIMEImage(img_data, name=os.path.basename(image_path))
        msg.attach(image)

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
        print("Usage: python3 send_email_image.py <to> <subject> <body> [image_path]")
        sys.exit(1)
    
    to = sys.argv[1]
    subject = sys.argv[2]
    body = sys.argv[3]
    image = sys.argv[4] if len(sys.argv) > 4 else None
    
    if send_email_with_image(to, subject, body, image):
        print("Email sent successfully!")
    else:
        print("Failed to send email.")
