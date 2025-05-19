import pandas as pd

df = pd.read_csv('led_wafer_with_voltage_as_measured.csv')

df['Radius_mm'] = (df['X_mm']**2 + df['Y_mm']**2)**(1/2)

def classify_region(r):
    if r <= 20:
        return 'Center'
    elif r <= 40:
        return 'Mid'
    else:
        return 'Edge'
df['region'] = df['Radius_mm'].apply(classify_region)

df.to_csv('led_wafer_with_voltage_as_measured_with_region.csv', index=False)