import os
import tkinter as tk
from tkinter import filedialog, ttk
import matplotlib.pyplot as plt

# Linear fit function (with no rounding on R^2, limit to 5 digits without rounding)
def linear_fit(x_vals, y_vals):
    n = len(x_vals)
    sum_x = sum(x_vals)
    sum_y = sum(y_vals)
    sum_xx = sum(x * x for x in x_vals)
    sum_xy = sum(x * y for x, y in zip(x_vals, y_vals))

    slope = (n * sum_xy - sum_x * sum_y) / (n * sum_xx - sum_x ** 2)
    intercept = (sum_y - slope * sum_x) / n

    mean_y = sum_y / n
    ss_tot = sum((y - mean_y) ** 2 for y in y_vals)
    ss_res = sum((y - (slope * x + intercept)) ** 2 for x, y in zip(x_vals, y_vals))
    r_squared = 1 - ss_res / ss_tot if ss_tot != 0 else 0

    return slope, intercept, str(r_squared)[:str(r_squared).find('.') + 6]

# Main analysis function for a single CSV file
def analyze_csv(filepath):
    results = []
    with open(filepath, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    header = lines[0].strip().split(',')
    for outer_value in sorted(set(line.split(',')[2] for line in lines[1:])):
        x_vals, y_vals = [], []
        for line in lines[1:]:
            parts = line.strip().split(',')
            if parts[2] == outer_value:
                x_vals.append(float(parts[3]))
                y_vals.append(float(parts[4]))

        slope, intercept, r_squared = linear_fit(x_vals, y_vals)
        eq_str = f"V = {slope:.6f}*I + {intercept:.2e}"
        result = [parts[0], parts[1], outer_value, f"{slope:.6f}", r_squared, eq_str]
        results.append(result)
    return results

# GUI part
def open_and_analyze():
    filepaths = filedialog.askopenfilenames(filetypes=[("CSV files", "*.csv")])
    all_results = []
    for filepath in filepaths:
        results = analyze_csv(filepath)
        all_results.extend(results)

    for row in tree.get_children():
        tree.delete(row)
    for row in all_results:
        tree.insert('', tk.END, values=row)

    result_label.config(text=f"총 {len(filepaths)}개 파일 분석 완료.")

root = tk.Tk()
root.title("TLM IV 분석 워크시트")
root.geometry("800x400")

btn = tk.Button(root, text="CSV 파일 선택 및 분석", command=open_and_analyze)
btn.pack(pady=10)

result_label = tk.Label(root, text="분석 결과가 여기에 표시됩니다.", fg="blue")
result_label.pack()

cols = ["Pattern", "Inner Circle (um)", "Outer Circle (um)", "Slope (V/A)", "R²", "Equation"]
tree = ttk.Treeview(root, columns=cols, show='headings')
for col in cols:
    tree.heading(col, text=col)
    tree.column(col, width=130, anchor="center")
tree.pack(expand=True, fill='both')

root.mainloop()
