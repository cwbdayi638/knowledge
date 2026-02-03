# 利用 GNSS 資料進行降雨預報研究 (GNSS Meteorology)

## 1. 基本原理：大氣延遲 (Atmospheric Delay)
GNSS 衛星訊號穿過地球大氣層時，會受到電離層與中性大氣（對流層）的延遲。
- **對流層延遲 (Tropospheric Delay):** 可分為乾延遲 (ZHD) 與濕延遲 (ZWD)。
- **天頂總延遲 (Zenith Total Delay, ZTD):**  = ZHD + ZWD$。
- **可降水量 (Precipitable Water Vapor, PWV):** 濕延遲 (ZWD) 與大氣中的水氣含量呈高度正相關。透過公式轉換，可從 ZWD 估算出垂直柱狀水氣含量 (PWV)。

## 2. 降雨預報的關鍵指標
研究顯示，降雨發生前通常伴隨著 PWV 的顯著變化：
- **PWV 絕對值:** 超過特定閾值（如 50-60mm，視地區而定）代表水氣充足。
- **PWV 變化率:** PWV 在短時間內迅速攀升（如 2 小時內增加超過 5mm），是強降雨（特別是午後雷陣雨或對流性降雨）的重要前兆指標。
- **PWV 下降:** 降雨開始後，PWV 通常會因凝結降落而迅速下降。

## 3. 進階技術：GNSS 斷層掃描 (GNSS Tomography)
利用一個區域內多個 GNSS 測站的斜距延遲 (Slant Path Delay)，可以像醫學 CT 掃描一樣，重建出大氣水氣的三維空間分佈。這能幫助氣象學家掌握水氣在不同高度層的輸送狀況。

## 4. 在台灣的研究與應用
台灣擁有極高密度的 GNSS 觀測網（如 CWA 與內政部的 e-GNSS）：
- **短期預報整合:** 將即時 PWV 資料納入數值天氣預報模式 (NWP)，能顯著改善短時強降雨 (Nowcasting) 的準確度。
- **機器學習應用:** 結合 GNSS PWV、地面氣象站資料（溫、壓、濕）與雷達回波，利用神經網路模型預測未來 1-6 小時的降雨機率。

## 5. 優勢與挑戰
- **優勢:** 高時間解析度（可達每秒或每分鐘）、全天候監測、低成本（利用現有地殼變動監測網）。
- **挑戰:** ZWD 提取過程依賴精確的氣壓觀測；垂直空間解析度仍有提升空間。

---
*參考文獻建議：*
- *Bevis et al. (1992): GPS Meteorology: Remote Sensing of Atmospheric Water Vapor Using the Global Positioning System.*
- *Guerova et al. (2016): Review of the GNSS meteorology: from technical aspects to applications.*

## 6. 研究需要的資料類型：RINEX Raw Data
要進行 GNSS 氣象學研究，最核心的資料是 **RINEX (Receiver Independent Exchange Format)** 原始觀測檔。
- **內容:** 包含偽距 (Pseudorange)、載波相位 (Carrier Phase) 與 訊噪比 (S/N)。
- **版本:** 目前主流為 RINEX 3.x 或 2.x。
- **獲取方式:** 
  - 台灣: CWA (中央氣象署) 或 內政部地政司的基準站資料。
  - 全球: IGS (International GNSS Service) 公開數據庫。

## 7. 計算邏輯示範 (Python)
以下是一個簡化的 PWV 計算流程演示：
```python
# 核心步驟：從 ZTD 提取 PWV
ZWD = ZTD - ZHD  # 總延遲減去乾延遲
PWV = PI * ZWD    # 濕延遲乘以轉換係數
```
*(完整演示腳本請見工作區範例)*
