# OpenClaw AI 新聞收集系統說明文件

## 概述

此自動化系統每日收集 OpenClaw 的最新消息，將其翻譯為繁體中文並生成 Markdown 報告，同時發送電子郵件通知。

## 功能特點

1. **自動收集新聞**：從多個來源獲取 OpenClaw 相關資訊
   - GitHub Releases（版本發布）
   - GitHub Commits（最新開發動態）
   - Hacker News（社群討論）
   
2. **繁體中文翻譯**：自動將英文內容翻譯為繁體中文摘要

3. **自動化報告**：生成格式化的 Markdown 報告檔案

4. **電子郵件通知**：將報告透過電子郵件發送給指定收件人

5. **自動更新**：自動更新 README.md 並提交到 GitHub 儲存庫

## 檔案結構

```
knowledge/
├── .github/workflows/
│   └── openclaw-news.yml          # GitHub Actions 工作流程
├── scripts/
│   └── collect_openclaw_news.py   # 主要收集腳本
├── openclaw_news_report_*.md      # 每日生成的報告
└── README.md                       # 專案說明（自動更新）
```

## 使用方式

### 自動執行

系統會在每天 **05:00 UTC**（台北時間 13:00）自動執行。

### 手動執行

#### 方法 1：透過 GitHub Actions 界面

1. 前往儲存庫的 **Actions** 標籤
2. 選擇 **OpenClaw News Collection** 工作流程
3. 點擊 **Run workflow** 按鈕
4. 選擇分支並點擊 **Run workflow**

#### 方法 2：本地執行腳本

```bash
# 安裝相依套件
pip install requests beautifulsoup4

# 執行腳本
cd knowledge
python3 scripts/collect_openclaw_news.py
```

## 環境變數設定

為了啟用完整功能（特別是電子郵件通知），需要在 GitHub 儲存庫中設定以下 Secrets：

### 必要設定（電子郵件功能）

1. 前往 GitHub 儲存庫：**Settings** → **Secrets and variables** → **Actions**
2. 點擊 **New repository secret**
3. 新增以下任一組合：

#### 選項 A：使用 Gmail

- **名稱**：`EMAIL_PASSWORD`
- **值**：您的 Gmail 應用程式密碼

#### 選項 B：使用其他郵件服務

- **名稱**：`CWBDAYI_EMAIL_PASSWORD`
- **值**：您的郵件服務應用程式密碼
- **名稱**：`SENDER_EMAIL_NEW`
- **值**：發件人電子郵件地址

### Gmail 應用程式密碼設定

Gmail 需要使用「應用程式密碼」而非一般密碼：

1. 前往 [Google 帳戶設定](https://myaccount.google.com/)
2. 選擇 **安全性**
3. 啟用 **兩步驟驗證**（如果尚未啟用）
4. 前往 [應用程式密碼](https://myaccount.google.com/apppasswords)
5. 選擇「其他（自訂名稱）」→ 輸入「OpenClaw News」
6. 複製生成的 16 位密碼
7. 將此密碼設定為 GitHub Secret

## 輸出範例

每次執行會產生類似以下檔案：

- `openclaw_news_report_2026-02-06.md`
- `openclaw_news_report_2026-02-07.md`
- ...

報告內容包含：

```markdown
# OpenClaw 最新消息報告（日期）

**日期**：2026年02月06日  
**更新時間**：05:00 UTC  
**資料來源**：多個新聞來源

---

## 📰 最新消息摘要

### 1. OpenClaw 版本發布
- **來源**：GitHub Releases
- **日期**：2026-02-05
- **連結**：[查看詳情](https://github.com/...)
- **摘要**：繁體中文摘要內容...

---

## 🔑 本日重點
（關鍵資訊摘要）

## 📊 技術發展趨勢
（發展趨勢分析）
```

## 工作流程運作原理

1. **觸發時機**：
   - 排程：每天 05:00 UTC
   - 手動：透過 GitHub Actions 界面

2. **執行步驟**：
   ```
   下載儲存庫 → 設定 Python → 安裝套件 → 
   收集新聞 → 生成報告 → 發送郵件 → 
   更新 README → 提交並推送
   ```

3. **結果**：
   - 新增 Markdown 報告檔案
   - README.md 自動更新
   - 發送電子郵件通知（如已設定）

## 故障排除

### 問題：無法發送電子郵件

**解決方法**：
1. 確認已設定 `EMAIL_PASSWORD` 或 `CWBDAYI_EMAIL_PASSWORD`
2. 確認使用的是應用程式密碼，而非一般密碼
3. 檢查 Gmail 帳號是否啟用兩步驟驗證
4. 查看 GitHub Actions 日誌中的詳細錯誤訊息

### 問題：無法收集新聞

**解決方法**：
1. 檢查網路連線是否正常
2. 確認 API 端點是否可訪問
3. 腳本會使用備用內容，不會完全失敗

### 問題：工作流程執行失敗

**解決方法**：
1. 前往 **Actions** 標籤查看錯誤日誌
2. 確認所有必要的 Secrets 都已正確設定
3. 嘗試手動執行以測試
4. 檢查 Python 相依套件是否正確安裝

## 進階設定

### 修改執行時間

編輯 `.github/workflows/openclaw-news.yml`：

```yaml
on:
  schedule:
    # 範例：改為每天 12:00 UTC
    - cron: '0 12 * * *'
```

Cron 表達式格式：`分 時 日 月 星期`

### 修改收件人

編輯工作流程檔案中的環境變數：

```yaml
env:
  EMAIL_TO: your-email@example.com
```

或修改 `scripts/collect_openclaw_news.py` 中的預設值：

```python
EMAIL_TO = os.environ.get('EMAIL_TO', 'your-email@example.com')
```

## 相關資源

- [GitHub Actions 文件](https://docs.github.com/actions)
- [OpenClaw 官方儲存庫](https://github.com/openchatai/openclaw)
- [Gmail 應用程式密碼說明](https://support.google.com/accounts/answer/185833)

## 技術規格

- **程式語言**：Python 3.11+
- **主要套件**：
  - `requests`：HTTP 請求
  - `beautifulsoup4`：HTML 解析
- **執行平台**：Ubuntu (GitHub Actions)
- **儲存格式**：Markdown (UTF-8)

---

*最後更新：2026-02-06*
