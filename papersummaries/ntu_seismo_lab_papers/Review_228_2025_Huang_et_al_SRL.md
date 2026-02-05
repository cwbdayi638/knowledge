# [Review] 228_2025_Huang_et_al_SRL

## 📌 原始文獻資訊
- **檔案名稱**: 228_2025_Huang_et_al_SRL.md
- **年份**: 2025

## 📖 研究摘要

### 主要研究內容：
1. **研究主題**: 本研究探討地震相關議題
2. **研究方法**: 採用地震學分析方法
3. **重要發現**: 提供對區域地震特性的新認識

## 🎯 研究價值與建議

### 學術貢獻：
- 為地震研究領域提供新的數據與分析
- 深化對地震物理機制的理解
- 可作為後續研究的重要參考

### 應用價值：
- 對地震預警系統具有參考價值
- 有助於改善地震監測技術
- 可應用於地震災害風險評估

### 研究建議：
- 建議後續研究可擴展至更大範圍的數據集
- 可結合其他觀測技術進行交叉驗證
- 值得探討方法在其他地區的適用性

## 📊 原始內容摘錄

## 2. 內容摘錄 (第一頁)
```text
Attention-Based Neural Network for
Onsite Peak Ground Velocity Earthquake
Early Warning
Ting-Chung Huang*1 , Tzu-Ling Liu1, Benjamin Ming Yang1 , and Yih-Min Wu1,2

Abstract
To improve on-site earthquake early warning for peak ground velocity (PGV), we leverage a machine learning approach. We propose a novel attention-based transformer
architecture to address this challenging problem. A series of comparisons with other
methods, including the traditional peak P-wave displacement amplitude approach
and long short-term memory neural networks, is conducted. In addition, we demonstrate that the influence of building effects can be mitigated by incorporating station
corrections to peak values in the seismograms as additional features during training.
Finally, we discuss how the shape of the label can serve as a proxy to indicate the reliability of PGV determination within the first few seconds after the arrival time.

Introduction
Earthquake early warning (EEW) relies on the speed difference
between P waves and S waves (V P > V S ) to deliver warnings of
destructive earthquakes before significant ground motion
occurs. In practice, to maximize warning time and enhance
effectiveness, EEW systems must determine whether an earthquake is destructive within the first few seconds (Wu and
Kanamori, 2005). This quasi-deterministic approach, which
involves assessing the earthquake’s destructiveness based on
the initial behavior of ground motion, has been widely adopted.
The parameters used for estimation may include magnitude
(Wu and Zhao, 2006), peak ground acceleration (PGA), or peak
ground velocity (PGV) (Chandrakumar et al., 2024).
There are two types of EEW systems: regional EEW and
onsite EEW. Regional EEW uses ground-motion data from
stations near the hypocenter to estimate key earthquake
parameters, including the earthquake’s location and magnitude. After determining these parameters, the regional EEW
takes advantage of the fact that internet transmission speeds
are much faster than the speeds of P waves and S waves
(V internet ≫ V P > V S ), enabling it to deliver warnings to
regions before the arrival of the largest seismic wave.
Regional EEW systems are highly reliable, with both low
false alarm rates and low missed alarm rates. There are several
operating regional EEW around the world, for example, in
Japan (Kamigaichi et al., 2009) and Mexico (Vaiciulyte
et al., 2024). However, regional EEW systems have a significant
limitation: they require seismic data from multiple stations,
and collecting these data take time. In addition, processing
the data to estimate parameters and broadcasting warnings
also requires time. As a result, issuing a regional warning
Volume XX

•

Number XX

•

– 2025

•

Cite this article as Huang, T.-C.,
T.-L. Liu, B. Ming Yang, and Y.-M. Wu
(2025). Attention-Based Neural Network
for Onsite Peak Ground Velocity
Earthquake Early Warning, Seismol. Res.
Lett. XX, 1–16, doi: 10.1785/
0220240496.

typically takes ∼10–20 s, depending
```

---
*自動生成日期: 2026-02-04*


---
*Reviewed on 2026-02-05*
