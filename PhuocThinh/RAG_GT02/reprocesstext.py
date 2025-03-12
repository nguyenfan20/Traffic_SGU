import re

def preprocess_text(text):
    # Loại bỏ các dòng chứa "about:blank", số trang, ngày giờ
    text = re.sub(r'about:blank', '', text)  # Xóa cụm từ "about:blank"
    text = re.sub(r'\d+/\d+/\d{2,4},? \d{1,2}:\d{2} (AM|PM)', '', text)  # Xóa ngày tháng
    text = re.sub(r'\d+/\d+', '', text)  # Xóa số trang dạng "4/37"
    
    # Loại bỏ ký tự đặc biệt không cần thiết, giữ lại dấu câu hợp lệ
    text = re.sub(r'[^\w\s.,;:\-\(\)\"\'\’]', '', text)

    # Chuẩn hóa khoảng trắng
    text = re.sub(r'\s+', ' ', text).strip()

    # Tách theo Điều X.
    sections = re.split(r'(?=\bĐiều \d+\.)', text)
    processed_sections = []

    for section in sections:
        if not section.strip():
            continue

        # Lấy số điều luật
        match = re.match(r'(Điều \d+\.)\s*(.*)', section, re.DOTALL)
        if not match:
            continue

        law_number, content = match.groups()

        # Tách khoản (1., 2., 3., ...)
        clauses = re.split(r'(?=\b\d+\.)', content)

        for clause in clauses:
            clause = clause.strip()
            if not clause:
                continue

            # Tách điểm (a), b), c), ...)
            subclauses = re.split(r'(?=\s+[a-z]\))', clause)

            for subclause in subclauses:
                subclause = subclause.strip()
                if subclause:
                    processed_sections.append(f"{law_number} {subclause}")

    return processed_sections

# Đọc file luật giao thông
with open("output.txt", "r", encoding="utf-8") as file:
    raw_text = file.read()
    
# Tiền xử lý văn bản
processed_text = preprocess_text(raw_text)

# Lưu kết quả ra file
with open("luat_giao_thong_cleaned.txt", "w", encoding="utf-8") as file:
    for line in processed_text:
        file.write(line + "\n")

print("Xử lý xong! Dữ liệu đã được tách nhỏ và lưu lại.")
