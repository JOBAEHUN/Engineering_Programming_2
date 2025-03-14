import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter

# 1. 엑셀 파일 읽기
file_path = "200_20.xlsx"  # 엑셀 파일 경로
data = pd.read_excel(file_path)

# 2. 데이터 확인 (Optional)
print(data.head())  # 데이터 구조 확인

# 3. 데이터 처리 및 그래프 그리기
plt.figure(figsize=(10, 6))

# 최대 5개의 Gate Voltage에 대해 반복
for i in range(0, min(data.shape[1], 15), 3):  # 열 인덱스를 3씩 증가 (최대 5개의 세트 = 15열)
    gate_voltage = data.iloc[:, i].dropna().values[0]  # Gate Voltage (고정값, 첫 번째 값만 사용)
    drain_current = data.iloc[:, i + 1].dropna()  # Drain Current (Id)
    drain_voltage = data.iloc[:, i + 2].dropna()  # Drain Voltage (Vd)

    # 그래프 추가 (Drain Current 스케일 조정)
    plt.plot(drain_voltage, drain_current * 1e4, label=f"Vg = {gate_voltage}V")  # Id를 1e4로 변환

# y축 포맷 설정: 소수점 첫째 자리까지만 표시
plt.gca().yaxis.set_major_formatter(FuncFormatter(lambda x, _: f"{x:.1f}"))

# 4. 그래프 꾸미기
plt.title("Output Curve (W/L = 10)")
plt.xlabel("Drain Bias Voltage (Vd) [V]")
plt.ylabel("Drain Current (Id) [10⁻⁴ A]")  # 단위를 10⁻⁴로 표시
plt.legend()
plt.grid(True)
plt.show()
