# Daily AI News Collection System - Setup Guide

## Overview

This repository includes an automated system that:
- ✅ Collects latest AI news every day at 18:30 UTC
- ✅ Creates a markdown report in `ai_news/YYYY-MM-DD.md`
- ✅ Updates `README.md` with the new entry
- ✅ Updates `index.html` with the new entry
- ✅ Sends email notification to oceanicdayi@gmail.com

## Quick Start

The system is **ready to run** with default settings. However, to enable email notifications, you need to configure the GitHub repository secrets.

## Required Secrets (Optional)

### 1. EMAIL_PASSWORD (for email notifications)

**Purpose**: Allows the system to send daily digest emails

**Setup Steps**:
1. Go to your GitHub repository
2. Click **Settings** → **Secrets and variables** → **Actions**
3. Click **New repository secret**
4. Name: `EMAIL_PASSWORD`
5. Value: Your email app password (see below for Gmail instructions)
6. Click **Add secret**

**For Gmail Users**:
- You need to create an "App Password" (not your regular Gmail password)
- Steps:
  1. Go to https://myaccount.google.com/security
  2. Enable "2-Step Verification" if not already enabled
  3. Go to https://myaccount.google.com/apppasswords
  4. Select "Mail" and "Other" (name it "GitHub Actions")
  5. Copy the 16-character password generated
  6. Use this as the `EMAIL_PASSWORD` secret

### 2. OPENAI_API_KEY (Optional - for enhanced summaries)

**Purpose**: Enables AI-powered news summaries and analysis

**Setup Steps**:
1. Get API key from: https://platform.openai.com/api-keys
2. Add as repository secret named `OPENAI_API_KEY`

## Testing the Workflow

### Manual Trigger

You can test the workflow without waiting for the scheduled time:

1. Go to the **Actions** tab in your GitHub repository
2. Click on **Daily AI News Collection** workflow in the left sidebar
3. Click the **Run workflow** dropdown button
4. Select the branch (usually `main`)
5. Click **Run workflow**
6. Wait for the workflow to complete (~1-2 minutes)

### Check Results

After running:
- A new file should appear: `ai_news/YYYY-MM-DD.md`
- `README.md` should be updated with a link to the new file
- `index.html` should be updated with a link to the new file
- If email is configured, you should receive an email at oceanicdayi@gmail.com

## Schedule

The workflow runs automatically:
- **Every day at 18:30 UTC**
- Cron expression: `30 18 * * *`

To change the schedule:
1. Edit `.github/workflows/daily-ai-news.yml`
2. Modify the cron expression:
   ```yaml
   schedule:
     - cron: '30 18 * * *'  # Format: minute hour day month dayofweek
   ```
3. Commit and push the changes

### Cron Examples
- `30 18 * * *` - Every day at 18:30 UTC
- `0 9 * * *` - Every day at 09:00 UTC
- `0 12 * * 1-5` - Every weekday at 12:00 UTC
- `0 0 * * 0` - Every Sunday at midnight UTC

## How It Works

### Workflow Steps

1. **Checkout** - Gets the latest repository code
2. **Setup Python** - Installs Python 3.11
3. **Install Dependencies** - Installs required packages (requests, beautifulsoup4, openai)
4. **Collect AI News** - Runs the Python script to:
   - Fetch latest AI news from multiple sources
   - Generate markdown report
   - Send email (if configured)
   - Update README.md and index.html
5. **Commit and Push** - Commits changes back to the repository

### News Sources

The script attempts to collect news from:
- TechCrunch AI category
- The Verge AI section
- Fallback: Generates generic AI news topics if external sources fail

### File Structure

```
knowledge/
├── .github/
│   └── workflows/
│       └── daily-ai-news.yml         # GitHub Actions workflow
├── scripts/
│   ├── collect_ai_news.py            # Main Python script
│   └── README.md                     # Detailed script documentation
├── ai_news/
│   ├── 2026-02-03.md                 # Daily reports
│   ├── 2026-02-04.md
│   └── YYYY-MM-DD.md                 # New reports created daily
├── README.md                         # Updated automatically
└── index.html                        # Updated automatically
```

## Troubleshooting

### Workflow Not Running

**Issue**: The scheduled workflow doesn't run automatically

**Solutions**:
- Check that GitHub Actions are enabled: Settings → Actions → General
- Repository must have activity within the past 60 days
- Scheduled workflows may be delayed during high GitHub load
- Try manual trigger to verify the workflow works

### Email Not Sending

**Issue**: Markdown file created but no email received

**Solutions**:
- Verify `EMAIL_PASSWORD` secret is set correctly
- For Gmail, ensure you're using an App Password
- Check spam folder
- Review workflow logs in Actions tab for error messages

### News Collection Fails

**Issue**: Script runs but no news items collected

**Solutions**:
- External news sites may be temporarily unavailable
- Script includes fallback content that will be used
- Check workflow logs for specific error messages
- Internet connectivity issues in GitHub Actions (rare)

### README/index.html Not Updated

**Issue**: New markdown file created but README/index.html not updated

**Solutions**:
- Check workflow logs for update errors
- Verify file permissions
- Ensure README/index.html follow expected format

## Maintenance

### Updating News Sources

To add or modify news sources:
1. Edit `scripts/collect_ai_news.py`
2. Locate the `collect_ai_news()` function
3. Add new source parsing logic
4. Test locally before committing

### Modifying Email Content

To customize email format:
1. Edit `scripts/collect_ai_news.py`
2. Locate the `send_email()` function
3. Modify the message content
4. Test with manual workflow trigger

### Changing Report Format

To modify markdown report format:
1. Edit `scripts/collect_ai_news.py`
2. Locate the `generate_markdown()` function
3. Adjust the template
4. Test and commit

## Security Notes

- **Never commit secrets** to the repository
- Always use GitHub Secrets for sensitive data
- Email passwords should be app-specific, not your main password
- API keys should have minimal required permissions
- Review workflow logs to ensure no sensitive data is exposed

## Support

For issues or questions:
1. Check the workflow logs in the Actions tab
2. Review this documentation
3. Test manually to isolate the problem
4. Check GitHub Actions status: https://www.githubstatus.com/

## License

This automation system is part of the knowledge repository.
