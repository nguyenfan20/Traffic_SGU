import numpy as np

# Đọc file embeddings
data = np.load("traffic_law_embeddings.npy", allow_pickle=True)

# Kiểm tra dữ liệu
print("Số lượng embeddings:", len(data))
print("Ví dụ một embedding:", data[0])
with open("luat_giao_thong_cleaned.txt", "r", encoding="utf-8") as file:
    documents = [line.strip() for line in file if line.strip()]

print(f"Số lượng văn bản cần nhúng: {len(documents)}")
