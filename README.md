# HỆ THỐNG HỎI ĐÁP LUẬT GIAO THÔNG VỚI RAG

## 1. Giới Thiệu
Hệ thống này được phát triển nhằm cung cấp một công cụ hỏi đáp tự động về luật giao thông tại Việt Nam, sử dụng kiến trúc Retrieval-Augmented Generation (RAG) kết hợp với ngôn ngữ mô hình lớn (LLM) như LangChain và AI Agent. Mô hình giúp cung cấp câu trả lời chính xác, bám sát luật, giảm nguy cơ sinh ra thông tin sai lệch.

## 2. Mục Tiêu
- Xây dựng hệ thống hỏi đáp tự động dựa trên RAG.
- Tích hợp LangChain và AI Agent để cải thiện chất lượng câu trả lời.
- Tối ưu hiệu suất truy xuất dữ liệu và sinh câu trả lời chính xác.
- Xây dựng giao diện tương tác giúp người dùng dễ hỏi đáp.

## 3. Kiến Trúc Hệ Thống
Hệ thống gồm 3 thành phần chính:

### 3.1. Thu Thập & Xử Lý Dữ Liệu
- Thu thập văn bản luật giao thông từ các nguồn chính thống.
- Xử lý văn bản (đánh dấu, chuẩn hóa, loại bỏ nhiễu).
- Chuyển văn bản thành vector embedding sử dụng PhoBERT hoặc Sentence-BERT.

### 3.2. Triển Khai Mô Hình RAG
- Sử dụng LangChain để triển khai các pipeline truy vấn.
- Vector Database (FAISS, ChromaDB) dùng lưu trữ dữ liệu truy vấn nhanh.
- Kết hợp mô hình ngôn ngữ lớn (LLM) như GPT hoặc LLaMA để sinh câu trả lời.

### 3.3. Giao Diện Hỏi Đáp
- Xây dựng giao diện web dựa trên Flask hoặc FastAPI.
- Tích hợp API truy vấn nhanh.
- Cung cấp chức năng hỏi đáp trực tuyến, gợi ý hỗ trợ người dùng.


## 4. Tổng Kết
Hệ thống RAG hỏi đáp luật giao thông có khả năng cung cấp thông tin nhanh, chính xác và linh hoạt. Các hướng phát triển trong tương lai:
- Cải thiện hiệu suất truy vấn và giảm thiểu sai sót.
- Tích hợp với các hệ thống giao thông thông minh.

## 5. Dự kiến thời gian
- 📝 [Lịch trình](./schedule.md)

## 6. Báo cáo và phân công
- [Google Drive](https://drive.google.com/drive/folders/1jZ8PaC2kOZtapw003d1tmEruziqxs5LA?usp=drive_link)
