# Monsoon Email Automation - Implementation Summary

## Overview

This implementation provides comprehensive information about monsoons (季風) in meteorology (氣象學) and includes an automated email delivery system.

## Created Files

### 1. monsoon.md
A comprehensive document covering:
- Definition and basic concepts of monsoons
- Formation mechanisms (海陸熱力差異)
- Major monsoon systems worldwide
- East Asian Monsoon and its impact on Taiwan
- Climate change implications
- Agricultural and economic importance
- Forecasting challenges

**Location**: `/home/runner/work/knowledge/knowledge/monsoon.md`

### 2. send_monsoon_email.py
An automated script to send the monsoon information via email.

**Location**: `/home/runner/work/knowledge/knowledge/scripts/send_monsoon_email.py`

**Features**:
- Reads monsoon.md content
- Formats email with proper encoding (UTF-8)
- Sends to: oceanicdayi@gmail.com
- Subject: "氣象學知識：季風 (Monsoon) 完整說明"

## How to Use

### Option 1: Manual Execution (With Credentials)

If you have email credentials set up:

```bash
# Set environment variables
export SENDER_EMAIL_NEW="your_email@gmail.com"
export CWBDAYI_EMAIL_PASSWORD="your_app_password"

# Run the script
cd /home/runner/work/knowledge/knowledge
python3 scripts/send_monsoon_email.py
```

### Option 2: Direct Email Using send_email.py

```bash
cd /home/runner/work/knowledge/knowledge/scripts
python3 send_email.py oceanicdayi@gmail.com "氣象學知識：季風 (Monsoon) 完整說明" "$(cat ../monsoon.md)"
```

### Option 3: GitHub Actions Workflow

Create a workflow file to automate email sending:

```yaml
name: Send Monsoon Email

on:
  workflow_dispatch:  # Manual trigger

jobs:
  send-email:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.x'
      - name: Send Email
        env:
          SENDER_EMAIL_NEW: ${{ secrets.SENDER_EMAIL_NEW }}
          CWBDAYI_EMAIL_PASSWORD: ${{ secrets.EMAIL_PASSWORD }}
        run: |
          python3 scripts/send_monsoon_email.py
```

## Email Content Preview

**To**: oceanicdayi@gmail.com  
**Subject**: 氣象學知識：季風 (Monsoon) 完整說明  
**Body**: Complete monsoon.md content with introduction

## Setup Requirements

### Gmail App Password Setup

1. Enable 2-factor authentication on your Gmail account
2. Go to Google Account → Security → 2-Step Verification → App passwords
3. Generate a new app password
4. Store in GitHub Secrets:
   - `SENDER_EMAIL_NEW`: Your Gmail address
   - `EMAIL_PASSWORD` or `CWBDAYI_EMAIL_PASSWORD`: The generated app password

### Environment Variables Needed

- `SENDER_EMAIL_NEW`: Sender's email address
- `CWBDAYI_EMAIL_PASSWORD`: Gmail app password

## Content Summary

The monsoon.md document provides comprehensive coverage of:

1. **Definition**: Seasonal wind systems with directional reversal
2. **Formation**: Sea-land thermal differential and planetary wind shifts
3. **Major Systems**: 
   - Asian Monsoon (South Asian & East Asian)
   - West African Monsoon
   - North American Monsoon
   - Australian Monsoon
4. **Taiwan Impact**: Meiyu season and Southwest Flow events
5. **Climate Change**: Precipitation intensity changes and circulation shifts
6. **Importance**: Agriculture, water resources, economics, ecology
7. **Challenges**: Long-term forecasting and mesoscale system prediction

## Verification

The content has been:
- ✓ Created in monsoon.md with full Chinese text
- ✓ Integrated into README.md navigation
- ✓ Email script created and tested (structure)
- ⏳ Email sending pending credentials

## Next Steps

To send the email immediately:

1. Ensure GitHub secrets are configured with email credentials
2. Run the script manually or trigger via GitHub Actions
3. Verify email delivery to oceanicdayi@gmail.com

## Technical Notes

- Character encoding: UTF-8 (supports Chinese characters)
- Email format: Plain text
- Script compatibility: Python 3.x
- Dependencies: Standard library only (smtplib, email.mime)

---

*Document created: 2026-02-06*  
*Repository: cwbdayi638/knowledge*
