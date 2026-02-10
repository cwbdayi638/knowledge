# MCP Server 能力清單與類型說明

## 📋 本知識庫中可用的 MCP Server 類型

### 1. 🎯 Demo MCP Server（演示服務器）
**位置**: `demo-mcp-server/server.js`

這是一個功能完整的演示 MCP 服務器，展示了 MCP 協議的核心能力。

#### 提供的工具 (Tools)：

##### 🧮 `calculate` - 數學計算工具
執行基本的數學運算。

**輸入參數**:
```json
{
  "operation": "add|subtract|multiply|divide",
  "a": 數字,
  "b": 數字
}
```

**使用示例**:
```
用戶: 使用 MCP 工具計算 25 + 17
結果: 計算結果: 25 add 17 = 42
```

##### 📊 `get_project_info` - 項目信息查詢
獲取指定項目的詳細信息和元數據。

**輸入參數**:
```json
{
  "projectName": "項目名稱字串"
}
```

**使用示例**:
```
用戶: 獲取 "knowledge" 項目的信息
結果: 返回項目名稱、版本、狀態、描述和最後更新時間
```

##### 🌤️ `get_weather` - 天氣信息查詢
獲取指定位置的模擬天氣信息（演示用）。

**輸入參數**:
```json
{
  "location": "位置名稱"
}
```

**使用示例**:
```
用戶: 查詢台北的天氣
結果: 返回溫度、天氣狀況、濕度等信息
```

##### 🌐 `fetch_url` - HTTP 客戶端工具（新增）
從外部服務器獲取數據，支援 HTTP GET 和 POST 請求。

**輸入參數**:
```json
{
  "url": "要訪問的 URL",
  "method": "GET|POST",
  "headers": {
    "Header-Name": "Header-Value"
  },
  "body": "POST 請求的內容（可選）"
}
```

**使用示例**:
```
用戶: 使用 MCP 工具從 https://api.example.com/data 獲取數據
結果: 返回 API 響應內容
```

**支援的用途**:
- 🔍 查詢公開 API（天氣、地震、新聞等）
- 📡 獲取即時數據源
- 🔗 集成第三方服務
- 📊 收集監控數據

---

## 🚀 MCP Server 的工作原理

### 架構圖

```
┌──────────────────────┐
│   GitHub Copilot     │
│   (AI 助手)          │
└──────────┬───────────┘
           │ MCP Protocol
           │ (JSON-RPC 2.0)
           │
┌──────────▼───────────┐
│    MCP Host          │
│  (VS Code Extension) │
└──────────┬───────────┘
           │
           │ stdio transport
           │
┌──────────▼───────────┐
│  MCP Server          │
│  (Node.js Process)   │
├──────────────────────┤
│  工具集 (Tools):     │
│  • calculate         │
│  • get_project_info  │
│  • get_weather       │
│  • fetch_url         │
└──────────┬───────────┘
           │
┌──────────▼───────────┐
│  外部資源 (Resources)│
│  • 文件系統          │
│  • 數據庫            │
│  • Web APIs          │
│  • 自定義服務        │
└──────────────────────┘
```

### 通信流程

1. **用戶發起請求**: 在 GitHub Copilot Chat 中輸入問題
2. **Copilot 分析**: AI 判斷是否需要使用 MCP 工具
3. **列出工具**: MCP Host 向 Server 請求可用工具列表
4. **選擇工具**: Copilot 選擇合適的工具並準備參數
5. **調用工具**: 通過 MCP 協議發送工具調用請求
6. **執行工具**: Server 執行相應的邏輯並訪問資源
7. **返回結果**: 結果通過 MCP 協議返回給 Copilot
8. **呈現答案**: Copilot 整合結果並呈現給用戶

---

## 🛠️ 可以創建的 MCP Server 類型

### 1. 📁 文件系統 MCP Server
**功能**: 訪問和管理本地文件系統
- 讀取文件內容
- 列出目錄
- 搜索文件
- 監控文件變化

### 2. 🗄️ 數據庫 MCP Server
**功能**: 查詢和管理數據庫
- 執行 SQL 查詢
- 獲取表結構
- 數據統計分析
- 支援 MySQL、PostgreSQL、MongoDB 等

### 3. 🌐 API 集成 MCP Server
**功能**: 連接第三方 API 服務
- RESTful API 調用
- GraphQL 查詢
- WebSocket 連接
- OAuth 認證

**示例服務**:
- GitHub API - 倉庫管理、Issues、PR
- OpenWeather API - 天氣數據
- News API - 新聞內容
- Earthquake API - 地震數據

### 4. 🔧 開發工具 MCP Server
**功能**: 集成開發工具和工作流
- Git 操作
- Docker 容器管理
- CI/CD 狀態查詢
- 測試執行器

### 5. 📊 數據分析 MCP Server
**功能**: 數據處理和分析
- 統計計算
- 數據可視化
- 機器學習推理
- 報表生成

### 6. 🔐 認證與安全 MCP Server
**功能**: 身份驗證和安全管理
- Token 管理
- 密鑰加密
- 權限驗證
- 安全掃描

---

## 💡 作為 MCP Server 連接到外部服務器

### 是的，MCP Server 可以作為客戶端連接到其他服務器！

MCP Server 本質上是一個 Node.js 進程，因此可以：

#### ✅ 支援的連接方式

1. **HTTP/HTTPS 請求**
   ```javascript
   import axios from 'axios';
   
   // GET 請求
   const response = await axios.get('https://api.example.com/data');
   
   // POST 請求
   const result = await axios.post('https://api.example.com/submit', {
     data: 'value'
   });
   ```

2. **WebSocket 連接**
   ```javascript
   import WebSocket from 'ws';
   
   const ws = new WebSocket('wss://example.com/stream');
   ws.on('message', (data) => {
     console.log('Received:', data);
   });
   ```

3. **數據庫連接**
   ```javascript
   import mysql from 'mysql2/promise';
   
   const connection = await mysql.createConnection({
     host: 'localhost',
     user: 'root',
     database: 'mydb'
   });
   
   const [rows] = await connection.execute('SELECT * FROM users');
   ```

4. **gRPC 調用**
   ```javascript
   import grpc from '@grpc/grpc-js';
   
   const client = new ServiceClient(
     'localhost:50051',
     grpc.credentials.createInsecure()
   );
   ```

#### 🎯 實際應用場景

##### 場景 1: 地震數據 MCP Server
```javascript
// 連接到 USGS 地震 API
const earthquakeData = await fetch(
  'https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_day.geojson'
);
```

##### 場景 2: 天氣服務 MCP Server
```javascript
// 連接到氣象局 API
const weatherData = await fetch(
  'https://opendata.cwa.gov.tw/api/v1/rest/datastore/...'
);
```

##### 場景 3: 新聞聚合 MCP Server
```javascript
// 連接到新聞 API
const news = await fetch(
  'https://newsapi.org/v2/top-headlines?country=tw&apiKey=...'
);
```

##### 場景 4: 內部服務集成
```javascript
// 連接到公司內部 API
const internalData = await fetch(
  'http://internal-api.company.com/data',
  {
    headers: {
      'Authorization': `Bearer ${process.env.API_TOKEN}`
    }
  }
);
```

---

## 🔒 安全最佳實踐

### 1. 使用環境變量管理敏感信息
```javascript
import dotenv from 'dotenv';
dotenv.config();

const API_KEY = process.env.API_KEY;
const DATABASE_URL = process.env.DATABASE_URL;
```

### 2. 驗證和清理輸入
```javascript
function validateUrl(url) {
  try {
    const urlObj = new URL(url);
    // 只允許 HTTPS
    if (urlObj.protocol !== 'https:') {
      throw new Error('只允許 HTTPS 連接');
    }
    return true;
  } catch (error) {
    throw new Error('無效的 URL');
  }
}
```

### 3. 實現速率限制
```javascript
const rateLimiter = {
  requests: new Map(),
  limit: 100, // 每小時最多 100 次請求
  
  checkLimit(toolName) {
    const now = Date.now();
    const hour = Math.floor(now / 3600000);
    const key = `${toolName}-${hour}`;
    
    const count = this.requests.get(key) || 0;
    if (count >= this.limit) {
      throw new Error('已達到速率限制');
    }
    
    this.requests.set(key, count + 1);
  }
};
```

### 4. 設置超時限制
```javascript
const response = await axios.get(url, {
  timeout: 5000 // 5秒超時
});
```

### 5. 錯誤處理和日誌記錄
```javascript
try {
  const result = await fetchExternalData(url);
  logger.info('成功獲取數據', { url, status: 200 });
  return result;
} catch (error) {
  logger.error('獲取數據失敗', { url, error: error.message });
  throw error;
}
```

---

## 📚 相關文檔

- [MCP Server GitHub Copilot 完整指南](MCP_SERVER_GITHUB_COPILOT_GUIDE.md)
- [MCP 快速開始指南](MCP_QUICK_START.md)
- [VS Code 配置示例](VSCODE_MCP_CONFIGURATION_EXAMPLES.md)
- [Demo MCP Server 說明](demo-mcp-server/README.md)

---

## 🎓 總結

### MCP Server 的核心能力

1. **雙向通信**: 作為服務器接收請求，同時作為客戶端訪問外部資源
2. **工具擴展**: 可以無限擴展各種自定義工具
3. **安全隔離**: 在獨立進程中運行，通過協議進行受控通信
4. **異步執行**: 支援並發處理多個請求
5. **標準化接口**: 遵循 MCP 協議標準，易於集成

### 回答原始問題

**"你有什麼樣的 MCP Server？"**
- 我們有一個功能完整的 Demo MCP Server
- 提供 4 種工具：計算、項目信息、天氣、HTTP 客戶端
- 可以根據需求擴展更多工具

**"你能成為一個 MCP Server 連接到服務器並獲取信息嗎？"**
- **是的！** MCP Server 完全可以連接到外部服務器
- 支援 HTTP/HTTPS、WebSocket、數據庫、gRPC 等多種連接方式
- 本專案的 MCP Server 已包含 `fetch_url` 工具，可以從任何 HTTP(S) 端點獲取數據
- 可以輕鬆集成各種第三方 API 服務

---

*文件創建時間: 2026-02-10*  
*作者: GitHub Copilot Agent*  
*版本: 1.0.0*
