# 論文摘要：利用機器學習與震源時間函數分析地震初始與規模之相關性

## 1. 基礎資訊
- **標題**: Analyzing Earthquake’s Onset-Magnitude Correlation Using Modeled Source Time Functions of Recorded Earthquakes and Machine Learning
- **作者**: Gopala Krishna Rodda and Yuval Tal
- **年份**: 2025 (Published Online Dec 5)
- **期刊**: Seismological Research Letters (SRL)
- **DOI**: 10.1785/0220240161

## 2. 研究核心問題
地震物理學與預警系統中一個懸而未決的核心問題：**能否從地震初期的破裂特徵預測其最終規模？** 過去的研究對此存有分歧（確定論 vs. 隨機論）。

## 3. 研究方法 (Methodology)
- **模型架構**: 採用混合型 **CNN-RNN** (卷積神經網路 - 遞迴神經網路) 模型。
- **數據來源**: 使用 USGS 數據庫中 228 個地震事件，透過「有限斷層反演」獲得的**震源時間函數 (Source Time Functions, STFs)**。
- **特徵提取**: 僅分析地震發生後前 **2 秒** 的 STF 訊號。
- **目標**: 預測地震的地震矩規模 ($)。

## 4. 關鍵結果與發現
- **預測表現**: 
    - 相關係數 (Correlation Coefficient) 達 **0.71**。
    - 平均絕對誤差 (MAE) 僅 **0.21** 規模單位。
    - 測試集規模主要集中在 $ 6.75 至 8.25 之間。
- **時間窗口**: 分析顯示，**2 秒** 的 STF 窗口已足以讓模型捕捉到與最終規模相關的關鍵特徵。
- **結論**: 研究結果支持「地震初期階段與最終大小之間存在某種複雜關聯」的觀點。

## 5. 科研意義與應用
- **地震預警 (EEW)**: 若能在破裂前 2 秒即初步判定其為強震，將能大幅增加預警的黃金時間。
- **未來方向**: 需進一步研究更廣泛的規模範圍，並減少震源反演過程中可能引入的人為產物 (artifacts)，以提升預測的可靠性。

---
*整理日期: 2026-02-04*
