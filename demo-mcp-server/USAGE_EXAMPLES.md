# MCP Server 使用示例

## 📚 完整的工具使用示例

本文檔提供了 Demo MCP Server 所有工具的詳細使用示例。

---

## 🧮 1. Calculate 工具

### 基本運算

#### 加法
```
用戶提問: 使用 MCP 工具計算 25 + 17

MCP 調用:
{
  "name": "calculate",
  "arguments": {
    "operation": "add",
    "a": 25,
    "b": 17
  }
}

返回結果:
計算結果: 25 add 17 = 42
```

#### 減法
```
用戶提問: 使用 MCP 工具計算 100 - 35

返回結果:
計算結果: 100 subtract 35 = 65
```

#### 乘法
```
用戶提問: 使用 MCP 工具計算 12 * 8

返回結果:
計算結果: 12 multiply 8 = 96
```

#### 除法
```
用戶提問: 使用 MCP 工具計算 144 / 12

返回結果:
計算結果: 144 divide 12 = 12
```

#### 錯誤處理 - 除以零
```
用戶提問: 使用 MCP 工具計算 10 / 0

返回結果:
錯誤: 除數不能為零
```

---

## 📊 2. Get Project Info 工具

### 獲取項目信息

```
用戶提問: 使用 MCP 工具獲取 "knowledge" 項目的信息

MCP 調用:
{
  "name": "get_project_info",
  "arguments": {
    "projectName": "knowledge"
  }
}

返回結果:
項目信息:
{
  "name": "knowledge",
  "version": "1.0.0",
  "status": "活躍開發中",
  "description": "這是一個演示 MCP 服務器的項目",
  "lastUpdated": "2026-02-10T01:30:00.000Z"
}
```

### 其他項目示例

```
用戶提問: 獲取 "demo-mcp-server" 項目的詳細信息

返回結果:
項目信息:
{
  "name": "demo-mcp-server",
  "version": "1.0.0",
  "status": "活躍開發中",
  "description": "這是一個演示 MCP 服務器的項目",
  "lastUpdated": "2026-02-10T01:31:00.000Z"
}
```

---

## 🌤️ 3. Get Weather 工具

### 查詢天氣信息

```
用戶提問: 使用 MCP 工具查詢台北的天氣

MCP 調用:
{
  "name": "get_weather",
  "arguments": {
    "location": "台北"
  }
}

返回結果:
台北 的天氣:
溫度: 23°C
狀況: 多雲
濕度: 65%
更新時間: 2026-02-10T01:32:00.000Z
```

### 其他城市示例

```
用戶提問: 查詢東京的天氣狀況

返回結果:
東京 的天氣:
溫度: 18°C
狀況: 晴朗
濕度: 55%
更新時間: 2026-02-10T01:33:00.000Z
```

**注意**: 這是模擬數據，每次調用會返回隨機生成的天氣信息。

---

## 🌐 4. Fetch URL 工具 (HTTP 客戶端)

### 示例 1: 查詢 GitHub API

```
用戶提問: 使用 MCP 工具從 GitHub API 獲取 modelcontextprotocol/sdk 倉庫信息

MCP 調用:
{
  "name": "fetch_url",
  "arguments": {
    "url": "https://api.github.com/repos/modelcontextprotocol/sdk"
  }
}

返回結果:
HTTP GET 請求到 https://api.github.com/repos/modelcontextprotocol/sdk
狀態碼: 200 OK
Content-Type: application/json; charset=utf-8

響應內容:
{
  "id": 123456789,
  "name": "sdk",
  "full_name": "modelcontextprotocol/sdk",
  "description": "Model Context Protocol SDK",
  "stargazers_count": 1234,
  "forks_count": 56,
  ...
}
```

### 示例 2: 查詢地震數據

```
用戶提問: 獲取最近一小時的全球地震數據

MCP 調用:
{
  "name": "fetch_url",
  "arguments": {
    "url": "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_hour.geojson"
  }
}

返回結果:
HTTP GET 請求到 https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_hour.geojson
狀態碼: 200 OK
Content-Type: application/json

響應內容:
{
  "type": "FeatureCollection",
  "metadata": {
    "generated": 1707523200000,
    "title": "USGS All Earthquakes, Past Hour"
  },
  "features": [
    {
      "type": "Feature",
      "properties": {
        "mag": 4.5,
        "place": "10km SSW of Volcano, Hawaii",
        "time": 1707522800000,
        "updated": 1707523000000
      },
      ...
    }
  ]
}
```

### 示例 3: 使用自定義標頭

```
用戶提問: 從 API 獲取數據，需要添加認證標頭

MCP 調用:
{
  "name": "fetch_url",
  "arguments": {
    "url": "https://api.example.com/data",
    "headers": {
      "Authorization": "Bearer YOUR_API_TOKEN",
      "Accept": "application/json"
    }
  }
}
```

### 示例 4: POST 請求

```
用戶提問: 向測試 API 發送 POST 請求

MCP 調用:
{
  "name": "fetch_url",
  "arguments": {
    "url": "https://httpbin.org/post",
    "method": "POST",
    "headers": {
      "Content-Type": "application/json"
    },
    "body": "{\"message\": \"Hello from MCP Server\", \"timestamp\": \"2026-02-10T01:35:00.000Z\"}"
  }
}

返回結果:
HTTP POST 請求到 https://httpbin.org/post
狀態碼: 200 OK
Content-Type: application/json

響應內容:
{
  "args": {},
  "data": "{\"message\": \"Hello from MCP Server\", \"timestamp\": \"2026-02-10T01:35:00.000Z\"}",
  "headers": {
    "Content-Type": "application/json",
    "User-Agent": "MCP-Server/1.0"
  },
  "json": {
    "message": "Hello from MCP Server",
    "timestamp": "2026-02-10T01:35:00.000Z"
  },
  "url": "https://httpbin.org/post"
}
```

### 示例 5: 查詢公開的天氣 API

```
用戶提問: 從 OpenWeatherMap 獲取台北的真實天氣數據

MCP 調用:
{
  "name": "fetch_url",
  "arguments": {
    "url": "https://api.openweathermap.org/data/2.5/weather?q=Taipei&appid=YOUR_API_KEY&units=metric"
  }
}

返回結果:
HTTP GET 請求到 https://api.openweathermap.org/data/2.5/weather?q=Taipei...
狀態碼: 200 OK
Content-Type: application/json

響應內容:
{
  "coord": {"lon": 121.5319, "lat": 25.048},
  "weather": [
    {"id": 801, "main": "Clouds", "description": "few clouds"}
  ],
  "main": {
    "temp": 22.5,
    "feels_like": 22.3,
    "humidity": 65
  },
  "name": "Taipei"
}
```

### 示例 6: 查詢 JSON Placeholder API

```
用戶提問: 獲取示例用戶數據

MCP 調用:
{
  "name": "fetch_url",
  "arguments": {
    "url": "https://jsonplaceholder.typicode.com/users/1"
  }
}

返回結果:
HTTP GET 請求到 https://jsonplaceholder.typicode.com/users/1
狀態碼: 200 OK
Content-Type: application/json

響應內容:
{
  "id": 1,
  "name": "Leanne Graham",
  "username": "Bret",
  "email": "Sincere@april.biz",
  "address": {
    "street": "Kulas Light",
    "city": "Gwenborough"
  }
}
```

### 錯誤處理示例

#### 無效的 URL
```
用戶提問: 使用無效的 URL

MCP 調用:
{
  "name": "fetch_url",
  "arguments": {
    "url": "not-a-valid-url"
  }
}

返回結果:
錯誤: 無效的 URL: Invalid URL
```

#### 不支援的協議
```
用戶提問: 嘗試使用 FTP 協議

MCP 調用:
{
  "name": "fetch_url",
  "arguments": {
    "url": "ftp://example.com/file.txt"
  }
}

返回結果:
錯誤: 只支援 HTTP 和 HTTPS 協議
```

#### 請求超時
```
如果請求超過 10 秒未完成，將返回超時錯誤。
```

---

## 🔧 組合使用示例

### 場景 1: 計算並查詢

```
用戶: 計算 25 + 17，然後查詢台北天氣

步驟 1: 調用 calculate 工具
結果: 計算結果: 25 add 17 = 42

步驟 2: 調用 get_weather 工具
結果: 台北的天氣: 溫度 23°C，多雲
```

### 場景 2: 從 API 獲取數據並分析

```
用戶: 從 GitHub API 獲取 sdk 倉庫信息，告訴我星標數量

步驟 1: 調用 fetch_url 工具
結果: 返回包含 stargazers_count 的 JSON

步驟 2: AI 分析 JSON 數據
結果: "該倉庫有 1234 個星標"
```

### 場景 3: 多個 API 調用

```
用戶: 分別從 GitHub 和 USGS 獲取數據

步驟 1: 調用 fetch_url 獲取 GitHub 數據
步驟 2: 調用 fetch_url 獲取地震數據
步驟 3: AI 綜合分析兩個數據源
```

---

## 💡 最佳實踐

### 1. 使用具體的提示詞

❌ 不好: "計算一些東西"
✅ 好: "使用 MCP 工具計算 25 + 17"

### 2. 明確指定 API 端點

❌ 不好: "獲取一些數據"
✅ 好: "使用 MCP 工具從 https://api.github.com/repos/owner/repo 獲取倉庫信息"

### 3. 提供完整的 URL

❌ 不好: "api.github.com/repos/owner/repo"
✅ 好: "https://api.github.com/repos/owner/repo"

### 4. POST 請求時指定 Content-Type

✅ 好的做法:
```json
{
  "method": "POST",
  "headers": {
    "Content-Type": "application/json"
  },
  "body": "{\"key\": \"value\"}"
}
```

### 5. 處理大型響應

由於響應限制為 10KB，對於大型 API 響應：
- 使用 API 的分頁參數
- 請求特定字段
- 使用過濾參數減少數據量

---

## 🔐 安全注意事項

### 1. 不要在提示詞中暴露敏感信息

❌ 危險:
```
"使用 API 密鑰 abc123xyz 從 API 獲取數據"
```

✅ 安全:
```
"從需要認證的 API 獲取數據"
（將 API 密鑰存儲在環境變量中）
```

### 2. 驗證數據來源

- 只訪問信任的 API 端點
- 使用 HTTPS 而非 HTTP
- 驗證 API 響應的合法性

### 3. 注意速率限制

許多公開 API 有速率限制（如 GitHub API）：
- 不要在短時間內發送大量請求
- 遵守 API 提供者的使用條款

---

## 📚 相關文檔

- [MCP Server 能力清單](../MCP_SERVER_CAPABILITIES.md)
- [MCP Server 主要指南](../MCP_SERVER_GITHUB_COPILOT_GUIDE.md)
- [快速開始指南](../MCP_QUICK_START.md)

---

*文件創建時間: 2026-02-10*  
*作者: GitHub Copilot Agent*  
*版本: 1.0.0*
