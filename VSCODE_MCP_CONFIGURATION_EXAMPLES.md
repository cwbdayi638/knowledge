# VS Code 配置示例 - GitHub Copilot MCP Server

此文件包含各種 VS Code 配置示例，用於在 GitHub Copilot 中啟用 MCP 服務器。

## 基本配置

### 單個 MCP 服務器

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

### 多個 MCP 服務器

```json
{
  "github.copilot.advanced": {
    "mcpServers": {
      "demo-server": {
        "command": "node",
        "args": ["/path/to/demo-mcp-server/server.js"]
      },
      "filesystem-server": {
        "command": "node",
        "args": ["/path/to/filesystem-server/server.js"]
      },
      "database-server": {
        "command": "node",
        "args": ["/path/to/database-server/server.js"]
      }
    }
  }
}
```

## 高級配置

### 使用環境變量

```json
{
  "github.copilot.advanced": {
    "mcpServers": {
      "api-server": {
        "command": "node",
        "args": ["/path/to/api-server/server.js"],
        "env": {
          "API_KEY": "your-api-key-here",
          "NODE_ENV": "production",
          "LOG_LEVEL": "info"
        }
      }
    }
  }
}
```

### 使用工作區相對路徑

```json
{
  "github.copilot.advanced": {
    "mcpServers": {
      "demo-server": {
        "command": "node",
        "args": ["${workspaceFolder}/demo-mcp-server/server.js"]
      }
    }
  }
}
```

### 使用 npx 運行

```json
{
  "github.copilot.advanced": {
    "mcpServers": {
      "mcp-server-fetch": {
        "command": "npx",
        "args": ["-y", "@modelcontextprotocol/server-fetch"]
      }
    }
  }
}
```

## 特定場景配置

### Python MCP 服務器

```json
{
  "github.copilot.advanced": {
    "mcpServers": {
      "python-server": {
        "command": "python",
        "args": ["/path/to/mcp_server.py"]
      }
    }
  }
}
```

### 使用虛擬環境的 Python 服務器

```json
{
  "github.copilot.advanced": {
    "mcpServers": {
      "python-venv-server": {
        "command": "/path/to/venv/bin/python",
        "args": ["/path/to/mcp_server.py"],
        "env": {
          "PYTHONPATH": "/path/to/project"
        }
      }
    }
  }
}
```

### 數據庫 MCP 服務器

```json
{
  "github.copilot.advanced": {
    "mcpServers": {
      "postgres-server": {
        "command": "node",
        "args": ["/path/to/postgres-mcp-server/server.js"],
        "env": {
          "DATABASE_URL": "postgresql://user:password@localhost:5432/mydb",
          "DB_POOL_SIZE": "10"
        }
      }
    }
  }
}
```

## 平台特定配置

### macOS

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

### Windows

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

### Linux

```json
{
  "github.copilot.advanced": {
    "mcpServers": {
      "demo-server": {
        "command": "node",
        "args": ["/home/username/projects/knowledge/demo-mcp-server/server.js"]
      }
    }
  }
}
```

## 調試配置

### 啟用詳細日誌

```json
{
  "github.copilot.advanced": {
    "mcpServers": {
      "demo-server": {
        "command": "node",
        "args": ["/path/to/server.js"],
        "env": {
          "DEBUG": "*",
          "LOG_LEVEL": "debug"
        }
      }
    }
  },
  "github.copilot.debug": true
}
```

## 完整配置示例

這是一個包含多個 MCP 服務器和其他 Copilot 設置的完整配置：

```json
{
  "github.copilot.enable": {
    "*": true,
    "yaml": true,
    "plaintext": false,
    "markdown": true
  },
  "github.copilot.advanced": {
    "mcpServers": {
      "demo-server": {
        "command": "node",
        "args": ["${workspaceFolder}/demo-mcp-server/server.js"]
      },
      "filesystem-server": {
        "command": "node",
        "args": ["/path/to/filesystem-server/server.js"],
        "env": {
          "ALLOWED_PATHS": "/home/user/documents,/home/user/projects"
        }
      },
      "api-server": {
        "command": "node",
        "args": ["/path/to/api-server/server.js"],
        "env": {
          "API_KEY": "${env:MY_API_KEY}",
          "NODE_ENV": "production"
        }
      }
    }
  },
  "github.copilot.inlineSuggest.enable": true,
  "github.copilot.editor.enableAutoCompletions": true
}
```

## 注意事項

1. **路徑**: 始終使用絕對路徑或 `${workspaceFolder}` 變量
2. **權限**: 確保服務器腳本具有執行權限（在 Unix 系統上運行 `chmod +x`）
3. **環境變量**: 敏感信息應使用環境變量，不要硬編碼
4. **重啟**: 修改配置後需要重啟 VS Code

## 測試配置

保存配置後，可以通過以下方式測試：

1. 重啟 VS Code
2. 打開輸出面板（查看 > 輸出）
3. 選擇 "GitHub Copilot"
4. 查看是否有 MCP 服務器相關的日誌
5. 在 Copilot Chat 中嘗試使用 MCP 工具

---

*本文件創建於 2026-02-10*  
*作者：GitHub Copilot Agent*
