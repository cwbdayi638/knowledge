import smtplib
from email.mime.text import MIMEText
from email.header import Header

smtp_server = "smtp.gmail.com"
smtp_port = 587
sender_email = "cwbdayi@gmail.com"
password = "gncgcncvzvnkkitg"

receiver_email = "oceanicdayi@gmail.com"
subject = "應力與應變專題研究 (3/5)"

with open("earthquake_report_3.txt", "r", encoding="utf-8") as f:
    body = f.read()

message = MIMEText(body, "plain", "utf-8")
message["From"] = sender_email
message["To"] = receiver_email
message["Subject"] = Header(subject, "utf-8")

try:
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    server.login(sender_email, password)
    server.sendmail(sender_email, [receiver_email], message.as_string())
    server.quit()
    print("Email sent successfully.")
except Exception as e:
    print(f"Failed to send email: {e}")
