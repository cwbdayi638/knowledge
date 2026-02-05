# [Review] 台灣地震預警系統的技術現況 (2007)

## 📌 原始文獻資訊
- **標題**: State of the Art and Progress in the Earthquake Early Warning System in Taiwan
- **作者**: Yih-Min Wu, Nai-Chi Hsiao, William H.K. Lee, Ta-liang Teng, and Tzay-Chyn Shin
- **來源**: *Earthquake Early Warning Systems (Springer)*
- **年份**: 2007

## 📖 內容摘要
本文綜述了截至 2007 年，台灣中央氣象局 (CWB) 在地震預警系統開發上的最新進展。

### 技術里程碑：
1.  **區域型預警 (Regional EWS)**：利用「虛擬子網」技術，已將地震速報時間穩定縮短至 **30 秒** 內（平均 22 秒）。
    -   **預警效益**：對於距離震央 100 公里以外的城市，可提供超過 10 秒的預警時間。
    -   **限制**：對於震央 70 公里內的區域（往往是重災區），仍無法提供有效預警（盲區問題）。
2.  **現地型預警 (On-site EWS)**：
    -   為了突破盲區限制，引入了 $\tau_c$ 與 $P_d$ 方法。
    -   實驗顯示，利用 P 波前 3 秒資訊，可在地震發生後 **10 秒** 內發出警報，這對盲區內的減災至關重要。

## 🎓 專業解說與研究建議
- **混合式系統 (Hybrid System)**：台灣是全球最早倡導結合「區域型」準確度與「現地型」速度的國家。這種混合架構現在已成為國際主流（如日本 REIS, 美國 ShakeAlert）。
- **通訊延遲的挑戰**：文中提到 30 秒的延遲中，有一大部分來自數據傳輸。這提示了未來 5G/6G 低延遲通訊技術在防災上的應用潛力。

---
*Reviewed by SeismoProphet on 2026-02-05*
