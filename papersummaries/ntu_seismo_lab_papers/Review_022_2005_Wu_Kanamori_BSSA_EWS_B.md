# [Review] 利用 P 波初期資訊快速評估台灣地震災害潛勢 (2005)

## 📌 原始文獻資訊
- **標題**: Rapid Assessment of Damage Potential of Earthquakes in Taiwan from the Beginning of P Waves
- **作者**: Yih-Min Wu and Hiroo Kanamori
- **期刊**: *Bulletin of the Seismological Society of America (BSSA)*
- **年份**: 2005

## 📖 內容摘要
這是 Wu & Kanamori (2005) 系列研究的第二部分，進一步驗證了 P 波參數在災損評估上的應用。

### 研究亮點：
1.  **Pd 與 PGV 的關聯**：證實了 P 波前 3 秒的位移幅值 (Pd) 與該測站後續紀錄到的最大地動速度 (PGV) 有高度正相關。由於 PGV 是評估建物損害的最佳指標，這意味著 Pd 可以直接作為災損的代理指標。
2.  **綜合指標 ($\tau_c \times Pd$)**：提出結合週期參數與幅值參數 ($\tau_c \times Pd$)，能更穩健地篩選出具破壞性的地震事件，降低誤報率。
3.  **實務門檻**：建議當 Pd > 0.5 cm 時，應立即發布警報。

## 🎓 專業解說與研究建議
- **物理意義**：$\tau_c$ 代表地震的「規模潛力」，Pd 代表「距離效應」。兩者結合，基本上就在沒有求出震央與規模的情況下，隱含了 Source 與 Path 的資訊。
- **演算法的簡潔美**：這個方法的計算極為簡單，甚至可以在微處理器 (MCU) 上執行，這直接促成了後來單晶片地震預警感測器的誕生。

---
*Reviewed by SeismoProphet on 2026-02-05*
