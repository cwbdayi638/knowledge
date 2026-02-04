# 論文摘要：2024 年台灣花蓮 ML 7.2 地震中 FinDer、VS 與 eBEAR 系統的預警表現

## 1. 基礎資訊
- **標題**: Early Warning Performance of FinDer, Virtual Seismologist, and eBEAR Systems in the 2024 ML 7.2 Hualien, Taiwan, Earthquake
- **作者**: Guan-Yi Song, Da-Yi Chen, Yih-Min Wu, et al.
- **年份**: 2025
- **期刊**: Seismological Research Letters (SRL)
- **DOI**: 10.1785/0220250187

## 2. 研究核心內容
本研究分析了台灣中央氣象署 (CWA) 在 2024 年 4 月 3 日花蓮地震中，三種地震預警 (EEW) 系統的實戰表現。

### (1) 系統對比
- **eBEAR (Earthworm-Based Earthquake Alarm Reporting)**: 
    - **原理**: 點源模型 (Point-source)。
    - **實戰**: 初始警報漏報了台北等 5 個高人口密度區域。隨後 CWA 將規模更新閾值從 0.5 降至 0.1 以提升靈敏度。
- **FinDer (Finite-fault rupture Detector)**: 
    - **原理**: 線源/有限斷層模型 (Line-source/Finite-fault)。
    - **實戰**: **表現最優**。準確捕捉斷層破裂幾何，地動強度預測精度最高，空間覆蓋範圍最廣。
- **VS (Virtual Seismologist)**: 
    - **原理**: 基於貝氏機率的點源模型。
    - **實戰**: 修正配置後表現與 eBEAR 相似，驗證了點源模型在面對巨型斷層破裂時的共同局限。

## 3. 關鍵觀測數據 (403 花蓮地震)
- **最大 PGA**: 1102 cm/s² (ETL 太魯閣站)。
- **最大 PGV**: 84 cm/s (EHP 和平站)。
- **震度指標**: 建築物損害與傷亡高度集中在 PGV 指標達震度 5 弱以上區域，證明了 CWA 2020 年震度新制（高震度改用 PGV）的有效性。

## 4. 結論與應用建議
- **單一模型限制**: 單純依賴點源模型會導致大型地震（有限破裂）的嚴重漏報。
- **混合策略**: 強烈建議將快速反應的點源模型與能即時估算斷層幾何的線源模型 (如 FinDer) 整合。
- **系統演進**: 此研究為台灣未來提升 PWS 警報精確度提供了重要的技術路徑。

---
*整理日期: 2026-02-03*
