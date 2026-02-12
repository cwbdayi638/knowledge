import requests
from bs4 import BeautifulSoup
import os

def run_agent():
    print("Agent: Starting information collection...")
    
    # 1. SCRAPE: Example - Collecting headlines from Hacker News
    url = "https://news.ycombinator.com/"
    try:
        res = requests.get(url, timeout=10)
        res.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data from Hacker News: {e}")
        return
    
    soup = BeautifulSoup(res.text, "html.parser")
    links = soup.select(".titleline > a")[:5]
    
    if not links:
        print("Warning: No headlines found. The website structure may have changed.")
        return
    
    # 2. SUMMARIZE: Formatting the findings
    report = "--- DAILY AGENT REPORT ---\n\n"
    for link in links:
        href = link.get('href', 'No URL')
        report += f"- {link.text}\n  Link: {href}\n\n"
    
    # 3. OUTPUT: This gets captured by the GitHub Action logs 
    # To actually SEND an email, you would add an API call here (e.g., SendGrid)
    print(report)
    
    try:
        with open("report.txt", "w", encoding="utf-8") as f:
            f.write(report)
    except IOError as e:
        print(f"Error writing report to file: {e}")

if __name__ == "__main__":
    run_agent()
