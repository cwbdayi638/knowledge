# 論文摘要：228_2025_Huang_et_al_SRL.pdf

## 1. 基礎資訊
- **檔案名稱**: 228_2025_Huang_et_al_SRL.pdf
- **原始連結**: http://seismology.gl.ntu.edu.tw/papers/228_2025_Huang_et_al_SRL.pdf

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
