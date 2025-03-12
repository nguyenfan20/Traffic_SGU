# RAG
## Tổng kết buổi 3
## Building a RAG **pipeline**

Mục tiêu của paper này để xây dựng một **RAG (Retrieval Augmented Generation) pipeline** hoản chỉnh và chain bằng GPU.

Việc truy vấn và trả lời được dựa trên file PDF nhất định và được trả lời thông qua **mô hình ngôn ngữ lớn LMM**.

Một vài frameworks được sử dụng trong dự án cụ thể như [*LlamIndex*](https://www.llamaindex.ai/) và *[LangChain](https://www.langchain.com/)*,…

## **What is RAG?**

RAG được viết tắt của cụm từ Retrieval Augmented Generation

Được mô tả chi tiết ở bài báo nghiên cứu sau:  [*Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks*](https://arxiv.org/abs/2005.11401).

Các bước của một mô hình RAG được thực hiện như sau:

- **Retrieval** - Tìm kiếm thông tin liên quan từ một nguồn được đưa ra bởi một truy vấn.
- **Augmented** - Sử dụng thông tin được truy xuất có liên quan để sửa đổi đầu vào thành mô hình tổng quát (ví dụ: LLM).
- **Generation** - Tạo ra câu trả lời từ dữ liệu đầu vào đã được gửi.

## **Why RAG?**

**Mục tiêu chính của RAG là cải thiện hiệu quả đầu ra của LLM**

Hai khía cạnh quan trọng mà RAG có thể cải thiện:

1. **Ngăn chặn** **hallucinations (Ảo giác mô hình):** LLM cung cấp khả năng tạo sinh ngôn ngữ đáng kinh ngạc nhưng chúng dễ gây ra các ảo giác.
2. **Nguồn dữ liệu được tùy chỉnh:** Nhiều LLM được tạo ra với nguồn dữ liệu khổng lồ từ internet. Điều này có nghĩa rằng các LLM có nguồn kiến thức rộng nhưng thiếu chuyên sâu về một lĩnh vực cụ thể hoặc các nguồn tài liệu của công ty. Vì lẽ đó việc tùy ý sử dụng dữ liệu cho việc truy vấn trên RAG là một trong những lợi ích lớn.

## **What kind of problems can RAG be used for?**

RAG là một giải pháp cho việc cung cấp một nguồn truy xuất các dữ liệu mà các LLM không được đào tạo. ( ví dụ: Các nguồn tài liệu bảo mật của công ty, các dữ liệu không được publish trên mạng internet,… )

Các trường hợp ứng dụng mô hình RAG hiệu quả:

- **Hệ thống chăm sóc khách hàng:** Với việc sử dụng các tài liệu chăm sóc khách hàng là một nguồn dữ liệu để truy vấn và truy xuất, hệ thống RAG có thể dựa vào các câu hỏi liên quan của khách hàng và sử dụng LLM để biến tấu cách đoạn trích được truy xuất thành các câu trả lời cho khách hàng. [*Klarna*](https://www.klarna.com/international/press/klarna-ai-assistant-handles-two-thirds-of-customer-service-chats-in-its-first-month/) - Một công ty tài chính lớn trong việc cung cấp hệ thống hỗ trợ khách hàng như trên để kiếm ít nhất 40 triệu USD cho mỗi năm.
- **Một mô hình hỏi đáp tiện ích:** Với việc bạn có một tập dữ liệu text rộng lớn ( ví dụ: các điều khoản của một hợp đồng bảo hiểm ).  Bạn có thể sử dụng mô hình RAG cho việc truy vấn về các bồi thường và điều lệ của hợp đồ một cách nhanh chóng mà không cần biết quá chi tiết về nội dung của tập dữ liệu.