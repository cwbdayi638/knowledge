# Scripts Directory

This directory contains automated scripts for data collection and monitoring.

## Continuous Integration

### Test Workflow (`test.yml`)

A GitHub Actions workflow automatically runs all test scripts on every push and pull request to ensure code quality.

**Features:**
- ✅ Runs automatically on push/PR to main branch
- 🧪 Executes all unit tests (earthquake, waveforms, email)
- 🔄 Manual trigger available via workflow_dispatch
- 📊 Test results visible in GitHub Actions tab

**Testing locally:**
```bash
# Install all test dependencies
pip install requests beautifulsoup4 obspy matplotlib numpy

# Run all tests
cd scripts
python3 test_earthquake_collection.py
python3 test_fetch_seismic_waveforms.py
python3 test_monsoon_email.py
```

**Workflow location:** `.github/workflows/test.yml`

---

## Available Scripts

### 1. Seismic Waveform Fetching (`fetch_seismic_waveforms.py`)

Automatically fetches and plots seismic waveforms from FDSN web services.

**Features:**
- 🌊 Fetches 10 minutes of seismic data from multiple FDSN providers
- 📊 Generates high-quality PNG plots of three-component waveforms
- 🔄 Automatic retry logic with exponential backoff
- ✅ Data validation and quality checks
- 🎯 Graceful fallback to example data when services unavailable
- ⏱️ Runs every 30 minutes via GitHub Actions

**Testing:**
```bash
# Run unit tests
python3 scripts/test_fetch_seismic_waveforms.py

# Manual execution
python3 scripts/fetch_seismic_waveforms.py
```

See [TESTING.md](TESTING.md) for comprehensive testing documentation.

**Dependencies:**
- obspy
- matplotlib
- numpy

---

### 2. Daily AI News Collection (`collect_ai_news.py`)

Automatically collects the latest AI news every day at 18:30 UTC, generates a markdown report, sends an email notification, and updates the repository's README.md and index.html files.

## Features

- 🔄 **Automated Collection**: Runs daily at 18:30 UTC via GitHub Actions
- 📰 **News Aggregation**: Collects latest AI news from multiple sources (TechCrunch, The Verge, etc.)
- 📧 **Email Notifications**: Sends digest to oceanicdayi@gmail.com
- 📝 **Markdown Reports**: Creates dated markdown files in `ai_news/` directory
- 🔄 **Auto Updates**: Updates README.md and index.html with new entries

## Setup Instructions

### Required GitHub Secrets

To enable all features, configure the following secrets in your GitHub repository:

1. **OPENAI_API_KEY** (Optional)
   - Used for enhanced news summaries with AI
   - Get from: https://platform.openai.com/api-keys
   - Set in: Repository Settings → Secrets and variables → Actions → New repository secret

2. **EMAIL_PASSWORD** (Optional)
   - Used to send email notifications
   - For Gmail: Use an App Password (not your regular password)
   - Generate at: https://myaccount.google.com/apppasswords
   - Set in: Repository Settings → Secrets and variables → Actions → New repository secret

### How to Set Secrets

1. Go to your repository on GitHub
2. Click **Settings** → **Secrets and variables** → **Actions**
3. Click **New repository secret**
4. Name: `OPENAI_API_KEY` or `EMAIL_PASSWORD`
5. Value: Paste your API key or password
6. Click **Add secret**

### Manual Trigger

To run the workflow manually:

1. Go to **Actions** tab in your repository
2. Click on **Daily AI News Collection** workflow
3. Click **Run workflow** button
4. Select branch and click **Run workflow**

## Files Structure

```
.github/workflows/
  └── daily-ai-news.yml          # GitHub Actions workflow
scripts/
  └── collect_ai_news.py         # Python script for news collection
  └── README.md                  # This file
ai_news/
  └── YYYY-MM-DD.md              # Daily news reports
```

## Workflow Schedule

The workflow runs:
- **Daily at 18:30 UTC** (automatically via cron schedule)
- **Manual trigger** available for testing

To change the schedule, edit the cron expression in `.github/workflows/daily-ai-news.yml`:
```yaml
schedule:
  - cron: '30 18 * * *'  # Minute Hour Day Month DayOfWeek
```

## Dependencies

Python packages installed automatically:
- `requests` - HTTP requests
- `beautifulsoup4` - HTML parsing
- `openai` - OpenAI API integration (optional)

## Troubleshooting

### Email not sending
- Verify `EMAIL_PASSWORD` secret is set correctly
- For Gmail, ensure you're using an App Password, not your account password
- Check the Actions log for specific error messages

### News collection fails
- The script has fallback content if external sources are unavailable
- Check if news source websites have changed their HTML structure

### Workflow not running
- Verify the cron schedule is correct
- Check that GitHub Actions are enabled for your repository
- Repository must have activity in the past 60 days for scheduled workflows

## Testing Locally

### AI News Collection
To test the AI news script locally:

```bash
# Install dependencies
pip install requests beautifulsoup4 openai

# Set environment variables
export EMAIL_TO="your-email@example.com"
export EMAIL_PASSWORD="your-app-password"
export OPENAI_API_KEY="your-api-key"  # Optional

# Run the script
python scripts/collect_ai_news.py
```

### Seismic Waveforms
To test the waveform script locally:

```bash
# Install dependencies
pip install obspy matplotlib numpy

# Run unit tests
python3 scripts/test_fetch_seismic_waveforms.py

# Run the script
python3 scripts/fetch_seismic_waveforms.py
```

For detailed testing documentation, see [TESTING.md](TESTING.md).

## Test Coverage

Current test suites:

| Test Script | Tests | Coverage |
|-------------|-------|----------|
| `test_earthquake_collection.py` | 3 tests | Earthquake markdown generation, None value handling |
| `test_fetch_seismic_waveforms.py` | 18 tests | Waveform validation, FDSN connection, plotting, main function |
| `test_monsoon_email.py` | 1 test | Email preview generation |

All tests run automatically via GitHub Actions on every push and pull request.

## License

This automation system is part of the knowledge repository and follows the same license.
