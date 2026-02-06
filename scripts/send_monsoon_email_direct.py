#!/usr/bin/env python3
"""
Direct script to send monsoon email using EMAIL_PASSWORD from environment
This script can be run in GitHub Actions or locally with proper credentials
"""
import os
import sys
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_monsoon_email_direct():
    """Send monsoon email directly using EMAIL_PASSWORD"""
    
    # Read monsoon content
    script_dir = os.path.dirname(os.path.abspath(__file__))
    monsoon_file = os.path.join(script_dir, '..', 'monsoon.md')
    
    try:
        with open(monsoon_file, 'r', encoding='utf-8') as f:
            monsoon_content = f.read()
    except Exception as e:
        print(f"❌ Error reading monsoon.md: {e}")
        return False
    
    # Email configuration
    to_email = "oceanicdayi@gmail.com"
    sender_email = os.getenv('SENDER_EMAIL_NEW') or os.getenv('EMAIL_FROM') or to_email
    password = os.getenv('CWBDAYI_EMAIL_PASSWORD') or os.getenv('EMAIL_PASSWORD')
    subject = "氣象學知識：季風 (Monsoon) 完整說明"
    
    if not password:
        print("❌ Error: Email credentials not found in environment variables.")
        print("   Please set CWBDAYI_EMAIL_PASSWORD or EMAIL_PASSWORD")
        return False
    
    # Create email body
    body = f"""您好！

以下是關於氣象學中「季風 (Monsoon)」的完整說明：

{monsoon_content}

---
此郵件由 SeismoProphet 知識庫系統自動發送。
如有任何問題，請回覆此郵件。
"""
    
    print(f"📧 準備發送郵件")
    print(f"   收件人: {to_email}")
    print(f"   寄件人: {sender_email}")
    print(f"   主題: {subject}")
    print(f"   內容長度: {len(body)} 字元")
    print("-" * 60)
    
    # Send email
    try:
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = to_email
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain', 'utf-8'))
        
        print("🔌 連接至 SMTP 伺服器...")
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        
        print("🔐 登入中...")
        server.login(sender_email, password)
        
        print("📤 發送郵件...")
        server.sendmail(sender_email, to_email, msg.as_string())
        server.quit()
        
        print("-" * 60)
        print("✅ 郵件發送成功！")
        print(f"   已發送至: {to_email}")
        return True
        
    except smtplib.SMTPAuthenticationError as e:
        print(f"❌ 認證失敗: {e}")
        print("   請檢查 EMAIL_PASSWORD 是否正確")
        return False
    except Exception as e:
        print(f"❌ 發送失敗: {e}")
        return False

if __name__ == "__main__":
    success = send_monsoon_email_direct()
    sys.exit(0 if success else 1)
