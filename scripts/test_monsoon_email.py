#!/usr/bin/env python3
"""
Test script to preview monsoon email content without sending
This shows what would be sent to oceanicdayi@gmail.com
"""
import os

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
    
    # Display email preview
    print("=" * 80)
    print("EMAIL PREVIEW - MONSOON INFORMATION")
    print("=" * 80)
    print()
    print(f"To: {to_email}")
    print(f"Subject: {subject}")
    print()
    print("Body Preview:")
    print("-" * 80)
    print(body[:500] + "..." if len(body) > 500 else body)
    print("-" * 80)
    print()
    print(f"Total Content Length: {len(body)} characters")
    print(f"Monsoon Document Length: {len(monsoon_content)} characters")
    print()
    print("=" * 80)
    print("✓ Email content prepared successfully!")
    print()
    print("To actually send this email, run:")
    print("  python3 scripts/send_monsoon_email.py")
    print()
    print("Make sure these environment variables are set:")
    print("  - SENDER_EMAIL_NEW")
    print("  - CWBDAYI_EMAIL_PASSWORD")
    print("=" * 80)
    
    return True

if __name__ == "__main__":
    import sys
    success = main()
    sys.exit(0 if success else 1)
