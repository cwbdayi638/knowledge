import smtplib
from email.mime.text import MIMEText
from email.header import Header

# 內容撰寫
content = """
應力與應變專題研究 - 系列 4/5：破壞理論與莫耳-庫倫準則

本專題探討岩石如何從穩定的彈性狀態進入不穩定的破壞或滑動狀態。

1. 莫耳圓 (Mohr's Circle) 的應用
莫耳圓是分析二維或三維應力狀態的幾何工具。在岩石力學中，莫耳圓可以用來：
- 表示主應力 (Sigma 1, Sigma 2, Sigma 3) 下的應力分佈。
- 求得任意倾角平面上的正應力 (Sigma_n) 與剪應力 (Tau)。
- 視覺化應力狀態與破壞包絡線之間的關係。

2. 莫耳-庫倫破壞準則 (Mohr-Coulomb Failure Criterion)
這是一個描述脆性材料（如岩石）破壞的線性模型。其數學表達式為：
Tau = C + Sigma_n * tan(phi)
其中：
- Tau: 破壞時的剪應力。
- C: 內聚力 (Cohesion)，代表正應力為零時的岩石強度。
- Sigma_n: 作用在平面上的有效正應力。
- phi: 內摩擦角 (Internal Friction Angle)，tan(phi) 即為摩擦係數。

3. 斷層滑動的決定因素：正應力與剪應力
斷層是否會發生滑動，取決於剪應力與正應力之間的競爭：
- 剪應力 (Shear Stress): 驅動斷層沿其平面滑動的力量。
- 正應力 (Normal Stress): 垂直於斷層面的壓力，會增加斷層面的摩擦阻力，抑制滑動。
- 當剪應力超過「摩擦力 + 內聚力」時，斷層便會發生不穩定滑動（地震）。
- 流體壓力的作用：流體壓力會降低「有效正應力」，使莫耳圓向左移動並縮小，更容易觸碰破壞包絡線，從而引發誘發性地震。

結論：
透過莫耳圓與莫耳-庫倫準則，科學家可以量化評估斷層在特定地應力環境下的穩定性，這對於地震預警與地質工程安全至關重要。
"""

# Email 設定
smtp_server = "smtp.gmail.com"
smtp_port = 587
sender = "cwbdayi@gmail.com"
receiver = "oceanicdayi@gmail.com"
subject = "應力與應變專題研究 (4/5)"
password = "gncgcncvzvnkkitg"

msg = MIMEText(content, 'plain', 'utf-8')
msg['Subject'] = Header(subject, 'utf-8')
msg['From'] = sender
msg['To'] = receiver

try:
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    server.login(sender, password)
    server.sendmail(sender, [receiver], msg.as_string())
    server.quit()
    print("Email sent successfully.")
except Exception as e:
    print(f"Failed to send email: {e}")
