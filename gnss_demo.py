import numpy as np

def demo_pwv_calculation():
    print("--- GNSS 氣象學：可降水量 (PWV) 計算演示 ---")
    
    # 模擬輸入參數 (從 RINEX 觀測值處理後獲得)
    ztd = 2.450  # 天頂總延遲 (Zenith Total Delay), 單位: 公尺
    
    # 1. 計算天頂乾延遲 (Zenith Hydrostatic Delay, ZHD)
    # 通常利用 Saastamoinen 模型，依賴地面氣壓 (P)
    pressure = 1013.25  # 模擬氣壓 (hPa)
    latitude = 23.5     # 模擬緯度 (度)
    height = 100.0      # 模擬測站高度 (公尺)
    
    # 簡化公式：ZHD = 0.0022768 * P / (1 - 0.00266 * cos(2*lat) - 0.00028 * H/1000)
    lat_rad = np.radians(latitude)
    zhd = (0.0022768 * pressure) / (1 - 0.00266 * np.cos(2 * lat_rad) - 0.00028 * height / 1000)
    
    # 2. 提取天頂濕延遲 (Zenith Wet Delay, ZWD)
    zwd = ztd - zhd
    
    # 3. 轉換為可降水量 (Precipitable Water Vapor, PWV)
    # PWV = PI * ZWD
    # PI 是一個無因次轉換係數，通常約在 0.15 左右，取決於大氣平均溫度
    pi_factor = 0.162
    pwv = zwd * pi_factor * 1000  # 換算為 mm
    
    print(f"輸入 ZTD: {ztd:.3f} m")
    print(f"計算 ZHD: {zhd:.3f} m (基於氣壓 {pressure} hPa)")
    print(f"提取 ZWD: {zwd:.3f} m")
    print(f"最終 PWV: {pwv:.2f} mm")
    
    # 預報邏輯模擬
    if pwv > 50:
        print("\n[預警系統]: PWV 數值極高 ({:.2f} mm)，降雨機率顯著增加！".format(pwv))
    else:
        print("\n[預警系統]: 目前水氣狀態穩定。")

if __name__ == "__main__":
    demo_pwv_calculation()
