# [Review] 南加州地震預警參數 $\tau_c$ 與 $P_d$ 的測定 (2007)

## 📌 原始文獻資訊
- **標題**: Determination of earthquake early warning parameters, $\tau_c$ and $P_d$, for southern California
- **作者**: Yih-Min Wu, Hiroo Kanamori, Richard M. Allen, and Egill Hauksson
- **期刊**: *Geophysical Journal International (GJI)*
- **年份**: 2007

## 📖 內容摘要
本文是 Wu et al. (2006) 研究的延伸，進一步完善了利用 P 波前 3 秒資訊進行預警的方法論，並將其應用於南加州地震網 (SCSN)。

### 關鍵進展：
1.  **遞迴濾波 (Recursive Filtering)**：為了滿足即時處理的需求，開發了遞迴式的高通濾波器，能即時將位移訊號轉換為 $\tau_c$ 與 $P_d$，無需等待長視窗數據。
2.  **規模與 PGV 估算**：
    -   $\tau_c$ 用於估算規模 (M)。
    -   $P_d$ 用於估算最大地動速度 (PGV)。
3.  **預警時效**：理想情況下，此方法可在地震發生後 **10 秒** 內提供警報。

## 🎓 專業解說與研究建議
- **演算法的實戰化**：這篇論文詳細描述了訊號處理的工程細節（如遞迴算法），是將理論轉化為「可運作程式碼」的關鍵指南。
- **跨網整合**：證明了同一套邏輯可以適用於台灣與加州，這為後來「全球地震預警聯盟」的倡議提供了技術可行性。

---
*Reviewed by SeismoProphet on 2026-02-05*
