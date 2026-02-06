# Monsoon Email Sending Instructions

## ✅ COMPLETED IMPLEMENTATION

All components have been successfully created and are ready to use:

1. **✓ monsoon.md** - Comprehensive 113-line document (275 words) about monsoon in 氣象學
2. **✓ scripts/send_monsoon_email.py** - Automated email sending script
3. **✓ scripts/test_monsoon_email.py** - Email preview/testing script
4. **✓ README.md** - Updated with monsoon document link
5. **✓ MONSOON_EMAIL_IMPLEMENTATION.md** - Complete implementation documentation

## 📧 TO SEND EMAIL TO oceanicdayi@gmail.com

### Option A: Using Repository Secrets (Recommended)

If you have GitHub repository access, set these secrets:
- `SENDER_EMAIL_NEW`: Your Gmail address
- `CWBDAYI_EMAIL_PASSWORD`: Your Gmail app password

Then run:
```bash
cd /home/runner/work/knowledge/knowledge
python3 scripts/send_monsoon_email.py
```

### Option B: Direct Command Line

```bash
cd /home/runner/work/knowledge/knowledge
export SENDER_EMAIL_NEW="your_email@gmail.com"
export CWBDAYI_EMAIL_PASSWORD="your_app_password"
python3 scripts/send_monsoon_email.py
```

### Option C: Using Existing send_email.py

```bash
cd /home/runner/work/knowledge/knowledge/scripts
export SENDER_EMAIL_NEW="your_email@gmail.com"
export CWBDAYI_EMAIL_PASSWORD="your_app_password"
python3 send_email.py \
  oceanicdayi@gmail.com \
  "氣象學知識：季風 (Monsoon) 完整說明" \
  "$(cat ../monsoon.md)"
```

### Option D: GitHub Actions (Automated)

Create this workflow file at `.github/workflows/send-monsoon-email.yml`:

```yaml
name: Send Monsoon Email

on:
  workflow_dispatch:

jobs:
  send-email:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.x'
      - name: Send Monsoon Email
        env:
          SENDER_EMAIL_NEW: ${{ secrets.SENDER_EMAIL_NEW }}
          CWBDAYI_EMAIL_PASSWORD: ${{ secrets.EMAIL_PASSWORD }}
        run: |
          cd ${{ github.workspace }}
          python3 scripts/send_monsoon_email.py
```

Then trigger from GitHub UI: Actions → Send Monsoon Email → Run workflow

## 📋 WHAT'S IN THE EMAIL

**To:** oceanicdayi@gmail.com  
**Subject:** 氣象學知識：季風 (Monsoon) 完整說明  
**Content:** Full monsoon.md (2,375 characters) including:

### Topics Covered:
1. 季風的定義與基本概念
   - 定義：大規模季節性風系統
   - 特徵：風向反轉、降水季節變化
   
2. 季風的形成機制
   - 海陸熱力差異
   - 行星風系的季節性移動
   
3. 世界主要季風系統
   - 亞洲季風（南亞、東亞）
   - 西非季風
   - 北美季風
   - 澳洲季風
   
4. 東亞夏季風與台灣
   - 梅雨季
   - 西南氣流事件
   
5. 季風與氣候變遷
   - 降水強度增加
   - 季風期改變
   - 環流減弱
   
6. 季風的重要性
   - 農業與水資源
   - 經濟與社會影響
   - 生態系統
   
7. 季風預報的挑戰
   - 長期預報不確定性
   - 中尺度系統預測
   - 海氣交互作用

## 🔐 HOW TO GET GMAIL APP PASSWORD

1. Enable 2-Step Verification on your Gmail account
2. Go to: https://myaccount.google.com/apppasswords
3. Select "Mail" and your device
4. Copy the 16-character password
5. Use this as `CWBDAYI_EMAIL_PASSWORD`

## ✅ VERIFICATION CHECKLIST

- [x] monsoon.md created with complete content (113 lines, 4.8KB)
- [x] Email sending script created and executable
- [x] Test script created for preview
- [x] README.md updated with link
- [x] Implementation documentation created
- [x] All files committed to repository
- [ ] Email credentials configured (requires user action)
- [ ] Email sent to oceanicdayi@gmail.com (requires credentials)

## 🚀 READY TO SEND

Everything is prepared. Simply:
1. Set the email credentials (see options above)
2. Run the script
3. Email will be automatically sent to oceanicdayi@gmail.com

---

**Note:** The email content is ready and the infrastructure is in place. The only requirement is to provide valid email credentials to complete the sending process.
