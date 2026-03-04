# 🚦 Vietnamese Traffic Law Q&A System with RAG

[![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python&logoColor=white)](https://www.python.org/)
[![LangChain](https://img.shields.io/badge/LangChain-0.2+-green?logo=chainlink)](https://www.langchain.com/)
[![HuggingFace](https://img.shields.io/badge/HuggingFace-Transformers-yellow?logo=huggingface)](https://huggingface.co/)
[![FAISS](https://img.shields.io/badge/Vector_DB-FAISS-orange)](https://faiss.ai/)
[![License](https://img.shields.io/badge/License-MIT-lightgrey)](LICENSE)

> An intelligent, bilingual (Vietnamese/English) question-answering system for Vietnamese traffic regulations, powered by Retrieval-Augmented Generation (RAG) and a 7B-parameter language model.

---

## 📌 Overview

This project delivers an end-to-end RAG pipeline that allows users to ask natural language questions about Vietnamese traffic law (Nghị định 168/2024/NĐ-CP) and receive accurate, context-grounded answers in real time.

Instead of relying on a general-purpose LLM that may hallucinate legal details, the system **retrieves the most relevant passages** from official legal documents before generating responses — ensuring accuracy and traceability.

---

## ✨ Key Features

- **Domain-specific RAG pipeline** built on LangChain with a Vietnamese-optimized embedding model
- **Semantic search** over a FAISS vector database for fast, accurate document retrieval
- **Quantized LLM inference** (4-bit NF4) using `zephyr-7b-beta` for memory-efficient generation
- **Bilingual prompt routing** — automatically detects Vietnamese vs. English queries
- **Interactive Gradio chatbot UI** for real-time Q&A
- **Automated evaluation framework** measuring Correctness, Relevance, Completeness, and Conciseness
- Supports multiple document formats: **PDF, DOCX, TXT, CSV**

---

## 🏗️ System Architecture

```
User Query
    │
    ▼
┌──────────────────────────────────────────────────┐
│              Language Detection                  │
│          (Vietnamese / English)                  │
└──────────────────────┬───────────────────────────┘
                       │
    ┌──────────────────▼──────────────────┐
    │        Embedding Model              │
    │   (AITeamVN/Vietnamese_Embedding)   │
    └──────────────────┬──────────────────┘
                       │
    ┌──────────────────▼──────────────────┐
    │     FAISS Vector Database           │
    │   (Cosine Similarity Search, k=5)   │
    └──────────────────┬──────────────────┘
                       │ Top-k Chunks
    ┌──────────────────▼──────────────────┐
    │         LLM Reader                  │
    │  (zephyr-7b-beta, 4-bit quantized)  │
    └──────────────────┬──────────────────┘
                       │
                   Final Answer
```

---

## 🛠️ Tech Stack

| Component | Technology |
|---|---|
| **Framework** | LangChain |
| **Embedding Model** | `AITeamVN/Vietnamese_Embedding` (PhoBERT-based) |
| **Language Model** | `HuggingFaceH4/zephyr-7b-beta` |
| **Vector Database** | FAISS (cosine similarity) |
| **Quantization** | BitsAndBytes (4-bit NF4) |
| **UI** | Gradio |
| **Document Parsing** | PyMuPDF, python-docx |
| **Language** | Python 3.10+ |

---

## 📂 Project Structure

```
├── Vietnamese_Legal_Traffic_RAG.ipynb   # Main pipeline notebook
├── luatgt.pdf                           # Source legal document (NĐ 168/2024)
├── test.csv                             # Evaluation Q&A dataset
├── vectordatabase/
│   ├── faiss_index.bin                  # Persisted FAISS index
│   ├── docstore.pkl                     # Document store
│   └── index_to_docstore_id.pkl         # Index mapping
├── rag_evaluation_results.csv           # Evaluation output
├── schedule.md                          # Project timeline
└── README.md
```

---

## 🚀 Getting Started

### Prerequisites

```bash
pip install torch transformers accelerate bitsandbytes \
  langchain langchain-community sentence-transformers \
  faiss-cpu datasets pymupdf python-docx gradio langdetect
```

### Running the Pipeline

1. **Place your legal document** (PDF/DOCX/TXT) in the project root.

2. **Build the vector database** by running the notebook cells up to the *Vector Database* section.

3. **Launch the chatbot UI:**
   ```python
   demo.launch(share=True)
   ```

4. **Run evaluation** against a custom Q&A CSV:
   ```python
   main_evaluation(READER_LLM, loaded_vector_database, "test.csv")
   ```

---

## 📊 Evaluation Results

The system was evaluated on 10 domain-specific questions using a keyword-overlap scoring methodology across four dimensions (scale 1–5):

| Metric | Score Distribution |
|---|---|
| **Correctness** | 9/10 Excellent, 1/10 Good |
| **Relevance** | 8/10 Excellent, 2/10 Good |
| **Completeness** | 10/10 Excellent |
| **Conciseness** | Results at "Good" level — noted for future optimization |

---

## 🔮 Future Improvements

- [ ] Upgrade to a more advanced Vietnamese-native LLM (e.g., Vistral, PhoGPT)
- [ ] Implement re-ranking with cross-encoder models for improved retrieval precision
- [ ] Add multi-document support across multiple legal decrees
- [ ] Replace keyword-overlap evaluation with semantic similarity metrics (BERTScore, ROUGE)
- [ ] Deploy as a REST API (FastAPI) with a production-ready frontend

---

## 📄 Legal Source

This system is built on **Nghị định 168/2024/NĐ-CP** — the Vietnamese Government's decree on administrative penalties for road traffic violations, issued December 26, 2024.

---

## 👥 Team

| Name | Role |
|---|---|
| Phan Tài Nguyên | Project Lead & Report Coordination |
| Nguyễn Ngọc Khôi | Research & Technical Documentation |
| Bùi Trường Thịnh | Prototype Development & Engineering |

---

## 📬 References

- [LangChain Documentation](https://docs.langchain.com/)
- [HuggingFace — zephyr-7b-beta](https://huggingface.co/HuggingFaceH4/zephyr-7b-beta)
- [AITeamVN Vietnamese Embedding](https://huggingface.co/AITeamVN/Vietnamese_Embedding)
- [FAISS by Meta AI](https://faiss.ai/)
