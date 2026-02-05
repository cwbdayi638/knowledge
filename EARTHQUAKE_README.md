# Earthquake Information Collection System

## Overview

This automation system collects earthquake information from the USGS (United States Geological Survey) Earthquake Hazards Program every 20 minutes and creates detailed markdown reports.

## What This Does

The system:
1. **Runs every 20 minutes** via GitHub Actions
2. **Collects earthquake data** from USGS API (magnitude 2.5+ from past hour)
3. **Generates markdown report** in `earthquake_data/` directory
4. **Sends email notification** to oceanicdayi@gmail.com
5. **Commits and pushes** the new report to the repository

## Features

- **Real-time monitoring**: Collects data every 20 minutes
- **Comprehensive reporting**: Includes magnitude, location, depth, time, and alert levels
- **Tsunami warnings**: Highlights any tsunami warnings
- **Email notifications**: Sends reports directly to configured email
- **Automated commits**: Updates repository automatically

## Files Created

- `.github/workflows/earthquake-info.yml` - GitHub Actions workflow
- `scripts/collect_earthquake_info.py` - Main Python collection script
- `earthquake_data/` - Directory containing generated markdown reports

## Data Source

All earthquake data is sourced from:
- **USGS Earthquake Hazards Program**
- API: https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_hour.geojson
- Includes all earthquakes magnitude 2.5+ from the past hour

## Setup

### Email Notifications (Optional)

To enable email notifications:

1. Go to your GitHub repository settings
2. Navigate to: Settings → Secrets and variables → Actions
3. Add a new secret:
   - **Name**: `EMAIL_PASSWORD`
   - **Value**: Your Gmail App Password

#### How to Get Gmail App Password

1. Visit: https://myaccount.google.com/apppasswords
2. Create a new app password for "Mail"
3. Use this password as the `EMAIL_PASSWORD` secret

**Note**: You must have 2-factor authentication enabled on your Gmail account to create app passwords.

## Testing

To test the workflow manually:

1. Go to the **Actions** tab in GitHub
2. Select **Earthquake Information Collection**
3. Click **Run workflow** → **Run workflow**
4. Check the `earthquake_data/` directory for new files

## Schedule

**Current schedule**: Every 20 minutes (24/7)

The cron expression used: `*/20 * * * *`

To change the schedule, edit the cron expression in `.github/workflows/earthquake-info.yml`

### Common Cron Patterns

- `*/20 * * * *` - Every 20 minutes
- `*/30 * * * *` - Every 30 minutes
- `0 * * * *` - Every hour
- `0 */2 * * *` - Every 2 hours

## Report Format

Each markdown report includes:

### Summary Section
- Total number of earthquakes detected
- Largest magnitude
- Average magnitude

### Earthquake Details
For each earthquake:
- Magnitude
- Location (place name)
- Coordinates (latitude, longitude)
- Depth
- Time (UTC)
- Alert level (if applicable)
- Tsunami warning (if applicable)
- Number of felt reports
- Link to detailed USGS event page

## Troubleshooting

### Workflow Fails

1. Check the **Actions** tab for error logs
2. Verify the USGS API is accessible
3. Check if `EMAIL_PASSWORD` secret is set (if email is failing)

### No Email Received

1. Check spam/junk folder
2. Verify `EMAIL_PASSWORD` secret is configured correctly
3. Ensure you're using a Gmail App Password (not regular password)
4. Check the workflow logs for email errors

### No Data Collected

If no earthquakes are reported:
- This is normal! The system only reports earthquakes magnitude 2.5+ from the past hour
- Check the USGS website to verify current earthquake activity
- The report will still be generated with a "No significant earthquakes" message

## Maintenance

The system is fully automated and requires no regular maintenance. However:

- Monitor the Actions tab occasionally for any failures
- Update Python dependencies if security vulnerabilities are reported
- Adjust the schedule if needed based on your requirements

## Privacy & Security

- Email credentials are stored securely in GitHub Secrets
- No personal data is collected or stored
- All earthquake data is public information from USGS

## Support

For issues or questions:
- Check the GitHub Actions logs for detailed error messages
- Review this documentation
- Ensure all secrets are configured correctly
