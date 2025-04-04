"""
Created on Mon Mar 31 09:32:00 2025

@author: BaeHun
"""

# 기존 CSV 파일 경로
input_file_path = "C:/Temp/LED_wafer_Processing_summary.csv"
# 새로운 CSV 파일 경로
output_file_path = "C:/Temp/new_LED_wafer_Processing_summary.csv"

with open(input_file_path, "r") as inFp:
    with open(output_file_path, "w") as outFp:
        # 헤더 읽기 및 쓰기
        header = inFp.readline().strip()
        outFp.write(header + '\n')
        
        # 데이터 행 읽기 및 처리
        for inStr in inFp:
            inStr = inStr.strip()
            row_list = inStr.split(',')
            
            for i in range(len(row_list)):
                try:
                    row_list[i] = f"{float(row_list[i]):.4f}"
                except ValueError:
                    pass # 숫자가 아닌 경우는 그대로 두기
            # 변환된 행을 파일에 저장
            row_str = ','.join(row_list)
            outFp.write(row_str + '\n')
print('Save. OK~')