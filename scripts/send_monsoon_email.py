#!/usr/bin/env python3
"""
Script to send monsoon information email
Reads monsoon.md and sends it to the specified email address
"""
import sys
import os

# Add the parent directory to the Python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from send_email import send_email

def main():
    # Read the monsoon.md file
    monsoon_file = os.path.join(os.path.dirname(__file__), '..', 'monsoon.md')
    
    try:
        with open(monsoon_file, 'r', encoding='utf-8') as f:
            monsoon_content = f.read()
    except Exception as e:
        print(f"Error reading monsoon.md: {e}")
        return False
    
    # Email configuration
    to_email = "oceanicdayi@gmail.com"
    subject = "氣象學知識：季風 (Monsoon) 完整說明"
    
    # Create email body
    body = f"""您好！

以下是關於氣象學中「季風 (Monsoon)」的完整說明：

{monsoon_content}

---
此郵件由 SeismoProphet 知識庫系統自動發送。
如有任何問題，請回覆此郵件。
"""
    
    # Send email
    print(f"準備發送郵件至: {to_email}")
    print(f"主題: {subject}")
    print(f"內容長度: {len(body)} 字元")
    print("-" * 50)
    
    if send_email(to_email, subject, body):
        print("✓ 郵件發送成功！")
        return True
    else:
        print("✗ 郵件發送失敗。")
        return False

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
