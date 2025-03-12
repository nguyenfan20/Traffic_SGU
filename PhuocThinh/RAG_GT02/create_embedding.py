from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings

# Khởi tạo mô hình embeddings
embedding_model = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

with open("luat_giao_thong_cleaned.txt", "r", encoding="utf-8") as file:
    content = file.read()

import re
documents = re.split(r"(?=Điều \d+)", content)  # Tách theo điều luật
documents = [doc.strip() for doc in documents if doc.strip()]  # Loại bỏ dòng trống


# Tạo FAISS VectorStore từ embeddings
vector_store = FAISS.from_texts(documents, embedding_model)

# Lưu FAISS
vector_store.save_local("faiss_traffic_law")
print("✅ Đã lưu embeddings vào FAISS!")
