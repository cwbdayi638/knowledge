# 論文摘要：202_2022_Wang_et_al_SRL.pdf

## 1. 基礎資訊
- **檔案名稱**: 202_2022_Wang_et_al_SRL.pdf
- **原始連結**: http://seismology.gl.ntu.edu.tw/papers/202_2022_Wang_et_al_SRL.pdf

## 2. 內容摘錄 (第一頁)
```text
Using LSTM Neural Networks for Onsite
Earthquake Early Warning
Chia-Yu Wang1 , Ting-Chung Huang*1 , and Yih-Min Wu1,2,3

Abstract
Onsite earthquake early warning (EEW) systems determine possible destructive S
waves solely from initial P waves and issue alarms before heavy shaking begins.
Onsite EEW plays a crucial role in filling in the blank of the blind zone near the epicenter,
which often suffers the most from disastrous ground shaking. Previous studies suggest
that the peak P-wave displacement amplitude (P d ) may serve as a possible indicator of
destructive earthquakes. However, the attempt to use a single indicator with fixed
thresholds suffers from inevitable errors because the diversity in travel paths and site
effects for different stations introduces complex nonlinearities. In addition, the short
warning time poses a threat to the validity of EEW. To conquer the aforementioned
problems, this study presents a deep learning approach employing long short-term
memory (LSTM) neural networks, which can produce a highly nonlinear neural network
and derive an alert probability at every time step. The proposed LSTM neural network is
then tested with two major earthquake events and one moderate earthquake event
that occurred recently in Taiwan, yielding the results of a missed alarm rate of 0%
and a false alarm rate of 2.01%. This study demonstrates promising outcomes in both
missed alarms and false alarms reduction. Moreover, the proposed model provides an
adequate warning time for emergency response.

Introduction
Destructive earthquake events have continuously caused severe
loss of human lives and property. With studies showing the
probable inherent unpredictability of earthquakes (Geller,
1997), reliable short-term earthquake prediction remains
impractical (Kanamori et al., 1997). The urgent need for seismic hazard mitigation thus demands an alternative approach.
These circumstances encourage the development of earthquake
early warning (EEW) systems.
An EEW system delivers ground-shaking alerts after an
earthquake has nucleated. These alerts may provide crucial
warning time for hazard mitigation procedures to be carried
out, making it possible to avert human casualties and economic
losses. In this section, the history of the development of EEW
systems are reviewed. Next, we provide a detailed examination
of the conceptual difference between regional EEW and onsite
EEW.
In Taiwan, the idea for EEW system implementation came
after an M w  7:4 (from the U.S. Geological Survey database)
earthquake in 1986. Although the epicenter was located offshore of Hualien, the most severe damage occurred in Taipei,
approximately 120 km away (Wu et al., 1999). In 1994, the
Central Weather Bureau (CWB) of Taiwan started the operation of a prototype EEW system around Hualien. The station
signals were processed in real time, and the results were
814

Seismological Research Letters

Downloaded from http://pubs.geoscienceworld.org/ssa/srl/article-pdf/93/2A/814/55
```

---
*自動生成日期: 2026-02-04*
