# LangChain Function/Tool Calling Calculator

## 1. Tổng quan dự án

Dự án này hướng dẫn cách xây dựng một máy tính đơn giản sử dụng LangChain và Google Generative AI (phiên bản thay thế cho Google Gemini Flash model cũ) để thực hiện các phép toán cơ bản thông qua việc gọi một công cụ (tool) trong cuộc hội thoại. Mục tiêu của dự án là giúp mô hình LLM (Large Language Model) có thể thực hiện các phép tính chính xác bằng cách gọi một hàm tính toán tùy chỉnh.

## 2. Các bước thực hiện chi tiết

### **Bước 1: Cài đặt môi trường**

Yêu cầu cần có Google Colab, API key của Google Generative AI, và cài đặt hai thư viện LangChain và Google Generative AI.

#### **Lệnh cài đặt:**

```bash
pip install --upgrade langchain google-generativeai langchain-google-genai python-dotenv
```

Thiết lập biến môi trường cho API key bằng cách tạo file `.env` và sử dụng thư viện `dotenv` để tải API key vào biến:

```python
import os
from dotenv import load_dotenv

load_dotenv()
GOOGLE_GENERATIVE_API_KEY = os.getenv("GOOGLE_GENERATIVE_API_KEY")
```

### **Bước 2: Xây dựng công cụ tính toán**

Xây dựng lớp `Calculator` với phương thức `calculate()` để xử lý các phép toán cơ bản:

```python
class Calculator:
    def calculate(self, expression: str) -> str:
        try:
            # Sử dụng eval một cách hạn chế built-in để tính toán biểu thức
            result = eval(expression, {"__builtins__": None}, {})
            return str(result)
        except Exception as e:
            return f"Error: {e}"
```

### **Bước 3: Tích hợp công cụ vào LangChain**

Sử dụng decorator `@tool` để định nghĩa công cụ `calculator` giúp thực hiện phép toán:

```python
from langchain.tools import tool

@tool
def calculator(expression: str) -> str:
    """
    Perform arithmetic calculations.
    Input: A mathematical expression as a string (e.g., "2 + 2").
    Output: Result of the calculation as a string.
    """
    calc = Calculator()
    return calc.calculate(expression)
```

### **Bước 4: Cấu hình mô hình Google Generative AI**

Thay vì sử dụng phiên bản cũ của Google Gemini Flash, ta dùng mô hình Google Generative AI hiện đại từ gói `langchain-google-genai`.

```python
from langchain_google_genai import GoogleGenerativeAI

# Khởi tạo mô hình với API key và model hiện hành ("gemini-pro" hay tên model tương ứng)
llm = GoogleGenerativeAI(model="gemini-pro", api_key=GOOGLE_GENERATIVE_API_KEY)
```

Tiếp theo, tích hợp công cụ vào agent bằng cách sử dụng tool-calling:

```python
from langchain.agents import ToolAgent, ToolAgentExecutor

tools = [calculator]
agent = ToolAgent.from_tools_and_llm(tools, llm)
executor = ToolAgentExecutor(agent)
```

### **Bước 5: Xây dựng chuỗi hội thoại**

Sử dụng `ConversationBufferMemory` để duy trì trạng thái hội thoại trong quá trình tương tác:

```python
from langchain.chains import ConversationalChain
from langchain.memory import ConversationBufferMemory

memory = ConversationBufferMemory()  # Bạn có thể tùy chỉnh thêm các tham số nếu cần

chain = ConversationalChain(
    llm=llm,
    agent_executor=executor,
    memory=memory
)
```

### **Bước 6: Kiểm thử công cụ tính toán**

#### **Kiểm tra tính toán đơn giản:**

```python
query = "What is 15 divided by 3?"
response = chain.run(query)
print(response)
```

**Kết quả mong đợi:**

```
"The result of 15 divided by 3 is 5."
```

#### **Kiểm tra với nhiều truy vấn liên tiếp:**

```python
queries = [
    "What is 25 multiplied by 4?",
    "Now divide the result by 5.",
    "Add 10 to that."
]

for q in queries:
    print("Query:", q)
    print("Response:", chain.run(q))
    print("-" * 40)
```

**Kết quả mong đợi:**

```
Query 1: "The result of 25 multiplied by 4 is 100."
Query 2: "The result of dividing 100 by 5 is 20."
Query 3: "Adding 10 to 20 gives 30."
```

## 3. Nâng cấp tùy chọn

Một số cải tiến có thể thực hiện:

- **Mở rộng phép toán:** Hỗ trợ các phép toán phức tạp hơn như logarit, lượng giác, v.v.
- **Xử lý lỗi tốt hơn:** Đưa ra thông báo cụ thể nếu người dùng nhập sai định dạng hoặc phép toán không được hỗ trợ.
- **Tích hợp UI:** Xây dựng giao diện web bằng Streamlit hoặc FastAPI.
- **Ghi log:** Ghi lại dữ liệu đầu vào và đầu ra để hỗ trợ debug hoặc kiểm tra lịch sử thao tác.

## 4. Lợi ích của LangChain Tool-Calling

- **Tính mô-đun:** Dễ dàng mở rộng hoặc thay thế công cụ mà không cần sửa đổi logic cốt lõi.
- **Khả năng tích hợp:** Dễ dàng kết hợp nhiều công cụ vào workflow phức tạp.
- **Gọi hàm linh động:** Mô hình có thể tự động xác định khi nào cần gọi công cụ dựa trên yêu cầu của người dùng.

## 5. Kết luận

Dự án này giúp tạo ra một công cụ tính toán dựa trên LangChain và Google Generative AI, cho phép LLM có thể thực hiện các phép toán chính xác trong hội thoại. Các bước hướng dẫn chi tiết giúp dễ dàng triển khai, mở rộng và tích hợp vào các ứng dụng AI thực tế.