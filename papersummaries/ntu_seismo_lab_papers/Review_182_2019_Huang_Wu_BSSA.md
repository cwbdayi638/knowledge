# [Review] 182_2019_Huang_Wu_BSSA

## 📌 原始文獻資訊
- **檔案名稱**: 182_2019_Huang_Wu_BSSA.md
- **作者**: Ting-Chung Huang* and Yih-Min Wu
- **期刊**: Bulletin of the Seismological Society of America
- **年份**: 2019

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
Bulletin of the Seismological Society of America, Vol. 109, No. 1, pp. 413–423, February 2019, doi: 10.1785/0120180127

A Robust Algorithm for Automatic P-wave Arrival-Time
Picking Based on the Local Extrema Scalogram
by Ting-Chung Huang* and Yih-Min Wu

Abstract

A robust algorithm has been developed for the automatic picking of
P-wave arrival times. Owing to the properties of the local extrema scalogram (LES),
this algorithm finds all significant quasi-periodic peaks and valleys without selecting a
specific frequency. Consequently, the P-wave arrival times can be accurately derived
from the peaks and valleys of the seismic signal. A comparison of the proposed algorithm with the common short-term average/long-term average (STA/LTA) method and
the Akaike information criterion (AIC) method is conducted using real data. The results
show that our method consistently outperforms both methods, especially when substantial noise is present.

Introduction
The short-term average/long-term average (STA/LTA)
method (Allen, 1978, 1982) has achieved remarkable success
in automatically identifying P-wave arrivals in real-time scenarios situated within a quiet environment. In this approach,
a characteristic function (CF) is first defined, after which
the STA/LTA ratio is calculated. If this ratio exceeds a predefined threshold, the time will be designated as a picked
P-wave arrival. STA/LTA is computational cost-effective due
to its memoryless design, which will not look back to previous window, and best suited in the real-time detection. A
few seconds of P-wave signal is all it needs to trigger a pick.
However, some difficulties are encountered during the application of this method. First, it is limited by its one-way
design for differentiating true signals from noise. As a consequence of this flaw, the STA/LTA ratio will be triggered by
false fluctuations in some cases, thereby providing erroneous
arrival times. Second, an excessive number of free parameters are available for selection. In his original paper, Allen
(1978) presented a total of five parameters, and many more
parameters appeared in recent variations of the STA/LTA
method. This reflects the fact that higher order details of the
CF require additional parameters. Moreover, in addition to
the number of parameters, the meaning of each parameter
provides another level of complexity; although the parameters are defined explicitly, it is not easy to discern their physical meanings.
The Akaike information criterion (AIC; Akaike, 1973;
Sleeman and van Eck, 1999) constitutes another commonly

used picking approach. Although the AIC approach is capable
of demonstrating good results, it often provides highly erroneous picks. Consequently, in practice, one often determines
effective windows either by hand or by an automated method
to ensure that the AIC technique outputs the correct result.
Many approaches have been proposed based on the
above-mentioned principles to resolve problems associated
with the picki
```

---
*自動生成日期: 2026-02-04*


---
*Reviewed on 2026-02-05*
