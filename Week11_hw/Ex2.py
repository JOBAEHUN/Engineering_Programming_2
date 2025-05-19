import pandas as pd

df = pd.read_csv('led_wafer_with_voltage_as_measured_with_region.csv')

grouped = df.groupby(['region', 'Current_mA']).agg({'Voltage_V' : ['mean', 'std'], 'OpticalOutput_mW': ['mean','std']}).reset_index()

grouped.columns = ['region', 'Current_mA', 'Voltage_V_mean', 'Voltage_V_std', 'OpticalOutput_mW', 'OpticalOutput_std']

grouped.to_csv('led_wafer_with_voltage_stats_by_region.csv', index=False)
