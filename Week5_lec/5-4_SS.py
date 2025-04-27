# 기존 CSV 파일 경로
input_file_path = "E:/MyPythonProject/Week5_lec/LED_wafer_Processing_summary.csv"
# 새로운 CSV 파일 경로
output_file_path = "E:/MyPythonProject/Week5_lec/new_LED_wafer_Processing_summary.csv"

# 선택할 열 이름
selected_columns = ["Wafer_Number", "Vf_mean", "Pop", "EQE_mean", "Wavelength_mean"]

with open(input_file_path, "r") as inFp:
    with open(output_file_path, "w") as outFp:
        # 헤더 읽기
        header = inFp.readline().strip()
        header_list = header.split(',')

        # 선택된 열 인덱스 찾기
        selected_indices = [header_list.index(col) for col in selected_columns]

        # 새로운 헤더 쓰기
        new_header = ','.join([header_list[idx] for idx in selected_indices])
        outFp.write(new_header + '\n')
        
        # 데이터 행 읽고 필터링해서 저장
        for inStr in inFp:
            inStr = inStr.strip()
            row_list = inStr.split(',')
            try:
                # 선택된 열만 골라서
                new_row = [f"{float(row_list[idx]):.4f}" if row_list[idx].replace('.','',1).isdigit() else row_list[idx]
                           for idx in selected_indices]
            except IndexError:
                continue  # 혹시 비어있는 줄이 있으면 패스

            row_str = ','.join(new_row)
            outFp.write(row_str + '\n')

print('Save. OK~')
