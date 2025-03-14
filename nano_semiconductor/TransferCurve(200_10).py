import pandas as pd
import matplotlib.pyplot as plt

# 1. 엑셀 파일 읽기
file_path = "200_10_Drain=40V.xlsx"  # 엑셀 파일 경로
data = pd.read_excel(file_path)

# 2. Gate Voltage와 Drain Current 데이터 추출
gate_voltage = data['GateV'].dropna()  # Gate Voltage (GateV) 열
drain_current = data['DrainI'].dropna()  # Drain Current (Drain I) 열

# 3. Transfer Curve 그래프 그리기
plt.figure(figsize=(10, 6))
plt.plot(gate_voltage, drain_current, label="Drain Voltage = 40 V")

# 4. 그래프 꾸미기
plt.title("Transfer Curve(W/L = 20)")
plt.xlabel("Gate Bias Voltage (Vg) [V]")
plt.ylabel("Drain Current (Id) [A]")

# 5. Y축 로그 스케일로 설정
plt.yscale('log')

# 6. 그래프 출력
plt.grid(True)
plt.legend()
plt.show()
