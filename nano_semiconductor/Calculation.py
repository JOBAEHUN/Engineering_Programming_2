import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress

# 엑셀 파일 로드
file_path = '200_10_Drain=40V.xlsx'  # 엑셀 파일 경로
data = pd.read_excel(file_path)

# 데이터 칼럼 정의 (엑셀 데이터의 컬럼명과 맞게 변경)
Vg = data['GateV'].values  # 게이트 전압 (V)
Id = data['DrainI'].values  # 드레인 전류 (A)

# 1. 데이터 필터링 (Id > 0)
valid_indices = Id > 0  # Id가 양수인 데이터만 선택
Vg = Vg[valid_indices]
Id = Id[valid_indices]

if len(Vg) == 0 or len(Id) == 0:
    raise ValueError("Filtered data contains no valid points. Check your input data.")

# 선형관계를 나타내기 위해 루트 씌움
sqrt_Id = np.sqrt(Id)

# 선형 영역 설정 (필요하면 조정)
linear_region = (Vg > 0.5) & (Vg < 10)
Vg_linear = Vg[linear_region]
sqrt_Id_linear = sqrt_Id[linear_region]

if len(Vg_linear) < 2 or len(sqrt_Id_linear) < 2:
    raise ValueError("Not enough data points in the linear region for Vth calculation.")

slope, intercept, _, _, _ = linregress(Vg_linear, sqrt_Id_linear)
Vth = -intercept / slope



# 3. Subthreshold Swing (SS) 계산
log_Id = np.log10(Id)  # 로그 변환

# Subthreshold 영역 범위 설정 (Vg > Vth 근처로)
subthreshold_region = (Vg > Vth) & (Vg < 5)  # Vg 범위를 Vth 이후로 제한
Vg_sub = Vg[subthreshold_region]
log_Id_sub = log_Id[subthreshold_region]

if len(Vg_sub) < 2 or len(log_Id_sub) < 2:
    raise ValueError("Not enough data points in the Subthreshold region for SS calculation.")

# Subthreshold 영역에서 선형 피팅
sub_slope, _, _, _, _ = linregress(Vg_sub, log_Id_sub)
SS = 1 / sub_slope  # Subthreshold Swing 계산


# 특정 Gate Voltage 범위 선택 (-40V ~ 40V)
range_indices = (Vg >= -40) & (Vg <= 40)  # -40V ≤ Vg ≤ 40V
Vg_range = Vg[range_indices]
Id_range = Id[range_indices]

if len(Vg_range) == 0 or len(Id_range) == 0:
    raise ValueError("No valid points in the specified Vg range for mobility calculation.")

# 4. Mobility (μ) 계산 (Saturation 모드)
# 필요한 상수들 (단위에 주의!)
L = 10e-6  # 채널 길이 (m)
W = 200e-6  # 채널 폭 (m)
Cox = 1.725e-8  # 산화막 단위 면적당 정전 용량 (F/m^2)

# Mobility 계산
mobility = (2 * L * Id_range) / (W * Cox * (Vg_range - Vth)**2)





# 결과 출력
print(f"Threshold Voltage (Vth): {Vth:.2f} V")
print(f"Subthreshold Swing (SS): {SS:.2f} V/dec")
print(f"Mobility (Saturation Mode): {np.mean(mobility):.2e} cm^2/Vs")

# 그래프 (Vth, SS, Mobility)
plt.figure()
plt.plot(Vg, slope * Vg + intercept, 'r-', label=f'Fit: Vth={Vth:.2f} V')
plt.xlabel('Vg (V)')
plt.ylabel('sqrt(Id)')
plt.title('Threshold Voltage Extraction')
plt.legend()
plt.grid()
plt.show()

plt.figure()
plt.plot(Vg, log_Id, 'o', label='Measured log(Id)')
plt.plot(Vg, sub_slope * Vg + intercept, 'r-', label=f'Fit: SS={SS:.2f} V/dec')
plt.xlabel('Vg (V)')
plt.ylabel('log10(Id)')
plt.title('Subthreshold Swing Extraction')
plt.legend()
plt.grid()
plt.show()


plt.figure()
plt.plot(Vg_range, mobility, 'o', label='Mobility')
plt.xlabel('Gate Bias Voltage (V)')
plt.ylabel('Mobility (cm^2/Vs)')
plt.title('Electron Mobility')
plt.legend()
plt.grid()
plt.show()
