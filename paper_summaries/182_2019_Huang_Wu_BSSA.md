# 論文摘要：182_2019_Huang_Wu_BSSA.pdf

## 1. 基礎資訊
- **檔案名稱**: 182_2019_Huang_Wu_BSSA.pdf
- **原始連結**: http://seismology.gl.ntu.edu.tw/papers/182_2019_Huang_Wu_BSSA.pdf

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
