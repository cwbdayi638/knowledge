# 教學提案：以「反重力」概念啟發地震學編程與研究
# Teaching Proposal: Using "Antigravity" Concepts to Inspire Seismology Coding and Research

## 📋 提案概要 | Executive Summary

本提案旨在建立一套創新的地震學教育框架，透過「反重力」(Antigravity) 的類比思維，將抽象的地球物理概念轉化為具體的編程實作與研究方法論。我們將重力場的反轉概念作為教學隱喻，引導學習者從「顛覆常規」的角度理解地震波傳播、應力應變關係，並培養獨立研究與數據分析能力。

This proposal establishes an innovative seismology education framework using "antigravity" as an analogical thinking tool to transform abstract geophysical concepts into concrete programming implementations and research methodologies. By using the concept of gravitational field inversion as a teaching metaphor, we guide learners to understand seismic wave propagation and stress-strain relationships from a "paradigm-shifting" perspective, cultivating independent research and data analysis capabilities.

---

## 🎯 教學理念 | Educational Philosophy

### 核心概念：反重力思維 (Antigravity Thinking)

1. **反向推理 (Reverse Engineering)**
   - 如同反重力違反常規物理直覺，地震學研究需要從地表觀測「反推」地下結構
   - 訓練學員從測站記錄的地震波形，反演震源機制與速度結構

2. **對稱性與反轉 (Symmetry and Inversion)**
   - 重力向下 ↔ 反重力向上
   - 壓應力 (Compression) ↔ 張應力 (Tension)
   - P波壓縮 ↔ S波剪切
   - 編程思維：正向模擬 ↔ 反向問題求解 (Inverse Problem)

3. **突破框架 (Breaking Paradigms)**
   - 反重力啟發學習者挑戰傳統思維
   - 鼓勵嘗試非線性方法、機器學習等創新技術於地震學研究

---

## 📚 課程模組設計 | Course Module Design

### Module 1: 基礎原理 - 重力與反重力的對話
**Foundation - Dialogue Between Gravity and Antigravity**

#### 學習目標 (Learning Objectives):
- 理解重力場的物理本質與測量方法
- 掌握絕對重力儀 (FG5, A10) 的工作原理
- 學習如何用編程模擬重力異常

#### 課程內容 (Content):

**1.1 重力基礎理論**
```python
# 理論背景：牛頓萬有引力定律
# F = G * (m1 * m2) / r^2
# 地表重力加速度 g ≈ 9.8 m/s²

import numpy as np
import matplotlib.pyplot as plt

def gravitational_acceleration(mass, radius):
    """
    計算球對稱物體表面的重力加速度
    
    Parameters:
    mass: 物體質量 (kg)
    radius: 物體半徑 (m)
    
    Returns:
    g: 表面重力加速度 (m/s²)
    """
    G = 6.67430e-11  # 萬有引力常數 (m³/kg/s²)
    g = G * mass / (radius ** 2)
    return g

# 地球參數
earth_mass = 5.972e24  # kg
earth_radius = 6.371e6  # m

g_earth = gravitational_acceleration(earth_mass, earth_radius)
print(f"地球表面重力加速度: {g_earth:.2f} m/s²")
```

**1.2 反重力思維實作：重力異常反演**
```python
def gravity_anomaly_inversion(observed_gravity, reference_gravity, depth=1000):
    """
    「反重力」概念應用：從重力異常反推地下密度變化
    
    這個函數展示了反向問題 (inverse problem) 的核心思想：
    從地表觀測推斷地下結構
    
    Parameters:
    observed_gravity: 觀測重力值陣列
    reference_gravity: 參考重力值
    depth: 異常體深度 (m)
    
    Returns:
    density_anomaly: 推估的密度異常
    """
    G = 6.67430e-11  # 萬有引力常數
    gravity_residual = observed_gravity - reference_gravity
    
    # 簡化的布格異常反演 (Bouguer anomaly inversion)
    # 實際應用需考慮地形、緯度等校正
    density_anomaly = gravity_residual / (2 * np.pi * G * depth)
    
    return density_anomaly

# 教學重點：
# 1. 正問題 (Forward): 已知密度 → 計算重力
# 2. 反問題 (Inverse): 已知重力 → 推估密度 (反重力思維)
```

#### 實作練習 (Hands-on Exercise):
- **任務**: 模擬斷層附近的重力異常
- **工具**: Python + NumPy + Matplotlib
- **產出**: 視覺化重力場與異常分布圖

---

### Module 2: 波動理論 - 從重力波到地震波
**Wave Theory - From Gravitational Waves to Seismic Waves**

#### 學習目標:
- 區分重力波與地震波的差異
- 理解 P波、S波的物理機制
- 編程實現波動方程數值解

#### 課程內容:

**2.1 波動方程基礎**
```python
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def seismic_wave_simulation(wave_type='P'):
    """
    一維地震波傳播模擬
    
    Parameters:
    wave_type: 'P' (壓縮波) 或 'S' (剪切波)
    
    Returns:
    動畫展示波的傳播過程
    """
    # 物理參數
    length = 1000  # 介質長度 (m)
    dx = 1.0       # 空間步長 (m)
    dt = 0.001     # 時間步長 (s)
    
    # 波速設定
    if wave_type == 'P':
        velocity = 6000  # P波速度 (m/s)
        title = "P Wave (Compression)"
    else:
        velocity = 3500  # S波速度 (m/s)
        title = "S Wave (Shear)"
    
    # 初始化
    x = np.arange(0, length, dx)
    u = np.zeros_like(x)  # 位移場
    v = np.zeros_like(x)  # 速度場
    
    # 震源函數：Ricker wavelet
    def source_function(t, f0=5):
        """Ricker wavelet震源時間函數"""
        t0 = 1.0 / f0
        return (1 - 2 * (np.pi * f0 * (t - t0))**2) * \
               np.exp(-(np.pi * f0 * (t - t0))**2)
    
    # 有限差分法求解波動方程
    # ∂²u/∂t² = c² ∂²u/∂x²
    
    # 需要三個時間層：過去、現在、未來
    u_past = np.zeros_like(x)  # t-1 時刻
    u_now = np.zeros_like(x)   # t 時刻
    u_future = np.zeros_like(x) # t+1 時刻
    
    fig, ax = plt.subplots(figsize=(12, 6))
    line, = ax.plot(x, u_now)
    ax.set_ylim(-1, 1)
    ax.set_xlabel('Distance (m)')
    ax.set_ylabel('Displacement')
    ax.set_title(f'{title} Propagation')
    
    def animate(frame):
        nonlocal u_past, u_now, u_future
        t = frame * dt
        # 更新震源
        source_idx = int(length / (2 * dx))
        u_now[source_idx] += source_function(t) * dt
        
        # 波動方程數值解 (中央差分)
        u_future[1:-1] = 2*u_now[1:-1] - u_past[1:-1] + \
                         (velocity * dt / dx)**2 * (u_now[2:] - 2*u_now[1:-1] + u_now[:-2])
        
        # 更新時間層
        u_past[:] = u_now[:]
        u_now[:] = u_future[:]
        
        line.set_ydata(u_now)
        return line,
    
    anim = FuncAnimation(fig, animate, frames=500, interval=20, blit=True)
    plt.show()
    
    return anim

# 執行模擬
seismic_wave_simulation('P')
seismic_wave_simulation('S')
```

**2.2 反重力視角：波場反傳播**
```python
def reverse_time_migration(seismogram, velocity_model):
    """
    反時偏移 (Reverse Time Migration)：
    將地震波「反向傳播」以成像地下構造
    
    這是「反重力思維」的經典應用：
    時間反轉 → 波場逆向傳播 → 震源定位
    
    Parameters:
    seismogram: 地震記錄
    velocity_model: 速度模型
    
    Returns:
    migrated_image: 偏移成像結果
    
    注意：這是簡化的概念示範程式碼
    實際實現需要學員完成以下函數
    """
    # 概念示範程式碼
    nt, nx = seismogram.shape
    
    # 步驟1: 時間反轉
    reversed_data = seismogram[::-1, :]
    
    # 步驟2: 反向波場延拓
    # TODO: 學員需實現 backward_propagate() 函數
    # 使用波動方程進行反向時間積分
    backward_wavefield = backward_propagate(reversed_data, velocity_model)
    
    # 步驟3: 成像條件 (零時刻疊加)
    # TODO: 學員需實現 apply_imaging_condition() 函數
    # 將正向與反向波場在零時刻交叉相關
    migrated_image = apply_imaging_condition(backward_wavefield)
    
    return migrated_image

def backward_propagate(data, velocity_model):
    """學員實作任務：實現反向波場延拓"""
    # 提示：使用與正向傳播相同的波動方程
    # 但時間方向相反
    pass

def apply_imaging_condition(wavefield):
    """學員實作任務：實現成像條件"""
    # 提示：在時間=0時刻疊加波場
    pass

# 教學重點：
# 反時偏移是地震探勘的核心技術
# 體現了「反重力」概念：逆向推理以解決問題
```

#### 實作練習:
- **任務1**: 實現二維波動方程有限差分解
- **任務2**: 可視化 P波與 S波的傳播差異
- **任務3**: 挑戰題 - 簡化版反時偏移成像

---

### Module 3: 應力應變分析 - 反向力學
**Stress-Strain Analysis - Inverse Mechanics**

#### 學習目標:
- 掌握應力張量與應變張量
- 理解彈性理論與本構關係
- 從觀測資料反推應力狀態

#### 課程內容:

**3.1 應力張量基礎**
```python
import numpy as np

class StressTensor:
    """應力張量類別"""
    
    def __init__(self, sigma_xx, sigma_yy, sigma_zz, 
                 tau_xy, tau_xz, tau_yz):
        """
        初始化應力張量
        
        σ = [σ_xx  τ_xy  τ_xz]
            [τ_xy  σ_yy  τ_yz]
            [τ_xz  τ_yz  σ_zz]
        """
        self.tensor = np.array([
            [sigma_xx, tau_xy, tau_xz],
            [tau_xy, sigma_yy, tau_yz],
            [tau_xz, tau_yz, sigma_zz]
        ])
    
    def principal_stresses(self):
        """
        計算主應力（特徵值）
        
        Returns:
        主應力值及其方向（特徵向量）
        """
        eigenvalues, eigenvectors = np.linalg.eig(self.tensor)
        
        # 排序：σ₁ ≥ σ₂ ≥ σ₃
        idx = eigenvalues.argsort()[::-1]
        principal_stresses = eigenvalues[idx]
        principal_directions = eigenvectors[:, idx]
        
        return principal_stresses, principal_directions
    
    def mohr_circle(self):
        """
        繪製莫爾圓 (Mohr's Circle)
        用於視覺化二維應力狀態
        """
        sigma_1, sigma_2, sigma_3 = self.principal_stresses()[0]
        
        # 繪製莫爾圓
        fig, ax = plt.subplots(figsize=(8, 8))
        
        # 三個圓
        circles = [
            ((sigma_1 + sigma_2)/2, (sigma_1 - sigma_2)/2),
            ((sigma_2 + sigma_3)/2, (sigma_2 - sigma_3)/2),
            ((sigma_1 + sigma_3)/2, (sigma_1 - sigma_3)/2)
        ]
        
        for center, radius in circles:
            circle = plt.Circle((center, 0), radius, fill=False)
            ax.add_patch(circle)
        
        ax.set_aspect('equal')
        ax.axhline(y=0, color='k', linestyle='--', linewidth=0.5)
        ax.axvline(x=0, color='k', linestyle='--', linewidth=0.5)
        ax.set_xlabel('Normal Stress (σ)')
        ax.set_ylabel('Shear Stress (τ)')
        ax.set_title("Mohr's Circle")
        ax.grid(True)
        
        plt.show()

# 範例：地殼應力狀態
stress = StressTensor(
    sigma_xx=100e6,   # Pa (壓應力)
    sigma_yy=80e6,    # Pa
    sigma_zz=120e6,   # Pa (垂直應力最大)
    tau_xy=20e6,      # Pa
    tau_xz=10e6,      # Pa
    tau_yz=15e6       # Pa
)

principal_stresses, directions = stress.principal_stresses()
print(f"最大主應力 σ₁: {principal_stresses[0]/1e6:.2f} MPa")
print(f"中間主應力 σ₂: {principal_stresses[1]/1e6:.2f} MPa")
print(f"最小主應力 σ₃: {principal_stresses[2]/1e6:.2f} MPa")

stress.mohr_circle()
```

**3.2 反重力思維：應力反演**
```python
def focal_mechanism_inversion(first_motion_polarity, station_locations):
    """
    震源機制反演：從初動極性推斷斷層參數
    
    「反重力」應用：從地表觀測反推震源破裂過程
    
    Parameters:
    first_motion_polarity: 各測站 P波初動（上/下）
    station_locations: 測站位置（方位角、離源角）
    
    Returns:
    fault_parameters: 斷層參數（走向、傾角、滑動角）
    
    注意：這是簡化的概念示範
    實際實現需要學員完成極性計算函數
    """
    # 這是一個簡化的概念示範
    # 實際應用需要使用演算法如網格搜尋或遺傳演算法
    
    def compute_polarity(strike, dip, rake, locations):
        """
        學員實作任務：計算理論初動極性
        
        提示：使用震源機制解的輻射模式公式
        需要將測站位置轉換到震源球座標系
        """
        # 簡化示範：隨機返回極性（實際需要正確計算）
        return np.random.choice([1, -1], size=len(locations))
    
    def misfit_function(strike, dip, rake):
        """
        計算理論與觀測初動的誤差
        
        Parameters:
        strike: 走向 (0-360°)
        dip: 傾角 (0-90°)
        rake: 滑動角 (-180-180°)
        
        Returns:
        誤差函數值
        """
        predicted_polarity = compute_polarity(
            strike, dip, rake, station_locations
        )
        misfit = np.sum(predicted_polarity != first_motion_polarity)
        return misfit
    
    # 網格搜尋最佳解
    best_misfit = np.inf
    best_params = None
    
    for strike in range(0, 360, 10):
        for dip in range(0, 91, 10):
            for rake in range(-180, 181, 10):
                misfit = misfit_function(strike, dip, rake)
                if misfit < best_misfit:
                    best_misfit = misfit
                    best_params = (strike, dip, rake)
    
    return best_params

# 教學意義：
# 震源機制解是反問題的典型案例
# 從散布全球的測站觀測，反推震源的應力釋放方式
```

#### 實作練習:
- **任務1**: 實現應力張量的旋轉變換
- **任務2**: 繪製不同應力狀態的莫爾圓
- **任務3**: 進階挑戰 - 震源機制球體投影繪製

---

### Module 4: 數據處理與研究實踐
**Data Processing and Research Practice**

#### 學習目標:
- 掌握真實地震數據的獲取與處理
- 學習科學研究的完整流程
- 培養批判性思維與問題解決能力

#### 課程內容:

**4.1 地震數據獲取**
```python
from obspy import UTCDateTime
from obspy.clients.fdsn import Client

def fetch_seismic_data(network, station, starttime, duration):
    """
    從 IRIS 數據中心下載地震數據
    
    Parameters:
    network: 台網代碼（如 'TW'）
    station: 測站代碼（如 'NACB'）
    starttime: 開始時間（UTCDateTime 格式）
    duration: 持續時間（秒）
    
    Returns:
    stream: ObsPy Stream 物件
    """
    client = Client("IRIS")
    
    endtime = starttime + duration
    
    stream = client.get_waveforms(
        network=network,
        station=station,
        location="*",
        channel="BH*",  # 寬頻地震儀
        starttime=starttime,
        endtime=endtime
    )
    
    return stream

# 範例：下載台灣測站數據
starttime = UTCDateTime("2024-04-03T07:58:00")  # 花蓮地震
duration = 600  # 10分鐘

stream = fetch_seismic_data("TW", "NACB", starttime, duration)

# 繪製波形
stream.plot()
```

**4.2 反重力工作流程：從數據到知識**
```python
def research_workflow_antigravity_style(raw_data):
    """
    「反重力」研究工作流程：
    顛覆傳統線性流程，採用迭代式探索
    
    傳統流程（重力下落）:
    假設 → 實驗 → 分析 → 結論
    
    反重力流程（循環上升）:
    數據探索 ⇄ 假設生成 ⇄ 驗證迭代 ⇄ 知識提煉
    
    注意：這是概念框架示範
    各個函數需要根據具體研究問題實現
    """
    
    # Step 1: 數據探索（Data Exploration）
    print("=== Step 1: 探索數據特徵 ===")
    # TODO: 學員實現 - 繪製數據圖表、計算基本統計量
    visualize_data(raw_data)  # 繪製波形、頻譜等
    basic_stats = compute_statistics(raw_data)  # 計算均值、標準差等
    
    # Step 2: 生成假設（Hypothesis Generation）
    print("=== Step 2: 基於觀察生成假設 ===")
    # TODO: 學員實現 - 從數據中識別模式
    observations = identify_patterns(raw_data)  # 找出異常、週期等
    hypotheses = generate_hypotheses(observations)  # 形成可測試的假設
    
    # Step 3: 假設驗證（Hypothesis Testing）
    print("=== Step 3: 驗證假設 ===")
    for hypothesis in hypotheses:
        # TODO: 學員實現 - 設計實驗或分析來驗證假設
        result = test_hypothesis(hypothesis, raw_data)
        if not result.is_valid:
            # 反重力思維：失敗是新假設的起點
            refine_hypothesis(hypothesis, result.feedback)
    
    # Step 4: 知識綜合（Knowledge Synthesis）
    print("=== Step 4: 綜合知識 ===")
    # TODO: 學員實現 - 整合驗證結果
    validated_results = filter_valid_hypotheses(hypotheses)
    final_insights = synthesize_knowledge(validated_results)
    
    # Step 5: 反思與迭代（Reflection and Iteration）
    print("=== Step 5: 反思與下一步 ===")
    # TODO: 學員實現 - 從結果中提出新問題
    new_questions = generate_new_questions(final_insights)
    
    return {
        'insights': final_insights,
        'new_questions': new_questions,
        'raw_analyses': validated_results
    }

# 輔助函數框架（學員需實現）
def visualize_data(data):
    """繪製數據視覺化圖表"""
    pass

def compute_statistics(data):
    """計算基本統計量"""
    pass

def identify_patterns(data):
    """識別數據中的模式"""
    pass

def generate_hypotheses(observations):
    """根據觀察生成假設"""
    pass

def test_hypothesis(hypothesis, data):
    """測試假設"""
    pass

def refine_hypothesis(hypothesis, feedback):
    """根據反饋優化假設"""
    pass

def filter_valid_hypotheses(hypotheses):
    """篩選驗證通過的假設"""
    pass

def synthesize_knowledge(results):
    """綜合分析結果"""
    pass

def generate_new_questions(insights):
    """從洞察中生成新問題"""
    pass

# 教學核心：
# 真實研究很少是線性的
# 「反重力」提醒我們要不斷質疑、迭代、上升
```

**4.3 實戰項目：地震定位系統**
```python
def earthquake_location_project():
    """
    綜合項目：建立簡化版地震定位系統
    
    整合前面所學：
    1. 波速模型（Module 1 & 2）
    2. 走時計算（Module 2）
    3. 反演演算法（Module 3）
    4. 實際數據處理（Module 4）
    
    注意：部分函數需要學員實現
    """
    
    # 1. 準備數據
    # TODO: 學員實現 - 讀取測站資訊和拾取到時
    stations = load_station_info()  # 讀取測站經緯度、高程
    arrival_times = pick_arrival_times(stream)  # 從波形中拾取P波到時
    
    # 2. 建立速度模型
    velocity_model = create_1d_velocity_model(
        depths=[0, 10, 20, 30],
        vp=[5.8, 6.2, 6.8, 7.8],  # km/s
        vs=[3.4, 3.6, 3.9, 4.5]   # km/s
    )
    
    # 3. 地震定位（反問題求解）
    def location_inversion(arrival_times, stations, velocity_model):
        """
        使用網格搜尋或梯度下降法定位震源
        
        最小化目標函數：
        E = Σ(T_obs - T_calc)²
        
        其中 T_calc 為理論走時，需正向計算
        這是「反重力」的完美例子：
        - 正問題：已知震源 → 計算走時
        - 反問題：已知走時 → 推估震源
        """
        
        def misfit(location):
            lat, lon, depth = location
            # TODO: 學員實現 compute_travel_times()
            # 計算震源到各測站的理論走時
            calculated_times = compute_travel_times(
                lat, lon, depth, stations, velocity_model
            )
            residual = np.sum((arrival_times - calculated_times)**2)
            return residual
        
        # 使用scipy優化
        from scipy.optimize import minimize
        
        initial_guess = [24.0, 121.0, 15.0]  # 初始猜測
        result = minimize(misfit, initial_guess, method='Nelder-Mead')
        
        return result.x  # 最佳震源位置
    
    best_location = location_inversion(arrival_times, stations, velocity_model)
    
    print(f"震央位置: ({best_location[0]:.4f}°N, {best_location[1]:.4f}°E)")
    print(f"震源深度: {best_location[2]:.2f} km")
    
    # 4. 不確定性分析
    # TODO: 學員實現 - 使用 Bootstrap 方法估計誤差
    uncertainty = bootstrap_uncertainty(arrival_times, stations, velocity_model)
    
    # 5. 視覺化結果
    # TODO: 學員實現 - 繪製震央位置圖
    plot_earthquake_location(best_location, stations, uncertainty)
    
    return best_location, uncertainty

# 輔助函數框架（學員需實現）
def load_station_info():
    """讀取測站資訊（經緯度、高程）"""
    # 提示：可從文件讀取或硬編碼測站資訊
    pass

def pick_arrival_times(stream):
    """從波形中拾取到時"""
    # 提示：可使用 STA/LTA 或其他方法自動拾取
    pass

def compute_travel_times(lat, lon, depth, stations, velocity_model):
    """計算理論走時"""
    # 提示：使用射線追蹤或簡化的線性速度模型
    pass

def bootstrap_uncertainty(arrival_times, stations, velocity_model):
    """Bootstrap 不確定性分析"""
    # 提示：重複抽樣並重新定位，計算標準差
    pass

def plot_earthquake_location(location, stations, uncertainty):
    """視覺化地震定位結果"""
    # 提示：使用 matplotlib 或 cartopy 繪製地圖
    pass

def create_1d_velocity_model(depths, vp, vs):
    """建立一維速度模型"""
    return {'depths': depths, 'vp': vp, 'vs': vs}

# 執行項目（示範）
# location, uncertainty = earthquake_location_project()
```

#### 實作練習:
- **任務1**: 完成地震定位系統的完整實現
- **任務2**: 處理至少 3 筆真實地震事件
- **任務3**: 撰寫研究報告，包含方法、結果與討論

---

## 🔬 研究方法論訓練
## Research Methodology Training

### 反重力研究法則 (Antigravity Research Principles)

1. **質疑常規 (Question Conventions)**
   - 不盲從既有文獻
   - 從不同角度檢視問題
   - 編程實驗驗證理論

2. **迭代精進 (Iterative Refinement)**
   ```python
   def scientific_method_loop():
       while not converged:
           observation = collect_data()
           hypothesis = formulate_hypothesis(observation)
           prediction = make_prediction(hypothesis)
           experiment = design_experiment(prediction)
           result = run_experiment(experiment)
           
           if result.matches(prediction):
               refine_hypothesis(hypothesis, result)
           else:
               # 反重力時刻：失敗引導新發現
               new_direction = analyze_discrepancy(result, prediction)
               pivot_research(new_direction)
   ```

3. **開放協作 (Open Collaboration)**
   - 程式碼開源分享
   - 數據公開透明
   - 鼓勵同儕審查

---

## 📊 評量方式
## Assessment Methods

### 1. 編程作業 (40%)
- 每週編程練習
- 代碼品質、註解完整度
- 演算法效率

### 2. 研究專案 (40%)
- 獨立研究題目選定
- 方法論正確性
- 結果分析深度
- 報告撰寫品質

### 3. 課堂參與 (20%)
- 討論積極度
- 問題解決能力
- 協助同學程度

---

## 📖 教材與資源
## Teaching Materials and Resources

### 必備教材 (Required Materials)

1. **程式語言**
   - Python 3.8+ (主要語言)
   - 必備套件：NumPy, SciPy, Matplotlib, ObsPy

2. **線上資源**
   - [ObsPy Tutorial](https://docs.obspy.org/tutorial/)
   - [IRIS DMC](https://ds.iris.edu/ds/nodes/dmc/)
   - 本知識庫現有資源：
     - [地震波物理特性](seismic_waves.md)
     - [應力應變分析](stress_strain.md)
     - [重力測量技術](gravity_meters.md)

3. **參考書籍**
   - Stein & Wysession. *An Introduction to Seismology, Earthquakes, and Earth Structure*
   - Aki & Richards. *Quantitative Seismology* (進階)
   - Shearer. *Introduction to Seismology*

### 延伸資源 (Extended Resources)

4. **研究論文資源**
   - 參考本知識庫 [NTU 地震實驗室論文摘要集](papersummaries/NTU_Seismo_Lab_Full_PDF_List.md)
   - 重點論文：
     - [震源機制快速判定](papersummaries/ntu_seismo_lab_papers/Review_003_1998_Wu_Quick_Magnitude.md)
     - [地震預警系統](papersummaries/ntu_seismo_lab_papers/Review_004_1999_Wu_Integrated_EEW_Hualien.md)

5. **數據來源**
   - 中央氣象署地震測報中心
   - IRIS Data Management Center
   - 本知識庫即時數據：
     - [NACB 測站即時波形](seismic_waveforms/realtime_viewer.html)
     - [地震事件記錄](earthquake_data/)

---

## 🎓 學習成果
## Learning Outcomes

完成本課程後，學員將具備：

### 知識面 (Knowledge)
- ✅ 深入理解地震學基本原理
- ✅ 掌握波動理論與應力分析
- ✅ 熟悉地球內部結構與地震機制

### 技能面 (Skills)
- ✅ 獨立編寫地震數據分析程式
- ✅ 實施反演演算法解決地球物理問題
- ✅ 處理與視覺化大規模地震數據

### 思維面 (Mindset)
- ✅ 培養「反重力」批判性思維
- ✅ 具備從數據中提煉知識的能力
- ✅ 勇於挑戰傳統方法，創新研究途徑

---

## 🚀 課程特色
## Unique Features

### 1. 概念創新
- 首創「反重力」隱喻教學法
- 突破傳統地震學教學框架
- 強調反向思維與問題求解

### 2. 實作導向
- 每堂課皆包含編程實作
- 使用真實地震數據
- 鼓勵學員開發個人工具

### 3. 研究整合
- 連結本知識庫豐富資源
- 參考前沿研究論文
- 培養學員獨立研究能力

### 4. 開源精神
- 所有教材程式碼開源
- 鼓勵學員貢獻改進
- 建立學習社群

---

## 📅 課程時程建議
## Suggested Course Schedule

### 16週課程規劃 (16-Week Plan)

| 週次 | 主題 | 內容概要 |
|-----|------|---------|
| 1-2 | 重力與反重力基礎 | 重力理論、絕對重力儀、異常反演 |
| 3-4 | 波動理論 | P波/S波、波動方程、數值模擬 |
| 5-6 | 反時偏移與成像 | 波場延拓、反向傳播、地下成像 |
| 7-8 | 應力應變分析 | 應力張量、彈性理論、莫爾圓 |
| 9-10 | 震源機制解 | 斷層參數、初動極性、反演演算法 |
| 11-12 | 數據處理實務 | ObsPy、IRIS數據、訊號處理 |
| 13-14 | 地震定位系統 | 走時計算、網格搜尋、優化演算法 |
| 15-16 | 研究專案發表 | 學員專案展示、同儕審查、總結 |

---

## 💡 實施建議
## Implementation Recommendations

### 教學環境
1. **硬體需求**
   - 每位學員配備電腦（支援 Python 開發）
   - 網路穩定（需下載地震數據）
   - 選配：大螢幕用於數據視覺化展示

2. **軟體環境**
   ```bash
   # 建議使用 Conda 環境管理
   conda create -n seismology python=3.10
   conda activate seismology
   
   # 安裝必要套件
   conda install numpy scipy matplotlib pandas
   pip install obspy
   pip install cartopy  # 地圖繪製
   ```

### 教學方法
1. **翻轉教室**
   - 課前：學員自學理論、閱讀程式碼
   - 課中：討論疑惑、實作練習、專題演講
   - 課後：完成編程作業、撰寫學習筆記

2. **專題導向學習 (Project-Based Learning)**
   - 每 4 週一個小專題
   - 最後 4 週獨立研究專案
   - 鼓勵跨組協作

3. **程式碼審查 (Code Review)**
   - 學員互相檢視程式碼
   - 培養程式品質意識
   - 學習他人優秀實踐

---

## 🌟 預期影響
## Expected Impact

### 對學員
- 建立扎實的地震學知識基礎
- 獲得實用的編程與數據分析技能
- 培養創新思維與研究能力

### 對領域
- 推廣程式化地震學教育
- 培養下一代地球物理學家
- 促進開源科學文化

### 對社會
- 提升大眾對地震科學的理解
- 培養具備災害意識的公民
- 促進科學與技術結合

---

## 📧 聯絡資訊
## Contact Information

本提案歡迎各界建議與合作機會。

**知識庫維護**: OpenClaw AI Agent  
**相關資源**: https://github.com/cwbdayi638/knowledge  
**即時數據**: [NACB 測站波形監測](https://cwbdayi638.github.io/knowledge/seismic_waveforms/realtime_viewer.html)

---

## 📝 結語
## Conclusion

「反重力」不僅是物理學的有趣概念，更是一種教學哲學。在地震學研究中，我們始終在進行「反向工程」——從地表的觀測反推地下的真實。透過編程，我們能具體實現這些反演演算法；透過實作，我們培養解決複雜問題的能力。

本提案期望能啟發學習者，不僅學習地震學知識，更習得一種「反重力思維」：質疑常規、勇於創新、持續進步。就如同反重力讓物體違反常理上升，我們也期待學員在知識與思維上不斷「向上」提升。

---

*本提案由 SeismoProphet 知識庫團隊提出*  
*文件版本: v1.0*  
*最後更新: 2026-02-08*
