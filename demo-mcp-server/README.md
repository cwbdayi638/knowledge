# Demo MCP Server for GitHub Copilot

這是一個用於 GitHub Copilot 的演示 MCP（Model Context Protocol）服務器。

## 功能特性

此服務器提供以下工具：

1. **get_project_info** - 獲取項目的基本信息
2. **calculate** - 執行簡單的數學計算（加、減、乘、除）
3. **get_weather** - 獲取模擬的天氣信息
4. **fetch_url** - 從外部服務器獲取數據（HTTP 客戶端工具）🆕

## 安裝

確保已安裝 Node.js（版本 >= 18.0.0）：

```bash
node --version
```

安裝依賴：

```bash
npm install
```

## 使用方法

### 運行服務器

```bash
npm start
```

或直接運行：

```bash
node server.js
```

### 配置 GitHub Copilot

在 VS Code 的設置中（`settings.json`），添加以下配置：

```json
{
  "github.copilot.advanced": {
    "mcpServers": {
      "demo-server": {
        "command": "node",
        "args": ["/path/to/knowledge/demo-mcp-server/server.js"]
      }
    }
  }
}
```

將 `/path/to/knowledge/demo-mcp-server/server.js` 替換為此服務器的實際路徑。

## 工具示例

### 1. 計算工具

```javascript
// Copilot 可以使用此工具執行計算
calculate({
  operation: "add",
  a: 25,
  b: 17
})
// 返回: "計算結果: 25 add 17 = 42"
```

### 2. 項目信息

```javascript
get_project_info({
  projectName: "knowledge"
})
// 返回項目的詳細信息
```

### 3. 天氣信息

```javascript
get_weather({
  location: "台北"
})
// 返回模擬的天氣數據
```

### 4. HTTP 客戶端（從外部服務器獲取數據）🆕

```javascript
// GET 請求示例
fetch_url({
  url: "https://api.github.com/repos/modelcontextprotocol/sdk"
})
// 返回 GitHub 倉庫信息

// POST 請求示例
fetch_url({
  url: "https://httpbin.org/post",
  method: "POST",
  headers: {
    "Content-Type": "application/json"
  },
  body: JSON.stringify({ key: "value" })
})
// 返回 POST 請求的響應

// 查詢公開 API 示例
fetch_url({
  url: "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_hour.geojson"
})
// 返回過去一小時的全球地震數據
```

**支援的功能**:
- ✅ HTTP GET 和 POST 請求
- ✅ 自定義 HTTP 標頭
- ✅ JSON 和純文本響應
- ✅ 10 秒請求超時
- ✅ 響應大小限制（10KB）
- ✅ 安全 URL 驗證（僅支援 HTTP/HTTPS）

**使用場景**:
- 🌍 查詢公開 API（天氣、地震、新聞等）
- 📊 獲取即時數據
- 🔗 集成第三方服務
- 🧪 測試 API 端點

## 文件結構

```
demo-mcp-server/
├── server.js       # MCP 服務器主文件
├── package.json    # 項目配置和依賴
└── README.md       # 本文件
```

## 依賴

- `@modelcontextprotocol/sdk` - MCP SDK 核心庫

## 系統需求

- Node.js >= 18.0.0
- npm >= 8.0.0

## 許可證

MIT

## 更多信息

請參閱主文檔：[MCP_SERVER_GITHUB_COPILOT_GUIDE.md](../MCP_SERVER_GITHUB_COPILOT_GUIDE.md)
