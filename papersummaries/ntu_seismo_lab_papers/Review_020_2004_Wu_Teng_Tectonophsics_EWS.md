# [Review] 大地殼地震的即時規模測定 (2004)

## 📌 原始文獻資訊
- **標題**: Near real-time magnitude determination for large crustal earthquakes
- **作者**: Yih-Min Wu and Ta-liang Teng
- **期刊**: *Tectonophysics*
- **年份**: 2004

## 📖 內容摘要
針對大型地殼地震（ML > 6.5），傳統的規模計算方法常因儀器飽和或頻寬限制而失真。本文提出了一種基於 **加速度紀錄積分 (Time Integration)** 的經驗方法，用於快速估算地震矩規模 (Mw)。

### 技術方法：
1.  **總有效震動 (Total Effective Shaking)**：對強震站的三分量加速度紀錄取絕對值後進行時間積分，定義為「總有效震動」能量指標。
2.  **經驗公式**：利用台灣多次大地震的資料，建立了該指標與 Mw 之間的迴歸關係。
3.  **優勢**：此方法不需等待完整的波形記錄，且加速度計不易飽和，特別適合用於即時速報 (Rapid Reporting) 與早期預警 (EWS)。

## 🎓 專業解說與研究建議
- **解決規模飽和 (Magnitude Saturation)**：這是地震預警技術的一大突破。傳統 ML 在規模大於 7.0 時會飽和（無法區分 7.3 與 7.6 的差別），而此積分方法能更線性地反映地震能量。
- **防災應用的實用性**：對於防災單位而言，Mw 比 ML 更能代表災害潛勢。此算法的低運算成本使其非常適合植入於現地型預警裝置中。

---
*Reviewed by SeismoProphet on 2026-02-05*
