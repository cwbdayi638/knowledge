#!/usr/bin/env python3
"""
Standalone script to send OpenClaw news report via email
This script can be run independently to send the latest report
"""

import os
import sys
import smtplib
import ssl
from datetime import datetime
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

# Configuration
EMAIL_TO = os.environ.get('EMAIL_TO', 'oceanicdayi@gmail.com')
EMAIL_PASSWORD = os.environ.get('EMAIL_PASSWORD', '')
SENDER_EMAIL = os.environ.get('SENDER_EMAIL_NEW', '')
CWBDAYI_EMAIL_PASSWORD = os.environ.get('CWBDAYI_EMAIL_PASSWORD', EMAIL_PASSWORD)
DATE_STR = datetime.now().strftime('%Y-%m-%d')
DATE_DISPLAY_ZH = datetime.now().strftime('%Y年%m月%d日')

def send_email_with_attachment(filename):
    """
    Send email with markdown file attachment
    """
    print(f"📧 準備發送電子郵件至 {EMAIL_TO}...")
    print(f"📎 附件檔案：{filename}")
    
    # Determine which email credentials to use
    password = CWBDAYI_EMAIL_PASSWORD if CWBDAYI_EMAIL_PASSWORD else EMAIL_PASSWORD
    sender = SENDER_EMAIL if SENDER_EMAIL else EMAIL_TO
    
    if not password:
        print("❌ 錯誤：未設定電子郵件密碼")
        print("請設定以下環境變數之一：")
        print("  - EMAIL_PASSWORD")
        print("  - CWBDAYI_EMAIL_PASSWORD")
        return False
    
    if not sender:
        print("❌ 錯誤：未設定發件人電子郵件地址")
        print("請設定環境變數：SENDER_EMAIL_NEW")
        return False
    
    if not os.path.exists(filename):
        print(f"❌ 錯誤：找不到檔案 {filename}")
        return False
    
    try:
        # Read file content
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Create message
        message = MIMEMultipart()
        message["Subject"] = f"OpenClaw 最新消息報告 - {DATE_DISPLAY_ZH}"
        message["From"] = sender
        message["To"] = EMAIL_TO
        
        # Email body with summary
        text_content = f"""OpenClaw 最新消息報告
日期：{DATE_DISPLAY_ZH}

請參閱附件中的完整 Markdown 報告。

摘要：
{content[:500]}...

---
完整報告請見附件：{filename}

本報告由 AI 新聞收集系統自動產生。
GitHub 儲存庫：https://github.com/cwbdayi638/knowledge
"""
        
        # Attach plain text version
        part1 = MIMEText(text_content, "plain", "utf-8")
        message.attach(part1)
        
        # Attach the markdown file
        print(f"📎 正在附加檔案：{filename}")
        with open(filename, "rb") as attachment:
            part = MIMEBase("application", "octet-stream")
            part.set_payload(attachment.read())
        
        encoders.encode_base64(part)
        part.add_header(
            "Content-Disposition",
            f"attachment; filename={os.path.basename(filename)}",
        )
        message.attach(part)
        print(f"✅ 檔案已附加")
        
        # Try Gmail SMTP with SSL first
        print(f"🔐 正在連接 Gmail SMTP (SSL)...")
        print(f"   發件人：{sender}")
        print(f"   收件人：{EMAIL_TO}")
        
        try:
            context = ssl.create_default_context()
            with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
                print("🔑 正在驗證...")
                server.login(sender, password)
                print("📤 正在發送郵件...")
                server.sendmail(sender, EMAIL_TO, message.as_string())
            print("✅ 電子郵件發送成功！(使用 Gmail SMTP SSL)")
            return True
        except Exception as ssl_error:
            # Try with STARTTLS if SSL fails
            print(f"⚠️  SSL 連接失敗，嘗試 STARTTLS...")
            print(f"   錯誤訊息：{ssl_error}")
            context = ssl.create_default_context()
            with smtplib.SMTP("smtp.gmail.com", 587) as server:
                print("🔐 正在連接 Gmail SMTP (STARTTLS)...")
                server.starttls(context=context)
                print("🔑 正在驗證...")
                server.login(sender, password)
                print("📤 正在發送郵件...")
                server.sendmail(sender, EMAIL_TO, message.as_string())
            print("✅ 電子郵件發送成功！(使用 Gmail SMTP STARTTLS)")
            return True
        
    except Exception as e:
        print(f"❌ 發送電子郵件時發生錯誤：{e}")
        print("\n🔍 故障排除建議：")
        print("1. 確認 Gmail 帳號已啟用「兩步驟驗證」")
        print("2. 使用「應用程式密碼」而非一般密碼")
        print("3. 應用程式密碼產生位置：https://myaccount.google.com/apppasswords")
        print("4. 確認發件人和收件人電子郵件地址正確")
        print("5. 檢查網路連線是否正常")
        import traceback
        traceback.print_exc()
        return False

def main():
    """
    Main execution function
    """
    print("=" * 60)
    print("📧 OpenClaw 新聞報告郵件發送工具")
    print("=" * 60)
    print()
    
    # Find the latest report file
    filename = f'openclaw_news_report_{DATE_STR}.md'
    
    if not os.path.exists(filename):
        print(f"⚠️  找不到今日報告：{filename}")
        print("正在尋找最新的報告檔案...")
        
        # Try to find any openclaw report file
        import glob
        reports = sorted(glob.glob('openclaw_news_report_*.md'), reverse=True)
        if reports:
            filename = reports[0]
            print(f"✅ 找到報告檔案：{filename}")
        else:
            print("❌ 錯誤：找不到任何 OpenClaw 報告檔案")
            print("請先執行：python scripts/collect_openclaw_news.py")
            return 1
    
    print(f"📄 報告檔案：{filename}")
    print()
    
    # Check environment variables
    print("🔍 檢查環境變數...")
    if SENDER_EMAIL:
        print(f"✅ SENDER_EMAIL_NEW: {SENDER_EMAIL}")
    else:
        print("❌ SENDER_EMAIL_NEW: 未設定")
    
    if CWBDAYI_EMAIL_PASSWORD or EMAIL_PASSWORD:
        print(f"✅ 電子郵件密碼: 已設定")
    else:
        print("❌ 電子郵件密碼: 未設定")
    
    print(f"📬 收件人: {EMAIL_TO}")
    print()
    
    # Send email
    if send_email_with_attachment(filename):
        print()
        print("=" * 60)
        print("✅ 郵件發送完成！")
        print("=" * 60)
        return 0
    else:
        print()
        print("=" * 60)
        print("❌ 郵件發送失敗")
        print("=" * 60)
        return 1

if __name__ == '__main__':
    sys.exit(main())
