# GitHub Copilot 的 MCP Server 安裝與使用指南

## 📋 目錄
- [什麼是 MCP Server](#什麼是-mcp-server)
- [為什麼在 GitHub Copilot 中使用 MCP](#為什麼在-github-copilot-中使用-mcp)
- [系統需求](#系統需求)
- [安裝步驟](#安裝步驟)
- [配置示例](#配置示例)
- [實際演示](#實際演示)
- [常見問題](#常見問題)

---

## 什麼是 MCP Server

**MCP (Model Context Protocol)** 是一個開放協議，旨在標準化 AI 應用程式與外部數據源和工具之間的連接方式。由 Anthropic 開發，MCP 使 AI 助手能夠安全地訪問本地和遠程資源。

### MCP 的核心概念

```
┌─────────────────┐
│  AI 應用程式     │
│ (GitHub Copilot)│
└────────┬────────┘
         │ MCP Protocol
         │
    ┌────▼─────┐
    │ MCP Host │
    └────┬─────┘
         │
    ┌────▼──────────────┐
    │   MCP Servers     │
    ├───────────────────┤
    │ • 文件系統        │
    │ • 數據庫          │
    │ • API 服務        │
    │ • 自定義工具      │
    └───────────────────┘
```

### MCP 的主要組件

1. **MCP Host（主機）**: 運行在 AI 應用程式中，管理與 MCP 服務器的連接
2. **MCP Server（服務器）**: 提供特定功能或訪問特定資源的服務
3. **MCP Client（客戶端）**: 透過協議與服務器通信的接口

---

## 為什麼在 GitHub Copilot 中使用 MCP

### 主要優勢

✅ **擴展上下文**: 為 Copilot 提供項目特定的上下文信息  
✅ **訪問外部工具**: 連接數據庫、API、文件系統等  
✅ **自定義功能**: 創建專門的工具以滿足特定需求  
✅ **標準化接口**: 使用統一的協議連接不同的資源  
✅ **安全性**: 控制 AI 訪問資源的權限

### 使用場景

- 📚 訪問項目文檔和 API 規範
- 🗄️ 查詢數據庫架構和數據
- 🔧 執行自定義構建和測試工具
- 🌐 集成內部 API 和服務
- 📊 訪問分析和監控數據

---

## 系統需求

### 基本要求

- **操作系統**: Windows 10/11, macOS 10.15+, Linux
- **Node.js**: v18.0.0 或更高版本
- **npm**: v8.0.0 或更高版本
- **GitHub Copilot**: 最新版本的 VS Code 擴展或其他支持的編輯器

### 推薦配置

- **內存**: 至少 4GB RAM
- **存儲**: 至少 500MB 可用空間
- **網絡**: 穩定的互聯網連接（用於安裝依賴）

---

## 安裝步驟

### 步驟 1: 安裝 Node.js 和 npm

如果尚未安裝 Node.js，請訪問 [nodejs.org](https://nodejs.org/) 下載並安裝。

驗證安裝：
```bash
node --version  # 應顯示 v18.0.0 或更高
npm --version   # 應顯示 v8.0.0 或更高
```

### 步驟 2: 創建 MCP 服務器項目

創建一個新的項目目錄：
```bash
mkdir my-mcp-server
cd my-mcp-server
npm init -y
```

### 步驟 3: 安裝 MCP SDK

安裝 Anthropic 的 MCP SDK：
```bash
npm install @modelcontextprotocol/sdk
```

### 步驟 4: 創建簡單的 MCP 服務器

創建一個名為 `server.js` 的文件：

```javascript
#!/usr/bin/env node
import { Server } from "@modelcontextprotocol/sdk/server/index.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import {
  CallToolRequestSchema,
  ListToolsRequestSchema,
} from "@modelcontextprotocol/sdk/types.js";

// 創建 MCP 服務器實例
const server = new Server(
  {
    name: "demo-mcp-server",
    version: "1.0.0",
  },
  {
    capabilities: {
      tools: {},
    },
  }
);

// 定義可用的工具
server.setRequestHandler(ListToolsRequestSchema, async () => {
  return {
    tools: [
      {
        name: "get_project_info",
        description: "獲取項目的基本信息",
        inputSchema: {
          type: "object",
          properties: {
            projectName: {
              type: "string",
              description: "項目名稱",
            },
          },
          required: ["projectName"],
        },
      },
      {
        name: "calculate",
        description: "執行簡單的數學計算",
        inputSchema: {
          type: "object",
          properties: {
            operation: {
              type: "string",
              enum: ["add", "subtract", "multiply", "divide"],
              description: "要執行的操作",
            },
            a: {
              type: "number",
              description: "第一個數字",
            },
            b: {
              type: "number",
              description: "第二個數字",
            },
          },
          required: ["operation", "a", "b"],
        },
      },
    ],
  };
});

// 處理工具調用
server.setRequestHandler(CallToolRequestSchema, async (request) => {
  const { name, arguments: args } = request.params;

  if (name === "get_project_info") {
    return {
      content: [
        {
          type: "text",
          text: `項目名稱: ${args.projectName}\n版本: 1.0.0\n狀態: 活躍開發中`,
        },
      ],
    };
  } else if (name === "calculate") {
    let result;
    switch (args.operation) {
      case "add":
        result = args.a + args.b;
        break;
      case "subtract":
        result = args.a - args.b;
        break;
      case "multiply":
        result = args.a * args.b;
        break;
      case "divide":
        result = args.b !== 0 ? args.a / args.b : "錯誤：除數不能為零";
        break;
      default:
        throw new Error("不支持的操作");
    }
    return {
      content: [
        {
          type: "text",
          text: `計算結果: ${result}`,
        },
      ],
    };
  }

  throw new Error(`未知工具: ${name}`);
});

// 啟動服務器
async function main() {
  const transport = new StdioServerTransport();
  await server.connect(transport);
  console.error("Demo MCP Server 已啟動");
}

main().catch((error) => {
  console.error("服務器錯誤:", error);
  process.exit(1);
});
```

### 步驟 5: 更新 package.json

在 `package.json` 中添加以下內容：

```json
{
  "name": "demo-mcp-server",
  "version": "1.0.0",
  "description": "GitHub Copilot 的演示 MCP 服務器",
  "type": "module",
  "main": "server.js",
  "bin": {
    "demo-mcp-server": "./server.js"
  },
  "scripts": {
    "start": "node server.js"
  },
  "dependencies": {
    "@modelcontextprotocol/sdk": "^0.5.0"
  },
  "engines": {
    "node": ">=18.0.0"
  }
}
```

### 步驟 6: 使服務器可執行

在 Linux/macOS 上：
```bash
chmod +x server.js
```

### 步驟 7: 測試服務器

運行服務器以確保它正常工作：
```bash
npm start
```

如果看到 "Demo MCP Server 已啟動"，說明服務器正常運行。

---

## 配置示例

### 配置 GitHub Copilot 使用 MCP 服務器

#### 對於 VS Code

1. 打開 VS Code 設置（文件 > 首選項 > 設置）
2. 搜索 "copilot"
3. 找到 "GitHub Copilot: MCP Servers" 設置
4. 添加以下配置：

```json
{
  "github.copilot.advanced": {
    "mcpServers": {
      "demo-server": {
        "command": "node",
        "args": ["/path/to/my-mcp-server/server.js"]
      }
    }
  }
}
```

或者在 `settings.json` 中直接編輯：

```json
{
  "github.copilot.advanced": {
    "mcpServers": {
      "demo-server": {
        "command": "node",
        "args": ["${workspaceFolder}/../my-mcp-server/server.js"],
        "env": {
          "NODE_ENV": "production"
        }
      }
    }
  }
}
```

#### 對於 Claude Desktop（作為參考）

如果您使用 Claude Desktop，配置文件位於：

**macOS**: `~/Library/Application Support/Claude/claude_desktop_config.json`  
**Windows**: `%APPDATA%\Claude\claude_desktop_config.json`  
**Linux**: `~/.config/Claude/claude_desktop_config.json`

配置內容：
```json
{
  "mcpServers": {
    "demo-server": {
      "command": "node",
      "args": ["/path/to/my-mcp-server/server.js"]
    }
  }
}
```

---

## 實際演示

### 演示 1: 基本計算工具

創建 MCP 服務器後，在 GitHub Copilot 中可以這樣使用：

**用戶提問**:
```
使用 MCP 服務器計算 25 + 17
```

**Copilot 響應**（使用 MCP 工具）:
```
調用 calculate 工具...
參數: { operation: "add", a: 25, b: 17 }
結果: 計算結果: 42
```

### 演示 2: 項目信息查詢

**用戶提問**:
```
獲取 "knowledge" 項目的信息
```

**Copilot 響應**:
```
調用 get_project_info 工具...
參數: { projectName: "knowledge" }
結果: 
項目名稱: knowledge
版本: 1.0.0
狀態: 活躍開發中
```

### 演示 3: 更高級的 MCP 服務器 - 文件系統訪問

創建一個文件 `filesystem-server.js`:

```javascript
#!/usr/bin/env node
import { Server } from "@modelcontextprotocol/sdk/server/index.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import {
  CallToolRequestSchema,
  ListToolsRequestSchema,
} from "@modelcontextprotocol/sdk/types.js";
import fs from "fs/promises";
import path from "path";

const server = new Server(
  {
    name: "filesystem-mcp-server",
    version: "1.0.0",
  },
  {
    capabilities: {
      tools: {},
    },
  }
);

// 定義文件系統工具
server.setRequestHandler(ListToolsRequestSchema, async () => {
  return {
    tools: [
      {
        name: "read_file",
        description: "讀取文件內容",
        inputSchema: {
          type: "object",
          properties: {
            filepath: {
              type: "string",
              description: "文件路徑",
            },
          },
          required: ["filepath"],
        },
      },
      {
        name: "list_directory",
        description: "列出目錄內容",
        inputSchema: {
          type: "object",
          properties: {
            dirpath: {
              type: "string",
              description: "目錄路徑",
            },
          },
          required: ["dirpath"],
        },
      },
    ],
  };
});

// 處理工具調用
server.setRequestHandler(CallToolRequestSchema, async (request) => {
  const { name, arguments: args } = request.params;

  if (name === "read_file") {
    try {
      const content = await fs.readFile(args.filepath, "utf-8");
      return {
        content: [
          {
            type: "text",
            text: content,
          },
        ],
      };
    } catch (error) {
      return {
        content: [
          {
            type: "text",
            text: `錯誤：無法讀取文件 - ${error.message}`,
          },
        ],
        isError: true,
      };
    }
  } else if (name === "list_directory") {
    try {
      const files = await fs.readdir(args.dirpath);
      return {
        content: [
          {
            type: "text",
            text: `目錄內容:\n${files.join("\n")}`,
          },
        ],
      };
    } catch (error) {
      return {
        content: [
          {
            type: "text",
            text: `錯誤：無法讀取目錄 - ${error.message}`,
          },
        ],
        isError: true,
      };
    }
  }

  throw new Error(`未知工具: ${name}`);
});

async function main() {
  const transport = new StdioServerTransport();
  await server.connect(transport);
  console.error("Filesystem MCP Server 已啟動");
}

main().catch((error) => {
  console.error("服務器錯誤:", error);
  process.exit(1);
});
```

---

## 常見問題

### Q1: MCP 服務器無法啟動怎麼辦？

**答**: 檢查以下事項：
1. 確保 Node.js 版本 >= 18.0.0
2. 確保所有依賴已正確安裝（`npm install`）
3. 檢查文件權限（`chmod +x server.js`）
4. 查看錯誤日誌以獲取詳細信息

### Q2: GitHub Copilot 無法連接到 MCP 服務器？

**答**: 確認：
1. 配置文件中的路徑正確
2. 服務器已啟動並正常運行
3. VS Code 已重新加載配置（重啟 VS Code）
4. 檢查 VS Code 的輸出面板中的錯誤信息

### Q3: 如何調試 MCP 服務器？

**答**: 
```javascript
// 在服務器代碼中添加日誌
console.error("調試信息:", JSON.stringify(request, null, 2));

// 使用 VS Code 調試器
// 在 launch.json 中添加配置
{
  "type": "node",
  "request": "launch",
  "name": "Debug MCP Server",
  "program": "${workspaceFolder}/server.js"
}
```

### Q4: 可以創建哪些類型的 MCP 服務器？

**答**: MCP 服務器可以提供多種功能：
- 📁 文件系統訪問
- 🗄️ 數據庫查詢
- 🌐 API 調用
- 🔧 自定義工具和函數
- 📊 數據分析和可視化
- 🔍 搜索和索引服務

### Q5: MCP 服務器的安全性如何？

**答**: 
- ✅ 服務器在本地運行，不會向外部發送數據
- ✅ 可以通過代碼控制訪問權限
- ⚠️ 建議：不要在 MCP 服務器中硬編碼敏感信息
- ⚠️ 使用環境變量管理密鑰和憑證

### Q6: 如何更新 MCP 服務器？

**答**:
```bash
# 更新依賴
npm update @modelcontextprotocol/sdk

# 或指定版本
npm install @modelcontextprotocol/sdk@latest
```

---

## 進階主題

### 創建生產級 MCP 服務器

對於生產環境，考慮以下最佳實踐：

1. **錯誤處理**
```javascript
server.setRequestHandler(CallToolRequestSchema, async (request) => {
  try {
    // 工具邏輯
  } catch (error) {
    console.error("工具執行錯誤:", error);
    return {
      content: [
        {
          type: "text",
          text: `錯誤: ${error.message}`,
        },
      ],
      isError: true,
    };
  }
});
```

2. **日誌記錄**
```javascript
import winston from "winston";

const logger = winston.createLogger({
  level: "info",
  format: winston.format.json(),
  transports: [
    new winston.transports.File({ filename: "mcp-server.log" }),
  ],
});
```

3. **輸入驗證**
```javascript
function validateInput(args, schema) {
  // 實現 JSON Schema 驗證
  if (!args.projectName || typeof args.projectName !== "string") {
    throw new Error("無效的項目名稱");
  }
}
```

4. **環境配置**
```javascript
import dotenv from "dotenv";
dotenv.config();

const API_KEY = process.env.API_KEY;
const DATABASE_URL = process.env.DATABASE_URL;
```

### 集成第三方服務示例

#### GitHub API MCP 服務器

```javascript
import { Octokit } from "@octokit/rest";

const octokit = new Octokit({
  auth: process.env.GITHUB_TOKEN,
});

server.setRequestHandler(CallToolRequestSchema, async (request) => {
  if (request.params.name === "get_repo_info") {
    const { owner, repo } = request.params.arguments;
    const { data } = await octokit.repos.get({ owner, repo });
    
    return {
      content: [
        {
          type: "text",
          text: JSON.stringify(data, null, 2),
        },
      ],
    };
  }
});
```

---

## 資源鏈接

### 官方資源
- [MCP 官方文檔](https://modelcontextprotocol.io/)
- [MCP SDK GitHub](https://github.com/modelcontextprotocol/sdk)
- [GitHub Copilot 文檔](https://docs.github.com/en/copilot)

### 示例和模板
- [MCP 服務器示例](https://github.com/modelcontextprotocol/servers)
- [社區 MCP 服務器集合](https://github.com/topics/mcp-server)

### 相關工具
- [Node.js 官網](https://nodejs.org/)
- [VS Code](https://code.visualstudio.com/)
- [npm 包管理器](https://www.npmjs.com/)

---

## 總結

通過本指南，您已經學會了：

✅ 理解 MCP（Model Context Protocol）的概念和架構  
✅ 在系統上安裝和配置 MCP 服務器  
✅ 創建自定義 MCP 服務器以擴展 GitHub Copilot 的功能  
✅ 配置 GitHub Copilot 以使用 MCP 服務器  
✅ 實際演示和測試 MCP 服務器功能  

### 下一步

1. **實驗和學習**: 嘗試創建自己的 MCP 服務器
2. **擴展功能**: 添加更多工具和集成
3. **分享經驗**: 與社區分享您的 MCP 服務器
4. **持續改進**: 根據使用反饋優化服務器性能

---

**注意**: MCP 是一個相對較新的協議，某些功能可能仍在開發中。請參考最新的官方文檔以獲取最新信息。

---

*本文件創建於 2026-02-10*  
*作者：GitHub Copilot Agent*  
*儲存庫：cwbdayi638/knowledge*
