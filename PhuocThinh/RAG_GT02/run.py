from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings  

# 🚀 Load FAISS đã lưu
embedding_model = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
vector_store = FAISS.load_local("faiss_traffic_law", embeddings=embedding_model, allow_dangerous_deserialization=True)

def search_traffic_law(query):
    """Tìm kiếm điều luật gần nhất với câu hỏi của người dùng"""
    results = vector_store.similarity_search(query, k=3)  # Tìm 3 điều luật gần nhất
    
    print("\n🔍 Kết quả tìm kiếm:")
    for i, result in enumerate(results):
        print(f"\n🔹 Kết quả {i+1}:")
        print(result.page_content)  

# 📌 Chạy tìm kiếm theo truy vấn người dùng
while True:
    query = input("\nNhập câu hỏi về luật giao thông ('exit' để thoát): ")
    if query.lower() == "exit":
        break
    search_traffic_law(query)
