import os
import csv

# Linear fit function (from 교수님 힌트)
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

    return slope, intercept, r_squared

# 분석 함수
def analyze_csv(filepath):
    results = []
    with open(filepath, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    header = lines[0].strip().split(',')

    outer_values = sorted(set(line.split(',')[2] for line in lines[1:]))

    for outer_value in outer_values:
        x_vals, y_vals = [], []
        for line in lines[1:]:
            parts = line.strip().split(',')
            if parts[2] == outer_value:
                x_vals.append(float(parts[3]))
                y_vals.append(float(parts[4]))

        slope, intercept, r_squared = linear_fit(x_vals, y_vals)
        eq_str = f"V = {slope:.6f}*I + {intercept:.2e}"

        # 콘솔 출력
        print(f"\nPattern: {parts[0]}, Inner: {parts[1]}μm, Outer: {outer_value}μm")
        print(f"  ➤ Slope(R)       : {slope:.6f} (V/A)")
        print(f"  ➤ Intercept      : {intercept:.2e}")
        print(f"  ➤ R²             : {r_squared:.5f}")
        print(f"  ➤ Fitting Eq.    : {eq_str}")

        results.append([parts[0], parts[1], outer_value, f"{slope:.6f}", f"{r_squared:.5f}", eq_str])

    return results

# 메인
def main():
    filepath = input("CSV 파일 경로를 입력하세요: ").strip().strip('"')
    if not os.path.exists(filepath):
        print("파일이 존재하지 않습니다.")
        return

    results = analyze_csv(filepath)

    # CSV 저장
    out_path = os.path.splitext(filepath)[0] + '_analysis.csv'
    with open(out_path, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(["Pattern", "Inner Circle (um)", "Outer Circle (um)", "Slope (V/A)", "R²", "Equation"])
        writer.writerows(results)

    print(f"\n분석 결과가 {out_path} 에 저장되었습니다.")

if __name__ == "__main__":
    main()
