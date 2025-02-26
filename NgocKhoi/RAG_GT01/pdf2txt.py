import PyPDF2

def extract_text_from_pdf(pdf_path):
    text = ""
    with open(pdf_path, 'rb') as file:  # Mở file PDF ở chế độ đọc nhị phân ('rb')
        reader = PyPDF2.PdfReader(file)
        for page in reader.pages:
            text += page.extract_text()
    return text

# Đường dẫn đến file PDF của bạn
pdf_file = "data\luatgtdb.pdf"

# Trích xuất văn bản
text = extract_text_from_pdf(pdf_file)

# Lưu văn bản vào file TXT
with open("output.txt", "w", encoding="utf-8") as outfile:  # Lưu ý encoding='utf-8'
    outfile.write(text)

print("Văn bản đã được trích xuất và lưu vào output.txt")