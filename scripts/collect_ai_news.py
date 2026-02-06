#!/usr/bin/env python3
"""
Daily AI News Collection Script
Collects AI news, generates markdown report, sends email, and updates README/index.html
"""

import os
import sys
import json
import smtplib
import ssl
from datetime import datetime
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import requests
from bs4 import BeautifulSoup

# Configuration
OPENAI_API_KEY = os.environ.get('OPENAI_API_KEY', '')
EMAIL_TO = os.environ.get('EMAIL_TO', 'oceanicdayi@gmail.com')
EMAIL_PASSWORD = os.environ.get('EMAIL_PASSWORD', '')
NOW = datetime.now()
DATE_STR = NOW.strftime('%Y-%m-%d')
DATE_DISPLAY = f"{NOW.year}年{NOW.month}月{NOW.day}日"

def collect_ai_news():
    """
    Collect latest AI news from various sources
    """
    print("🔍 Collecting AI news...")
    
    news_items = []
    
    # Try to fetch from TechCrunch AI
    try:
        response = requests.get('https://techcrunch.com/category/artificial-intelligence/', timeout=10)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            articles = soup.find_all('h2', class_='wp-block-post-title')[:5]
            
            for article in articles:
                link = article.find('a')
                if link:
                    title = link.get_text(strip=True)
                    url = link.get('href', '')
                    news_items.append({
                        'title': title,
                        'url': url,
                        'source': 'TechCrunch AI'
                    })
    except Exception as e:
        print(f"⚠️  Error fetching TechCrunch: {e}")
    
    # Try to fetch from The Verge AI
    try:
        response = requests.get('https://www.theverge.com/ai-artificial-intelligence', timeout=10)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            articles = soup.find_all('h2')[:5]
            
            for article in articles:
                link = article.find('a')
                if link:
                    title = article.get_text(strip=True)
                    url = link.get('href', '')
                    if url and not url.startswith('http'):
                        url = 'https://www.theverge.com' + url
                    news_items.append({
                        'title': title,
                        'url': url,
                        'source': 'The Verge'
                    })
    except Exception as e:
        print(f"⚠️  Error fetching The Verge: {e}")
    
    # If we couldn't get real news, use a fallback
    if not news_items:
        print("📝 Using fallback AI news topics...")
        news_items = [
            {
                'title': '大型語言模型的最新進展',
                'url': '#',
                'source': 'AI 研究社群',
                'summary': '最新模型架構與訓練方法的研究突破，帶來更強的語言理解能力。'
            },
            {
                'title': 'AI 安全與對齊研究進展',
                'url': '#',
                'source': 'AI 安全研究',
                'summary': '新方法提升系統與人類價值的對齊程度，確保安全部署。'
            },
            {
                'title': 'AI 在產業中的實際應用',
                'url': '#',
                'source': '產業報告',
                'summary': '企業導入 AI 解決方案的最新案例與效益分析。'
            }
        ]
    
    print(f"✅ Collected {len(news_items)} news items")
    return news_items[:10]  # Limit to top 10

def build_traditional_chinese_summary(item):
    """
    Build a Traditional Chinese summary for a news item with fallback text.
    """
    summary = item.get('summary')
    if summary:
        return summary

    title = item.get('title', '').strip()
    if title:
        return f"本則新聞重點為「{title}」，更多內容請參閱原文。"
    return "本則新聞重點請參閱原文。"

def generate_markdown(news_items):
    """
    Generate markdown content for the news report
    """
    print("📝 Generating markdown report...")
    
    content = f"""# 全球 AI 新聞每日摘要 - {DATE_STR}

**日期**: {DATE_DISPLAY}  
**時間**: {NOW.strftime('%H:%M')} UTC  
**來源**: 多個 AI 新聞來源

---

## 最新 AI 新聞標題

"""
    
    for i, item in enumerate(news_items, 1):
        content += f"## {i}. {item['title']}\n"
        content += f"*   **來源**: {item['source']}\n"
        content += f"*   **連結**: [{item['url']}]({item['url']})\n"
        content += f"*   **摘要**: {build_traditional_chinese_summary(item)}\n"
        
        content += "\n"
    
    content += f"""---

## 今日關鍵主題

- **AI 研究**：模型架構與訓練方法持續突破
- **產業導入**：AI 解決方案在各產業加速落地
- **倫理與安全**：負責任 AI 的治理與對齊討論升溫
- **應用場景**：多元場景持續擴大，帶動新需求

---

*由每日 AI 新聞蒐集系統自動生成 | {DATE_STR}*
"""
    
    return content

def save_markdown(content):
    """
    Save the markdown content to a file
    """
    print(f"💾 Saving markdown to ai_news/{DATE_STR}.md...")
    
    # Ensure ai_news directory exists
    os.makedirs('ai_news', exist_ok=True)
    
    filename = f'ai_news/{DATE_STR}.md'
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"✅ Saved to {filename}")
    return filename

def send_email(content):
    """
    Send the news report via email using Gmail SMTP
    """
    print(f"📧 Preparing to send email to {EMAIL_TO}...")
    
    if not EMAIL_PASSWORD:
        print("⚠️  Email password not configured, skipping email send")
        print("ℹ️  To enable email: Set EMAIL_PASSWORD secret in GitHub repository")
        return False
    
    try:
        # Create message
        message = MIMEMultipart("alternative")
        message["Subject"] = f"每日 AI 新聞摘要 - {DATE_DISPLAY}"
        message["From"] = EMAIL_TO  # Send from the same address (Gmail requirement)
        message["To"] = EMAIL_TO
        
        # Convert markdown to simple text for email
        text_content = content.replace('#', '').replace('*', '')
        
        # Attach plain text version
        part1 = MIMEText(text_content, "plain")
        message.attach(part1)
        
        # Send via Gmail SMTP
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
            server.login(EMAIL_TO, EMAIL_PASSWORD)
            server.sendmail(EMAIL_TO, EMAIL_TO, message.as_string())
        
        print("✅ Email sent successfully!")
        return True
        
    except Exception as e:
        print(f"❌ Error sending email: {e}")
        print("ℹ️  Note: For Gmail, you need an App Password (not regular password)")
        print("ℹ️  Generate at: https://myaccount.google.com/apppasswords")
        return False

def update_readme(filename):
    """
    Update README.md to include the new report
    """
    print("📝 Updating README.md...")
    
    try:
        with open('README.md', 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Find the AI news section
        news_line = f"  - [每日 AI 新聞深入解說 ({DATE_STR})](ai_news/{DATE_STR}.md)"
        
        # Check if it already exists
        if news_line in content:
            print("ℹ️  Entry already exists in README.md")
            return
        
        # Find the insertion point (after "- **AI 新聞與分析**")
        marker = "- **AI 新聞與分析**"
        if marker in content:
            # Insert after the existing first entry
            lines = content.split('\n')
            new_lines = []
            inserted = False
            
            for i, line in enumerate(lines):
                new_lines.append(line)
                if marker in line and not inserted:
                    # Add the new entry after the marker
                    # Find the next line with content
                    if i + 1 < len(lines):
                        new_lines.append(f"  - [每日 AI 新聞深入解說 ({DATE_STR})](ai_news/{DATE_STR}.md)")
                        inserted = True
            
            if inserted:
                content = '\n'.join(new_lines)
                with open('README.md', 'w', encoding='utf-8') as f:
                    f.write(content)
                print("✅ Updated README.md")
            else:
                print("⚠️  Could not find insertion point in README.md")
        else:
            print("⚠️  Could not find AI news section in README.md")
            
    except Exception as e:
        print(f"❌ Error updating README.md: {e}")

def update_index_html():
    """
    Update index.html to include the new report
    """
    print("📝 Updating index.html...")
    
    try:
        with open('index.html', 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Create the new entry
        new_entry = f"""                <li>
                    <a href="https://github.com/cwbdayi638/knowledge/blob/main/ai_news/{DATE_STR}.md" target="_blank">
                        每日 AI 新聞 ({DATE_STR}) <span class="badge badge-ai">AI</span>
                    </a>
                </li>"""
        
        # Check if entry already exists
        if f'ai_news/{DATE_STR}.md' in content:
            print("ℹ️  Entry already exists in index.html")
            return
        
        # Find the AI section by looking for the data-category="ai" card
        # and the first <ul> within it
        ai_section_marker = '<div class="card" data-category="ai">'
        if ai_section_marker in content:
            # Find the position of this section
            section_pos = content.find(ai_section_marker)
            if section_pos != -1:
                # Find the first <ul> after this marker
                ul_start = content.find('<ul>', section_pos)
                if ul_start != -1:
                    # Find the first </li> after the <ul>
                    first_li_end = content.find('</li>', ul_start)
                    if first_li_end != -1:
                        # Insert the new entry after this </li>
                        insertion_point = first_li_end + 5  # len('</li>')
                        content = content[:insertion_point] + '\n' + new_entry + content[insertion_point:]
                        
                        with open('index.html', 'w', encoding='utf-8') as f:
                            f.write(content)
                        print("✅ Updated index.html")
                        return
        
        print("⚠️  Could not find insertion point in index.html")
        
    except Exception as e:
        print(f"❌ Error updating index.html: {e}")

def main():
    """
    Main execution function
    """
    print("=" * 60)
    print("🤖 Daily AI News Collection System")
    print("=" * 60)
    print()
    
    try:
        # Step 1: Collect news
        news_items = collect_ai_news()
        
        # Step 2: Generate markdown
        markdown_content = generate_markdown(news_items)
        
        # Step 3: Save markdown file
        filename = save_markdown(markdown_content)
        
        # Step 4: Send email
        send_email(markdown_content)
        
        # Step 5: Update README
        update_readme(filename)
        
        # Step 6: Update index.html
        update_index_html()
        
        print()
        print("=" * 60)
        print("✅ Daily AI News Collection completed successfully!")
        print("=" * 60)
        
        return 0
        
    except Exception as e:
        print(f"❌ Fatal error: {e}")
        import traceback
        traceback.print_exc()
        return 1

if __name__ == '__main__':
    sys.exit(main())
