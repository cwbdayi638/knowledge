import gradio as gr
import numpy as np

def calculate_pwv(ztd, pressure, latitude, height):
    # 1. 計算天頂乾延遲 (ZHD)
    lat_rad = np.radians(latitude)
    zhd = (0.0022768 * pressure) / (1 - 0.00266 * np.cos(2 * lat_rad) - 0.00028 * height / 1000)
    
    # 2. 提取天頂濕延遲 (ZWD)
    zwd = ztd - zhd
    
    # 3. 轉換為可降水量 (PWV)
    # 這裡使用一個通用的轉換係數 PI ~ 0.16
    pi_factor = 0.162
    pwv = zwd * pi_factor * 1000  # 換算為 mm
    
    # 預報邏輯
    status = "穩定"
    if pwv > 50:
        status = "⚠️ 降雨風險極高 (PWV > 50mm)"
    elif pwv > 35:
        status = "🟡 水氣充足，注意天氣變化"
        
    return f"{zhd:.4f} m", f"{zwd:.4f} m", f"{pwv:.2f} mm", status

# Gradio 介面設定
with gr.Blocks(title="GNSS 降雨預報模擬器") as demo:
    gr.Markdown("# 🛰️ GNSS 降雨預報模擬器 (PWV Estimator)")
    gr.Markdown("本程式演示如何利用 GNSS 天頂總延遲 (ZTD) 與氣象參數估算可降水量 (PWV) 並進行簡易預報。")
    
    with gr.Row():
        with gr.Column():
            ztd_input = gr.Number(label="天頂總延遲 ZTD (m)", value=2.450)
            p_input = gr.Number(label="地面氣壓 Pressure (hPa)", value=1013.25)
            lat_input = gr.Slider(label="測站緯度 Latitude (deg)", minimum=0, maximum=90, value=23.5)
            h_input = gr.Number(label="測站高度 Height (m)", value=100.0)
            btn = gr.Button("開始計算", variant="primary")
            
        with gr.Column():
            zhd_out = gr.Textbox(label="計算出的乾延遲 (ZHD)")
            zwd_out = gr.Textbox(label="提取出的濕延遲 (ZWD)")
            pwv_out = gr.Textbox(label="估計可降水量 (PWV)")
            result_out = gr.Textbox(label="預報狀態建議")

    btn.click(
        fn=calculate_pwv,
        inputs=[ztd_input, p_input, lat_input, h_input],
        outputs=[zhd_out, zwd_out, pwv_out, result_out]
    )

    gr.Markdown("---")
    gr.Markdown("### 📖 技術說明\n1. **ZHD**: 基於 Saastamoinen 模型。\n2. **ZWD**: 總延遲減去乾延遲。\n3. **PWV**: 濕延遲乘以轉換係數，代表大氣中的總水氣含量。")

if __name__ == "__main__":
    demo.launch()
