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
      {
        name: "get_weather",
        description: "獲取天氣信息（演示用）",
        inputSchema: {
          type: "object",
          properties: {
            location: {
              type: "string",
              description: "位置名稱",
            },
          },
          required: ["location"],
        },
      },
    ],
  };
});

// 處理工具調用
server.setRequestHandler(CallToolRequestSchema, async (request) => {
  const { name, arguments: args } = request.params;

  try {
    if (name === "get_project_info") {
      const projectInfo = {
        name: args.projectName,
        version: "1.0.0",
        status: "活躍開發中",
        description: "這是一個演示 MCP 服務器的項目",
        lastUpdated: new Date().toISOString(),
      };
      
      return {
        content: [
          {
            type: "text",
            text: `項目信息:\n${JSON.stringify(projectInfo, null, 2)}`,
          },
        ],
      };
    } else if (name === "calculate") {
      let result;
      const { operation, a, b } = args;
      
      switch (operation) {
        case "add":
          result = a + b;
          break;
        case "subtract":
          result = a - b;
          break;
        case "multiply":
          result = a * b;
          break;
        case "divide":
          if (b === 0) {
            throw new Error("除數不能為零");
          }
          result = a / b;
          break;
        default:
          throw new Error(`不支持的操作: ${operation}`);
      }
      
      return {
        content: [
          {
            type: "text",
            text: `計算結果: ${a} ${operation} ${b} = ${result}`,
          },
        ],
      };
    } else if (name === "get_weather") {
      // 演示用的模擬天氣數據
      const weatherData = {
        location: args.location,
        temperature: Math.floor(Math.random() * 30) + 10,
        condition: ["晴朗", "多雲", "小雨", "陰天"][Math.floor(Math.random() * 4)],
        humidity: Math.floor(Math.random() * 50) + 40,
        timestamp: new Date().toISOString(),
      };
      
      return {
        content: [
          {
            type: "text",
            text: `${args.location} 的天氣:\n溫度: ${weatherData.temperature}°C\n狀況: ${weatherData.condition}\n濕度: ${weatherData.humidity}%\n更新時間: ${weatherData.timestamp}`,
          },
        ],
      };
    }

    throw new Error(`未知工具: ${name}`);
  } catch (error) {
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

// 啟動服務器
async function main() {
  const transport = new StdioServerTransport();
  await server.connect(transport);
  console.error("Demo MCP Server 已啟動 - 提供以下工具:");
  console.error("  1. get_project_info - 獲取項目信息");
  console.error("  2. calculate - 執行數學計算");
  console.error("  3. get_weather - 獲取天氣信息");
}

main().catch((error) => {
  console.error("服務器錯誤:", error);
  process.exit(1);
});
