# 論文摘要：208_2022_Liao_et_al_IEEE.pdf

## 1. 基礎資訊
- **檔案名稱**: 208_2022_Liao_et_al_IEEE.pdf
- **原始連結**: http://seismology.gl.ntu.edu.tw/papers/208_2022_Liao_et_al_IEEE.pdf

## 2. 內容摘錄 (第一頁)
```text
IEEE TRANSACTIONS ON GEOSCIENCE AND REMOTE SENSING, VOL. 60, 2022

2900111

RED-PAN: Real-Time Earthquake Detection and
Phase-Picking With Multitask Attention Network
Wu-Yu Liao, En-Jui Lee , Da-Yi Chen, Po Chen, Dawei Mu, and Yih-Min Wu

1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32

Abstract— In this article, we show that the real-time
earthquake detection and phase picking with multitask attention
network (RED-PAN) can carry out earthquake detection
and seismic phase picking on real-time and continuous data
with appropriate data augmentation. Goal-oriented data
augmentations materialize the capability of RED-PAN. Mosaic
waveform augmentation (MWA) synthesizes data conditioned by
superimposed earthquake waveforms, marching MWA (MMWA)
extends MWA to allow the dynamic input of seismograms, and
earthquake early warning augmentation (EEWA) enables to
identify P arrivals using the early part of P-wave waveforms. For
stable P and S arrival probability distribution functions (pdfs) of
continuous recordings, we use the median values of phase predictions at each time point until the model scans through, which we
term the seismogram-tracking median filter (STMF). For realtime P arrival detection, we use a threshold (0.3) on the real-time
P arrival pdf as the trigger criterion. We examined our proposed
strategy in different application scenarios. For the dataset of
the fixed-length samples, our RED-PAN(60 s) model performs
similar to EQTransformer (EqT) on the STanford EArthquake
Dataset (STEAD) and outperforms the Taiwan dataset. For
continuous data examination of the 2019 Ridgecrest earthquake
sequence, the number of earthquake waveforms detected by our
RED-PAN(60 s) model is 2.7 times the number of EqT under the
same receptive field (60-s-long seismogram). In the application
of earthquake early warning (EEW), our RED-PAN(60 s) model
only requires the P-wave waveform about 0.13 s long from
the P-alert and 0.09 s long from the Taiwan Strong Motion
Instrumentation Program (TSMIP) network. The source code is
available at https://github.com/tso1257771/RED-PAN.
Index Terms— Data augmentation, multitask learning (MTL),
real-time earthquake monitoring.
Manuscript received 1 January 2022; revised 6 May 2022 and
1 August 2022; accepted 28 August 2022. Date of publication 8 September
2022; date of current version 27 September 2022. The work of Wu-Yu Liao
was supported in part by the Science College of National Cheng Kung
University (NCKU Science); and in part by the Ministry of Science and
Technology (MOST), Taiwan, under Contract MOST 109-2116-M-006-016.
The work of En-Jui Lee was supported by the Ministry of Science and
Technology, China, under Contract MOST 109-2116-M-006-016. The work
of Po Chen was supported in part by the Nielson Energy Fellowship provided
by the School of Energy Resources, University of Wyoming. This work
was supported in part by the National Science Foundation’s Major Research
Instrumentation progr
```

---
*自動生成日期: 2026-02-04*
