import pdfplumber

def extract_text_from_pdf(pdf_path):
    text = ""
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text += page.extract_text() + "\n"
    return text

pdf_file = "data/luatgtdb.pdf"

text = extract_text_from_pdf(pdf_file)

with open("output.txt", "w", encoding="utf-8") as outfile:
    outfile.write(text)

print("✅ Văn bản đã trích xuất và lưu vào output.txt")
