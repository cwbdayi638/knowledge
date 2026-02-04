import os
import sys
from obspy import UTCDateTime
from obspy.clients.fdsn import Client
import matplotlib.pyplot as plt

def fetch_and_plot():
    # 1. 設定參數
    client = Client("IRIS")
    net = "TW"
    sta = "NACB"
    loc = ""
    chan = "BHZ"
    
    # 2. 設定時間範圍：距今 10 分鐘前到現在
    now = UTCDateTime.now()
    starttime = now - 600  # 10 分鐘 = 600 秒
    endtime = now
    
    print(f"正在從 IRIS 抓取資料...")
    print(f"測站: {net}.{sta}.{loc}.{chan}")
    print(f"時間範圍: {starttime} 至 {endtime}")

    try:
        # 3. 抓取波形資料
        st = client.get_waveforms(net, sta, loc, chan, starttime, endtime)
        
        # 4. 基本處理 (去趨勢、去直流)
        st.detrend("demean")
        st.detrend("linear")
        
        # 5. 畫圖
        # 儲存成圖片以便在 Canvas 或其他地方查看
        output_file = "nacb_waveform.png"
        st.plot(outfile=output_file)
        
        print(f"成功！波形圖已儲存為: {output_file}")
        
        # 如果在有顯示介面的環境，可以直接 show
        # plt.show()
        
    except Exception as e:
        print(f"抓取失敗: {e}")

if __name__ == "__main__":
    fetch_and_plot()
