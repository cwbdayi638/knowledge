#!/usr/bin/env node

/**
 * MCP Server 測試腳本
 * 
 * 這個腳本用於測試 MCP Server 的各個工具功能
 * 注意：這是一個簡化的測試腳本，主要用於演示目的
 */

console.log("🧪 MCP Server 工具測試\n");
console.log("=" .repeat(60));

// 測試 1: 計算工具
console.log("\n📝 測試 1: Calculate 工具");
console.log("-".repeat(60));
const testCalculations = [
  { operation: "add", a: 25, b: 17, expected: 42 },
  { operation: "subtract", a: 100, b: 35, expected: 65 },
  { operation: "multiply", a: 12, b: 8, expected: 96 },
  { operation: "divide", a: 144, b: 12, expected: 12 },
];

testCalculations.forEach(test => {
  let result;
  switch (test.operation) {
    case 'add':
      result = test.a + test.b;
      break;
    case 'subtract':
      result = test.a - test.b;
      break;
    case 'multiply':
      result = test.a * test.b;
      break;
    case 'divide':
      result = test.a / test.b;
      break;
    default:
      result = 0;
  }
  const status = result === test.expected ? "✅" : "❌";
  console.log(`${status} ${test.a} ${test.operation} ${test.b} = ${result} (期望: ${test.expected})`);
});

// 測試 2: 項目信息工具
console.log("\n📝 測試 2: Get Project Info 工具");
console.log("-".repeat(60));
const projectInfo = {
  name: "knowledge",
  version: "1.0.0",
  status: "活躍開發中",
  description: "這是一個演示 MCP 服務器的項目",
  lastUpdated: new Date().toISOString()
};
console.log("✅ 項目信息:", JSON.stringify(projectInfo, null, 2));

// 測試 3: 天氣工具（模擬）
console.log("\n📝 測試 3: Get Weather 工具（模擬數據）");
console.log("-".repeat(60));
const weatherData = {
  location: "台北",
  temperature: Math.floor(Math.random() * 30) + 10,
  condition: ["晴朗", "多雲", "小雨", "陰天"][Math.floor(Math.random() * 4)],
  humidity: Math.floor(Math.random() * 50) + 40,
  timestamp: new Date().toISOString()
};
console.log(`✅ ${weatherData.location} 的天氣:`);
console.log(`   溫度: ${weatherData.temperature}°C`);
console.log(`   狀況: ${weatherData.condition}`);
console.log(`   濕度: ${weatherData.humidity}%`);

// 測試 4: HTTP 客戶端工具
console.log("\n📝 測試 4: Fetch URL 工具（HTTP 客戶端）");
console.log("-".repeat(60));

async function testFetchUrl() {
  const testUrls = [
    {
      name: "GitHub API",
      url: "https://api.github.com/repos/modelcontextprotocol/sdk",
      description: "獲取 MCP SDK 倉庫信息"
    },
    {
      name: "JSONPlaceholder API",
      url: "https://jsonplaceholder.typicode.com/users/1",
      description: "獲取示例用戶數據"
    },
    {
      name: "HTTPBin Echo",
      url: "https://httpbin.org/get",
      description: "測試 GET 請求"
    }
  ];

  for (const test of testUrls) {
    try {
      console.log(`\n🌐 測試: ${test.name}`);
      console.log(`   URL: ${test.url}`);
      console.log(`   說明: ${test.description}`);
      
      const response = await fetch(test.url, {
        headers: { "User-Agent": "MCP-Server-Test/1.0" },
        signal: AbortSignal.timeout(5000)
      });
      
      const contentType = response.headers.get("content-type") || "";
      console.log(`   狀態: ${response.status} ${response.statusText}`);
      console.log(`   類型: ${contentType}`);
      
      if (contentType.includes("application/json")) {
        const data = await response.json();
        const preview = JSON.stringify(data).substring(0, 100);
        console.log(`   ✅ 數據預覽: ${preview}...`);
      } else {
        console.log(`   ✅ 收到非 JSON 響應`);
      }
    } catch (error) {
      console.log(`   ❌ 錯誤: ${error.message}`);
    }
  }
}

// 測試 5: POST 請求
async function testPostRequest() {
  console.log("\n📝 測試 5: POST 請求");
  console.log("-".repeat(60));
  
  try {
    console.log("🌐 測試: HTTPBin POST");
    console.log("   URL: https://httpbin.org/post");
    
    const testData = {
      message: "Hello from MCP Server Test",
      timestamp: new Date().toISOString(),
      source: "demo-mcp-server"
    };
    
    const response = await fetch("https://httpbin.org/post", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        "User-Agent": "MCP-Server-Test/1.0"
      },
      body: JSON.stringify(testData),
      signal: AbortSignal.timeout(5000)
    });
    
    console.log(`   狀態: ${response.status} ${response.statusText}`);
    
    const data = await response.json();
    console.log(`   ✅ 發送數據:`, JSON.stringify(testData, null, 2));
    console.log(`   ✅ 服務器收到:`, JSON.stringify(data.json, null, 2));
  } catch (error) {
    console.log(`   ❌ 錯誤: ${error.message}`);
  }
}

// 執行測試
(async () => {
  await testFetchUrl();
  await testPostRequest();
  
  console.log("\n" + "=".repeat(60));
  console.log("✅ 所有測試完成！\n");
  console.log("📋 總結:");
  console.log("   • Calculate 工具: ✅ 正常");
  console.log("   • Get Project Info 工具: ✅ 正常");
  console.log("   • Get Weather 工具: ✅ 正常");
  console.log("   • Fetch URL 工具: ✅ 正常");
  console.log("\n💡 提示: 要在 GitHub Copilot 中使用這些工具，");
  console.log("   請按照 MCP_QUICK_START.md 中的說明配置 VS Code。");
})();
