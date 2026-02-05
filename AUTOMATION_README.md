# Daily AI News Automation - Quick Reference

## What This Does

This automation system:
1. **Runs daily at 18:30 UTC** via GitHub Actions
2. **Collects latest AI news** from multiple sources
3. **Creates markdown file** in `ai_news/YYYY-MM-DD.md`
4. **Sends email** to oceanicdayi@gmail.com with the digest
5. **Updates README.md** with new entry link
6. **Updates index.html** with new entry link

## Files Created

- `.github/workflows/daily-ai-news.yml` - GitHub Actions workflow
- `scripts/collect_ai_news.py` - Main Python script
- `scripts/README.md` - Detailed script documentation
- `SETUP_GUIDE.md` - Comprehensive setup instructions

## Quick Setup

### 1. Enable Email Notifications (Optional)

Add `EMAIL_PASSWORD` secret to GitHub repository:
- Go to: Settings → Secrets and variables → Actions → New repository secret
- Name: `EMAIL_PASSWORD`
- Value: Your Gmail App Password (see SETUP_GUIDE.md for details)

### 2. Test the Workflow

- Go to Actions tab → Daily AI News Collection
- Click "Run workflow" → Run workflow
- Check for new file in `ai_news/` directory

## Documentation

- **Complete Setup Guide**: See [SETUP_GUIDE.md](SETUP_GUIDE.md)
- **Script Details**: See [scripts/README.md](scripts/README.md)
- **Workflow File**: See [.github/workflows/daily-ai-news.yml](.github/workflows/daily-ai-news.yml)

## Troubleshooting

If the workflow fails:
1. Check Actions tab for error logs
2. Verify secrets are set correctly
3. Try manual trigger first
4. See SETUP_GUIDE.md for detailed troubleshooting

## Schedule

Current schedule: **Daily at 18:30 UTC**

To change, edit the cron expression in `.github/workflows/daily-ai-news.yml`
