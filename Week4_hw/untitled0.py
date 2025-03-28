from PIL import Image

def raw_to_png(raw_path, width, height, output_path):
    # raw 파일 읽기
    with open(raw_path, 'rb') as f:
        raw_data = f.read()

    # 픽셀 수와 길이 비교
    if len(raw_data) < width * height:
        raise ValueError("파일 크기가 이미지 크기보다 작습니다.")

    # Pillow의 Image 객체 만들기 ("L"은 흑백 모드)
    img = Image.frombytes('L', (width, height), raw_data)

    # PNG로 저장
    img.save(output_path)
    print(f"이미지 저장 완료: {output_path}")
raw_to_png("dd.raw", 400, 500, "uje.png")
img = Image.open("renoir01.gif")
print(img.size)  # (가로, 세로)