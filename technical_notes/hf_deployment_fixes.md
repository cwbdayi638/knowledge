# Hugging Face Spaces 部署與故障排除實務 (Technical Notes)

針對 Python Web 應用（特別是 Gradio/Streamlit）在 Hugging Face Spaces 上的部署，以下是本次專案實踐中總結的關鍵問題與修復方案。

## 1. 依賴庫版本相容性 (Dependency Conflict)
### 問題描述 (ImportError)
在 Python 3.13 環境下，載入 `gradio` 時發生錯誤：
```text
ImportError: cannot import name 'HfFolder' from 'huggingface_hub'
```
### 根本原因
新版 `huggingface_hub` (v0.25+) 移除了舊有的 `HfFolder` 類別，而部分版本的 `gradio` 仍依賴此組件。

### 修復方案
在 `requirements.txt` 中精確鎖定穩定版本：
```text
gradio==4.19.2
huggingface-hub==0.24.6
```

## 2. Python 3.13 移除內建模組 (Standard Library Removal)
### 問題描述 (ModuleNotFoundError)
```text
ModuleNotFoundError: No module named 'pyaudioop' (or audioop)
```
### 根本原因
根據 **PEP 594**，Python 3.13 正式移除了 `audioop`、`pyaudioop` 等被標記為「過時」的標準庫模組。許多第三方套件（如繪圖或音訊處理相關）尚未完成更新，導致在 3.13 環境下崩潰。

### 修復方案
在 `README.md` 的 YAML Header 中強制指定使用 **Python 3.11** 容器環境：
```yaml
python_version: 3.11
```

## 3. 分支命名慣例 (Git Branching)
Hugging Face Spaces 預設會建置 **`main`** 分支的內容。若從本地推送預設為 `master` 分支，頁面將顯示空白或找不到檔案。
- **解決指令**: `git branch -M main && git push origin main`

---
*本筆記記錄於 2026-02-03，用於協助研究團隊未來進行 AI 模型 Web 化部署。*
