import re


def preprocess_text(text):
    # 1. Loại bỏ ký tự đặc biệt và khoảng trắng thừa
    text = re.sub(r'[^a-zA-Z0-9\s]', '', text)  # Giữ lại chữ cái, chữ số, khoảng trắng
    text = re.sub(r'\s+', ' ', text).strip()  # Thay thế nhiều khoảng trắng bằng 1, bỏ khoảng trắng đầu cuối

    # 2. Loại bỏ dòng trống
    lines = text.splitlines()
    lines = [line for line in lines if line.strip()]  # Bỏ dòng chỉ có khoảng trắng
    text = '\n'.join(lines)

    # 3. Phân đoạn văn bản (ví dụ: theo điều khoản)
    # (Bạn có thể tùy chỉnh cách phân đoạn cho phù hợp với cấu trúc văn bản)
    segments = re.split(r'Điều \d+\.', text)  # Tách theo "Điều 1.", "Điều 2.", ...
    segments = [s.strip() for s in segments if s.strip()]  # Bỏ đoạn trống

    return segments


# Đọc file TXT
with open("output.txt", "r", encoding="utf-8") as file:
    text = file.read()

# Tiền xử lý văn bản
segments = preprocess_text(text)

# Lưu các đoạn văn bản đã xử lý vào file mới (hoặc cơ sở dữ liệu)
with open("luat_giao_thong_da_xu_ly.txt", "w", encoding="utf-8") as outfile:
    for segment in segments:
        outfile.write(segment + "\n\n")  # Mỗi đoạn cách nhau 2 dòng

print("Văn bản đã được tiền xử lý và lưu vào luat_giao_thong_da_xu_ly.txt")