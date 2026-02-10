import requests
from bs4 import BeautifulSoup
import os

def run_agent():
    print("Agent: Starting information collection...")
    
    # 1. SCRAPE: Example - Collecting headlines from Hacker News
    url = "https://news.ycombinator.com/"
    res = requests.get(url)
    soup = BeautifulSoup(res.text, "html.parser")
    links = soup.select(".titleline > a")[:5]
    
    # 2. SUMMARIZE: Formatting the findings
    report = "--- DAILY AGENT REPORT ---\n\n"
    for link in links:
        report += f"- {link.text}\n  Link: {link['href']}\n\n"
    
    # 3. OUTPUT: This gets captured by the GitHub Action logs 
    # To actually SEND an email, you would add an API call here (e.g., SendGrid)
    print(report)
    
    with open("report.txt", "w") as f:
        f.write(report)

if __name__ == "__main__":
    run_agent()
