## 🚀 Quick Start: Send OpenClaw Email NOW

Since you've already set the GitHub Secrets, here's the fastest way to send the email:

### ⚡ STEPS TO SEND EMAIL (Using GitHub Actions)

1. **Open your browser and go to:**
   ```
   https://github.com/cwbdayi638/knowledge/actions
   ```

2. **In the left sidebar, click on:**
   ```
   OpenClaw News Collection
   ```

3. **Click the "Run workflow" dropdown button** (top right, blue button)

4. **Select branch: `main` or `copilot/update-readme-and-add-ai-news`**

5. **Click the green "Run workflow" button**

6. **Wait ~30 seconds** and refresh the page to see the workflow running

7. **Click on the running workflow** to see real-time logs

8. **Look for these success messages in the logs:**
   ```
   ✅ 電子郵件發送成功！
   ✅ 已儲存至 openclaw_news_report_2026-02-06.md
   ```

---

## ✉️ What Will Happen

When you trigger the workflow, it will:

1. ✅ Collect latest OpenClaw news
2. ✅ Generate Traditional Chinese markdown report
3. ✅ **Send email to oceanicdayi@gmail.com with markdown attachment**
4. ✅ Update README.md
5. ✅ Commit and push changes

---

## 📧 Email Details

**To:** oceanicdayi@gmail.com  
**Subject:** OpenClaw 最新消息報告 - 2026年02月06日  
**Attachment:** openclaw_news_report_2026-02-06.md  

---

## 🔍 How to Verify Email Was Sent

### In GitHub Actions Log:
Look for this in the "Collect OpenClaw News" step:
```
📧 準備發送電子郵件至 oceanicdayi@gmail.com...
📎 已附加檔案：openclaw_news_report_2026-02-06.md
✅ 電子郵件發送成功！(使用 Gmail SMTP SSL)
```

### In Your Email Inbox:
Check `oceanicdayi@gmail.com` for:
- **Subject:** OpenClaw 最新消息報告 - 2026年02月06日
- **Attachment:** openclaw_news_report_2026-02-06.md

---

## 🆘 If It Doesn't Work

### Check GitHub Secrets are set correctly:

1. Go to: https://github.com/cwbdayi638/knowledge/settings/secrets/actions

2. Verify these secrets exist:
   - ✅ `SENDER_EMAIL_NEW` - Your Gmail address
   - ✅ `CWBDAYI_EMAIL_PASSWORD` - Your Gmail app password

3. If using regular Gmail password instead of app password:
   - ❌ This won't work!
   - ✅ Get app password from: https://myaccount.google.com/apppasswords
   - ✅ Must have 2-step verification enabled

### Check Workflow Logs:

1. Go to Actions tab
2. Click on the failed workflow
3. Look for error messages
4. Common issues:
   - "Authentication failed" → Wrong password or need app password
   - "Connection refused" → Network issue
   - "No such secret" → Secret not set properly

---

## 📱 Alternative: Manual Trigger via GitHub Mobile App

If you prefer using mobile:

1. Open GitHub mobile app
2. Go to your repository
3. Tap "Actions" tab
4. Select "OpenClaw News Collection"
5. Tap "Run workflow"
6. Select branch and tap "Run workflow"

---

## 💻 Alternative: Run Locally (Advanced)

If you want to test locally without GitHub Actions:

```bash
# Set environment variables (use your actual values)
export SENDER_EMAIL_NEW="your-email@gmail.com"
export CWBDAYI_EMAIL_PASSWORD="your-16-char-app-password"
export EMAIL_TO="oceanicdayi@gmail.com"

# Run the standalone script
python3 send_openclaw_email.py
```

---

## ⏰ Automatic Daily Emails

The workflow is scheduled to run automatically every day at:
- **UTC Time:** 05:00
- **Taiwan Time:** 13:00 (1 PM)

So after this manual trigger, it will automatically send daily updates!

---

## ✅ Success Checklist

After running the workflow, verify:

- [ ] Workflow shows green checkmark (completed successfully)
- [ ] Log shows "電子郵件發送成功"
- [ ] Email received at oceanicdayi@gmail.com
- [ ] Email has markdown file attached
- [ ] README.md was updated in repository
- [ ] New commit appears in repository history

---

**Ready? Go trigger the workflow now! 🚀**

Direct link: https://github.com/cwbdayi638/knowledge/actions/workflows/openclaw-news.yml
