#!/usr/bin/env python3
"""
Earthquake Information Collection Script
Collects earthquake data from USGS, generates markdown report, and sends email
Runs every 20 minutes via GitHub Actions
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

# Configuration
EMAIL_TO = os.environ.get('EMAIL_TO', 'oceanicdayi@gmail.com')
EMAIL_PASSWORD = os.environ.get('EMAIL_PASSWORD', '')
TIMESTAMP = datetime.now().strftime('%Y-%m-%d_%H-%M')
DATE_DISPLAY = datetime.now().strftime('%B %d, %Y %H:%M UTC')

# USGS Earthquake API endpoint
# Get earthquakes from the past hour with magnitude 2.5+
USGS_API_URL = 'https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_hour.geojson'

def collect_earthquake_data():
    """
    Collect earthquake data from USGS API
    """
    print("🌍 Collecting earthquake data from USGS...")
    
    try:
        response = requests.get(USGS_API_URL, timeout=15)
        if response.status_code == 200:
            data = response.json()
            earthquakes = data.get('features', [])
            print(f"✅ Collected {len(earthquakes)} earthquake records")
            return earthquakes
        else:
            print(f"⚠️  USGS API returned status code: {response.status_code}")
            return []
    except Exception as e:
        print(f"❌ Error fetching earthquake data: {e}")
        return []

def generate_markdown(earthquakes):
    """
    Generate markdown content for the earthquake report
    """
    print("📝 Generating markdown report...")
    
    content = f"""# Earthquake Information Report - {TIMESTAMP}

**Date & Time**: {DATE_DISPLAY}  
**Source**: USGS Earthquake Hazards Program  
**Data**: Magnitude 2.5+ earthquakes in the past hour

---

"""
    
    if not earthquakes:
        content += """## No Significant Earthquakes Detected

No earthquakes with magnitude 2.5 or greater were detected in the past hour.

"""
    else:
        content += f"## Summary\n\n"
        content += f"Total earthquakes detected: **{len(earthquakes)}**\n\n"
        
        # Calculate statistics
        magnitudes = [eq['properties']['mag'] for eq in earthquakes if eq['properties']['mag']]
        if magnitudes:
            max_mag = max(magnitudes)
            avg_mag = sum(magnitudes) / len(magnitudes)
            content += f"- Largest magnitude: **{max_mag:.1f}**\n"
            content += f"- Average magnitude: **{avg_mag:.2f}**\n\n"
        
        content += "---\n\n## Earthquake Details\n\n"
        
        # Sort by magnitude (descending)
        sorted_earthquakes = sorted(
            earthquakes, 
            key=lambda x: x['properties']['mag'] if x['properties']['mag'] else 0, 
            reverse=True
        )
        
        for i, eq in enumerate(sorted_earthquakes, 1):
            props = eq['properties']
            coords = eq['geometry']['coordinates']
            
            magnitude = props.get('mag', 'N/A')
            place = props.get('place', 'Unknown location')
            time_ms = props.get('time') if props.get('time') is not None else 0
            time_str = datetime.fromtimestamp(time_ms / 1000).strftime('%Y-%m-%d %H:%M:%S UTC')
            depth = coords[2] if len(coords) > 2 else 'N/A'
            longitude = coords[0] if len(coords) > 0 else 'N/A'
            latitude = coords[1] if len(coords) > 1 else 'N/A'
            
            # Get additional details
            alert_level = props.get('alert', 'None')
            tsunami = props.get('tsunami')
            if tsunami is None:
                tsunami = 0
            felt_reports = props.get('felt')
            if felt_reports is None:
                felt_reports = 0
            url = props.get('url', '#')
            
            content += f"### {i}. Magnitude {magnitude} - {place}\n\n"
            content += f"- **Time**: {time_str}\n"
            content += f"- **Location**: {latitude}°, {longitude}°\n"
            content += f"- **Depth**: {depth} km\n"
            
            if alert_level and alert_level != 'None':
                content += f"- **Alert Level**: {alert_level.upper()}\n"
            
            if tsunami == 1:
                content += f"- **Tsunami Warning**: ⚠️ YES\n"
            
            if felt_reports is not None and felt_reports > 0:
                content += f"- **Felt Reports**: {felt_reports} people\n"
            
            content += f"- **Details**: [USGS Event Page]({url})\n"
            content += "\n"
    
    content += """---

## About This Report

This automated report collects earthquake data from the USGS Earthquake Hazards Program every 20 minutes. The report includes:

- All earthquakes with magnitude 2.5 or greater from the past hour
- Location, depth, and timing information
- Alert levels and tsunami warnings when applicable
- Links to detailed USGS event pages

**Data Source**: [USGS Earthquake Hazards Program](https://earthquake.usgs.gov/)

---

*Generated automatically by Earthquake Information Collection System*
"""
    
    return content

def save_markdown(content):
    """
    Save the markdown content to a file
    """
    print(f"💾 Saving markdown to earthquake_data/{TIMESTAMP}.md...")
    
    # Ensure earthquake_data directory exists
    os.makedirs('earthquake_data', exist_ok=True)
    
    filename = f'earthquake_data/{TIMESTAMP}.md'
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"✅ Saved to {filename}")
    return filename

def send_email(content):
    """
    Send the earthquake report via email using Gmail SMTP
    """
    print(f"📧 Preparing to send email to {EMAIL_TO}...")
    
    if not EMAIL_PASSWORD:
        print("⚠️  Email password not configured, skipping email send")
        print("ℹ️  To enable email: Set EMAIL_PASSWORD secret in GitHub repository")
        return False
    
    try:
        # Create message
        message = MIMEMultipart("alternative")
        message["Subject"] = f"Earthquake Information Report - {DATE_DISPLAY}"
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

def main():
    """
    Main execution function
    """
    print("=" * 60)
    print("🌍 Earthquake Information Collection System")
    print("=" * 60)
    print()
    
    try:
        # Step 1: Collect earthquake data
        earthquakes = collect_earthquake_data()
        
        # Step 2: Generate markdown
        markdown_content = generate_markdown(earthquakes)
        
        # Step 3: Save markdown file
        filename = save_markdown(markdown_content)
        
        # Step 4: Send email
        send_email(markdown_content)
        
        print()
        print("=" * 60)
        print("✅ Earthquake Information Collection completed successfully!")
        print("=" * 60)
        
        return 0
        
    except Exception as e:
        print(f"❌ Fatal error: {e}")
        import traceback
        traceback.print_exc()
        return 1

if __name__ == '__main__':
    sys.exit(main())
