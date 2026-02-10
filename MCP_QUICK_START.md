# 快速開始：在 GitHub Copilot 中使用 MCP Server

## 🚀 5 分鐘快速上手指南

### 步驟 1: 檢查環境

```bash
# 檢查 Node.js 版本（需要 >= 18.0.0）
node --version

# 如果沒有安裝，請訪問 https://nodejs.org/ 下載安裝
```

### 步驟 2: 進入演示服務器目錄

```bash
cd /home/runner/work/knowledge/knowledge/demo-mcp-server

# 或者使用您克隆的實際路徑
cd /path/to/knowledge/demo-mcp-server
```

### 步驟 3: 安裝依賴

```bash
npm install
```

### 步驟 4: 測試服務器

```bash
npm start
```

您應該看到：
```
Demo MCP Server 已啟動 - 提供以下工具:
  1. get_project_info - 獲取項目信息
  2. calculate - 執行數學計算
  3. get_weather - 獲取天氣信息
```

按 `Ctrl+C` 停止服務器。

### 步驟 5: 配置 VS Code（GitHub Copilot）

1. 打開 VS Code
2. 按 `Ctrl+Shift+P`（macOS: `Cmd+Shift+P`）打開命令面板
3. 輸入 "Preferences: Open User Settings (JSON)"
4. 添加以下配置：

```json
{
  "github.copilot.advanced": {
    "mcpServers": {
      "demo-server": {
        "command": "node",
        "args": ["/absolute/path/to/knowledge/demo-mcp-server/server.js"]
      }
    }
  }
}
```

**重要**: 將 `/absolute/path/to/knowledge/demo-mcp-server/server.js` 替換為實際的絕對路徑。

### 步驟 6: 重啟 VS Code

關閉並重新打開 VS Code，使配置生效。

### 步驟 7: 測試 MCP 工具

在 VS Code 中，打開 GitHub Copilot Chat，嘗試以下提示：

1. **測試計算工具**:
   ```
   使用 MCP 工具計算 25 + 17
   ```

2. **測試項目信息**:
   ```
   使用 MCP 工具獲取 "knowledge" 項目的信息
   ```

3. **測試天氣工具**:
   ```
   使用 MCP 工具查詢台北的天氣
   ```

---

## 📝 配置示例（完整版）

### macOS/Linux 配置

```json
{
  "github.copilot.advanced": {
    "mcpServers": {
      "demo-server": {
        "command": "node",
        "args": ["/Users/username/projects/knowledge/demo-mcp-server/server.js"]
      }
    }
  }
}
```

### Windows 配置

```json
{
  "github.copilot.advanced": {
    "mcpServers": {
      "demo-server": {
        "command": "node",
        "args": ["C:\\Users\\username\\projects\\knowledge\\demo-mcp-server\\server.js"]
      }
    }
  }
}
```

---

## 🔧 故障排除

### 問題 1: 找不到 node 命令

**解決方案**: 安裝 Node.js
```bash
# macOS (使用 Homebrew)
brew install node

# Ubuntu/Debian
sudo apt install nodejs npm

# Windows: 訪問 https://nodejs.org/ 下載安裝
```

### 問題 2: MCP 服務器無法啟動

**檢查**:
1. 確認路徑正確
2. 確認 Node.js 版本 >= 18
3. 確認已運行 `npm install`
4. 查看 VS Code 的輸出面板（查看 > 輸出 > GitHub Copilot）

### 問題 3: Copilot 沒有使用 MCP 工具

**檢查**:
1. 確認配置文件正確
2. 重啟 VS Code
3. 確認服務器路徑是絕對路徑
4. 在提示中明確要求使用 MCP 工具

---

## 📚 下一步

- 閱讀完整指南: [MCP_SERVER_GITHUB_COPILOT_GUIDE.md](MCP_SERVER_GITHUB_COPILOT_GUIDE.md)
- 查看演示服務器代碼: [demo-mcp-server/server.js](demo-mcp-server/server.js)
- 創建自己的 MCP 工具
- 集成第三方 API

---

## ✅ 檢查清單

- [ ] 已安裝 Node.js >= 18.0.0
- [ ] 已運行 `npm install` 安裝依賴
- [ ] 已測試服務器可以啟動
- [ ] 已在 VS Code 中配置 MCP 服務器路徑
- [ ] 已重啟 VS Code
- [ ] 已測試 Copilot 可以使用 MCP 工具

---

*本文件創建於 2026-02-10*  
*作者：GitHub Copilot Agent*
