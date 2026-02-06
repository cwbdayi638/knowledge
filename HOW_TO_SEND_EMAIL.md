# 如何發送 OpenClaw 新聞報告郵件

## 方法一：使用 GitHub Actions（推薦）

由於您已經設定了 GitHub Secrets，最簡單的方法是手動觸發 GitHub Actions 工作流程：

### 步驟：

1. **前往 GitHub 儲存庫頁面**
   - 網址：https://github.com/cwbdayi638/knowledge

2. **點擊 "Actions" 標籤**
   - 在儲存庫頂部的導航欄中

3. **選擇 "OpenClaw News Collection" 工作流程**
   - 在左側工作流程列表中

4. **點擊 "Run workflow" 按鈕**
   - 在右上角的藍色按鈕
   - 選擇分支（通常是 `main`）
   - 點擊綠色的 "Run workflow" 按鈕

5. **等待執行完成**
   - 工作流程會自動：
     - 收集最新 OpenClaw 新聞
     - 生成繁體中文 Markdown 報告
     - 發送郵件（含附件）至 oceanicdayi@gmail.com
     - 更新 README.md
     - 提交並推送變更

6. **檢查執行結果**
   - 點擊工作流程執行記錄查看日誌
   - 確認郵件發送成功的訊息

### 優點：
- ✅ 使用您設定的 GitHub Secrets（安全）
- ✅ 完全自動化流程
- ✅ 包含所有步驟（收集、生成、發送、提交）
- ✅ 有完整的執行日誌可供查看

---

## 方法二：使用獨立腳本（本地執行）

如果您想在本地環境測試郵件發送功能：

### 前提條件：
需要設定以下環境變數：

```bash
export SENDER_EMAIL_NEW="your-email@gmail.com"
export CWBDAYI_EMAIL_PASSWORD="your-app-password"
export EMAIL_TO="oceanicdayi@gmail.com"
```

### 執行步驟：

1. **設定環境變數**
   ```bash
   export SENDER_EMAIL_NEW="your-email@gmail.com"
   export CWBDAYI_EMAIL_PASSWORD="your-gmail-app-password"
   ```

2. **執行獨立郵件發送腳本**
   ```bash
   python3 send_openclaw_email.py
   ```

3. **或執行完整的新聞收集腳本**
   ```bash
   python3 scripts/collect_openclaw_news.py
   ```

### 注意事項：
- 📧 Gmail 應用程式密碼獲取：https://myaccount.google.com/apppasswords
- 🔐 必須啟用 Gmail 兩步驟驗證
- 🚫 不能使用一般密碼，必須使用應用程式密碼

---

## 方法三：檢視現有報告

如果只是想查看已生成的報告：

### 檢視 Markdown 檔案：
```bash
cat openclaw_news_report_2026-02-06.md
```

### 在 GitHub 上檢視：
- 直接訪問：https://github.com/cwbdayi638/knowledge/blob/main/openclaw_news_report_2026-02-06.md

---

## 故障排除

### 問題：郵件發送失敗

**可能原因與解決方法：**

1. **環境變數未設定**
   ```bash
   # 檢查環境變數
   echo $SENDER_EMAIL_NEW
   echo $CWBDAYI_EMAIL_PASSWORD
   ```

2. **使用了一般密碼而非應用程式密碼**
   - 解決：前往 https://myaccount.google.com/apppasswords 生成應用程式密碼
   - Gmail 必須啟用兩步驟驗證才能生成應用程式密碼

3. **Gmail 安全設定阻擋**
   - 解決：檢查 Gmail 安全性設定
   - 確認沒有收到 Google 的安全性警告郵件

4. **網路連線問題**
   - 解決：檢查網路連線
   - 嘗試使用不同的 SMTP 端口（465 或 587）

### 問題：GitHub Actions 執行失敗

**檢查步驟：**

1. **查看工作流程日誌**
   - 前往 Actions 標籤
   - 點擊失敗的執行
   - 查看詳細錯誤訊息

2. **確認 Secrets 已正確設定**
   - 前往儲存庫 Settings → Secrets and variables → Actions
   - 確認已設定：
     - `SENDER_EMAIL_NEW`
     - `CWBDAYI_EMAIL_PASSWORD` 或 `EMAIL_PASSWORD`

3. **檢查權限**
   - 確認工作流程有 `contents: write` 權限
   - 確認 GITHUB_TOKEN 有足夠權限

---

## 自動化排程

系統已設定為每天自動執行：

- **執行時間**：每天 05:00 UTC（台北時間 13:00）
- **執行內容**：
  1. 收集 OpenClaw 最新新聞
  2. 生成繁體中文報告
  3. 發送郵件至 oceanicdayi@gmail.com
  4. 更新 README.md
  5. 提交並推送變更

**無需手動操作，系統會自動運行！**

---

## 測試郵件功能

### 快速測試腳本：

```bash
# 設定環境變數
export SENDER_EMAIL_NEW="your-email@gmail.com"
export CWBDAYI_EMAIL_PASSWORD="your-app-password"

# 執行郵件發送
python3 send_openclaw_email.py
```

### 預期輸出：
```
============================================================
📧 OpenClaw 新聞報告郵件發送工具
============================================================

📄 報告檔案：openclaw_news_report_2026-02-06.md

🔍 檢查環境變數...
✅ SENDER_EMAIL_NEW: your-email@gmail.com
✅ 電子郵件密碼: 已設定
📬 收件人: oceanicdayi@gmail.com

📧 準備發送電子郵件至 oceanicdayi@gmail.com...
📎 附件檔案：openclaw_news_report_2026-02-06.md
📎 正在附加檔案：openclaw_news_report_2026-02-06.md
✅ 檔案已附加
🔐 正在連接 Gmail SMTP (SSL)...
   發件人：your-email@gmail.com
   收件人：oceanicdayi@gmail.com
🔑 正在驗證...
📤 正在發送郵件...
✅ 電子郵件發送成功！(使用 Gmail SMTP SSL)

============================================================
✅ 郵件發送完成！
============================================================
```

---

## 聯絡資訊

- **收件人**：oceanicdayi@gmail.com
- **郵件主旨**：OpenClaw 最新消息報告 - {日期}
- **附件**：openclaw_news_report_{日期}.md

---

*最後更新：2026-02-06*
