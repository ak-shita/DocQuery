![Banner](./rag.png)

# 📄 PDF Query RAG

<div align="center">

**A hands-on RAG (Retrieval-Augmented Generation) application that transforms PDF documents into queryable knowledge bases**

[![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://www.python.org/)
[![LangChain](https://img.shields.io/badge/LangChain-0.1+-green.svg)](https://www.langchain.com/)
[![OpenAI](https://img.shields.io/badge/OpenAI-GPT--4o--mini-purple.svg)](https://openai.com/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.104+-teal.svg)](https://fastapi.tiangolo.com/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.28+-red.svg)](https://streamlit.io/)

*Perfect for learning RAG, LangChain, and LLM-powered document interactions*

</div>

---

## 🎯 What is This Project?

This is a **complete RAG application** that demonstrates how to build an intelligent system that:

- Uploads and processes PDF documents
- Extracts and chunks text intelligently
- Creates semantic embeddings for document search
- Answers questions using retrieved context from PDFs
- Returns human-friendly answers based on document content

**Perfect for students learning:**

- 🤖 Retrieval-Augmented Generation (RAG)
- 🔗 LangChain framework
- 💬 LLM prompt engineering
- 📄 PDF processing and text extraction
- 🔍 Vector embeddings and similarity search
- 🌐 Building full-stack AI applications

---

## ✨ Key Features

| Feature | Description |
|---------|-------------|
| 📄 **PDF Processing** | Automatic text extraction and intelligent chunking |
| 🧠 **Semantic Search** | Powered by OpenAI embeddings and FAISS vector store |
| 💬 **Context-Aware Answers** | Uses GPT models with retrieved context from documents |
| 🎨 **Dual Interface** | Both Streamlit web UI and FastAPI REST API |
| 🔄 **RAG Pipeline** | Complete RAG implementation with LangChain |
| ⚡ **Real-time Processing** | Upload and query documents instantly |
| 🚀 **Production Ready** | Modular architecture, error handling, and best practices |

---

## 🏗️ Architecture Overview

```
┌─────────────────┐
│   PDF Upload    │  User uploads a PDF document
└────────┬────────┘
         │
         ▼
┌─────────────────────────────────────┐
│      PDF Processing Pipeline         │
│  ┌───────────────────────────────┐  │
│  │  1. Extract text from PDF     │  │
│  └──────────────┬────────────────┘  │
│                 │                    │
│  ┌──────────────▼────────────────┐  │
│  │  2. Split into chunks         │  │
│  └──────────────┬────────────────┘  │
│                 │                    │
│  ┌──────────────▼────────────────┐  │
│  │  3. Create embeddings         │  │
│  │     and build vector store    │  │
│  └──────────────┬────────────────┘  │
└─────────────────┼────────────────────┘
                  │
                  ▼
         ┌────────────────┐
         │  User Query    │  "What is the main topic?"
         └────────┬───────┘
                  │
                  ▼
┌─────────────────────────────────────┐
│      LangChain RAG Pipeline         │
│  ┌───────────────────────────────┐  │
│  │  1. Embed query and search    │  │
│  │     for relevant chunks       │  │
│  └──────────────┬────────────────┘  │
│                 │                    │
│  ┌──────────────▼────────────────┐  │
│  │  2. Retrieve top-k chunks     │  │
│  └──────────────┬────────────────┘  │
│                 │                    │
│  ┌──────────────▼────────────────┐  │
│  │  3. LLM generates answer      │  │
│  │     using retrieved context   │  │
│  └──────────────┬────────────────┘  │
└─────────────────┼────────────────────┘
                  │
                  ▼
         ┌────────────────┐
         │  User-friendly │
         │     Answer     │
         └────────────────┘
```

---

## 🛠️ Tech Stack

<div align="center">

| Category | Technology | Purpose |
|----------|-----------|---------|
| **🤖 AI/ML** | LangChain | RAG pipeline orchestration |
| | OpenAI GPT-4o-mini | LLM for answer generation |
| | Sentence Transformers | Local embeddings (all-MiniLM-L6-v2) |
| **🌐 Backend** | FastAPI | REST API server |
| **💻 Frontend** | Streamlit | Interactive web interface |
| **🗄️ Vector Store** | FAISS | Efficient similarity search |
| **📄 PDF Processing** | PyPDF | PDF text extraction |
| **⚙️ Tools** | uv | Fast Python package manager |
| | Python 3.10+ | Programming language |

</div>

---

## 📦 Project Structure

```
rag-pdf-python/
├── backend/
│   ├── __init__.py
│   └── main.py              # 🚀 FastAPI REST endpoints
│
├── frontend/
│   ├── __init__.py
│   └── app.py               # 🎨 Streamlit web interface
│
├── shared/
│   ├── __init__.py
│   ├── config.py            # ⚙️ Configuration & environment variables
│   ├── pdf_processor.py     # 📄 PDF extraction & chunking
│   ├── vector_store.py      # 🔍 FAISS vector store management
│   └── rag.py               # 🧠 RAG query engine
│
├── uploads/                 # 📁 Uploaded PDFs directory (auto-created)
├── pyproject.toml           # 📋 Dependencies & project config
├── uv.lock                  # 🔒 Dependency lock file
└── README.md
```

---

## 🚀 Quick Start

### Prerequisites

- **Python 3.10+** installed
- **OpenAI API Key** ([Get one here](https://platform.openai.com/api-keys))
- **uv** package manager (we'll install it if needed)

### Installation Steps

#### 1️⃣ Install uv (if needed)

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

#### 2️⃣ Clone and Navigate

```bash
git clone https://github.com/JaimeLucena/rag-pdf-python.git
cd rag-pdf-python
```

#### 3️⃣ Install Dependencies

```bash
uv sync
```

This will create a virtual environment and install all required packages.

#### 4️⃣ Configure Environment

Create a `.env` file in the root directory:

```bash
OPENAI_API_KEY=sk-your-api-key-here
OPENAI_MODEL=gpt-4-turbo-preview
EMBEDDING_MODEL=text-embedding-3-small
CHUNK_SIZE=1000
CHUNK_OVERLAP=200
```

> 💡 **Tip**: Never commit your `.env` file! It's already in `.gitignore`

---

## 🎮 Usage

### Step 1: Start the Backend

Launch the FastAPI backend server:

```bash
uv run uvicorn backend.main:app --host localhost --port 8000 --reload
```

The API will be available at **http://localhost:8000**

- 📚 Interactive docs: **http://localhost:8000/docs**
- 📖 ReDoc: **http://localhost:8000/redoc**

### Step 2: Start the Frontend

In a new terminal, launch the Streamlit web interface:

```bash
uv run streamlit run frontend/app.py
```

The web UI will automatically open in your browser at **http://localhost:8501**

**Features:**

- 💬 Chat interface for natural language queries
- 📄 Drag & drop PDF upload
- 🎨 Clean, modern UI
- 📝 Chat history
- ✅ Real-time processing status

### Option 3: Use the REST API Directly

You can also interact with the API directly using HTTP requests:

#### Upload a PDF

```bash
curl -X POST "http://localhost:8000/upload" \
  -H "Content-Type: multipart/form-data" \
  -F "file=@document.pdf"
```

**Response:**

```json
{
  "message": "PDF uploaded and processed successfully",
  "chunks": 42,
  "filename": "document.pdf"
}
```

#### Query the Document

```bash
curl -X POST "http://localhost:8000/query" \
  -H "Content-Type: application/json" \
  -d '{"question": "What is the main topic of this document?"}'
```

**Response:**

```json
{
  "answer": "The main topic of this document is..."
}
```

#### Health Check

```bash
curl http://localhost:8000/health
```

**Response:**

```json
{
  "status": "healthy"
}
```

---

## 💡 Example Questions

Try asking these questions after uploading a PDF:

### Basic Queries

- `"What is this document about?"`
- `"Summarize the main points"`
- `"What are the key findings?"`
- `"List the main topics"`

### Specific Information

- `"What is mentioned about [topic]?"`
- `"Who are the authors?"`
- `"What are the conclusions?"`
- `"What methodology was used?"`

### Detailed Queries

- `"Explain the process described in the document"`
- `"What are the recommendations?"`
- `"What data or statistics are mentioned?"`
- `"What are the limitations discussed?"`

---

## 🧠 How RAG Works Here

### Step-by-Step Process

1. **PDF Upload** → User uploads a PDF document

   ```
   document.pdf uploaded
   ```

2. **Text Extraction** → Extract all text from PDF pages

   ```
   Extracted 15,000 characters from 10 pages
   ```

3. **Chunking** → Split text into overlapping chunks

   ```
   Created 42 chunks of ~1000 characters each
   ```

4. **Embedding** → Create vector embeddings for each chunk

   ```
   Generated 42 embeddings using sentence transformers
   ```

5. **Vector Store** → Build FAISS index for similarity search

   ```
   FAISS index created with 42 vectors
   ```

6. **Query Processing** → User asks a question

   ```
   "What is the main topic?"
   ```

7. **Retrieval** → Find most relevant chunks

   ```
   Retrieved top 5 chunks with highest similarity
   ```

8. **Generation** → LLM generates answer using context

   ```
   "Based on the document, the main topic is..."
   ```

### Key Components

- **`shared/pdf_processor.py`**: PDF text extraction and chunking
  - Extracts text from PDF pages
  - Intelligent chunking with sentence boundaries
  - Configurable chunk size and overlap

- **`shared/vector_store.py`**: Vector embeddings and search
  - FAISS index for fast similarity search
  - Sentence transformer embeddings
  - Top-k retrieval

- **`shared/rag.py`**: RAG query engine
  - Combines retrieval and generation
  - Context-aware prompt engineering
  - OpenAI GPT integration

---

## 📊 Configuration

You can customize the application behavior through environment variables:

| Variable | Description | Default |
|----------|-------------|---------|
| `OPENAI_API_KEY` | Your OpenAI API key | Required |
| `OPENAI_MODEL` | GPT model for answers | `gpt-4-turbo-preview` |
| `EMBEDDING_MODEL` | Model for embeddings | `text-embedding-3-small` |
| `CHUNK_SIZE` | Text chunk size | `1000` |
| `CHUNK_OVERLAP` | Overlap between chunks | `200` |

---

## 🎓 Learning Objectives

By exploring this project, you'll learn:

✅ **RAG Fundamentals**

- How to combine retrieval (vector search) with generation (LLM)
- Building end-to-end RAG pipelines
- Context-aware answer generation

✅ **LangChain Patterns**

- Creating custom chains
- Prompt engineering
- LLM integration

✅ **Vector Embeddings**

- Creating document embeddings
- Similarity search with FAISS
- Retrieval strategies

✅ **PDF Processing**

- Text extraction from PDFs
- Intelligent text chunking
- Handling different document formats

✅ **Full-Stack AI Apps**

- Building APIs for AI services
- Creating interactive UIs
- Managing state and sessions

✅ **Best Practices**

- Modular code organization
- Environment configuration
- Error handling
- Type hints and documentation

---

## 🔧 Development

### Running Tests

```bash
uv run pytest
```

### Code Formatting

```bash
uv run ruff format .
uv run ruff check .
```

---

## 🤔 Common Questions

**Q: Why FAISS instead of other vector databases?**  

A: FAISS is perfect for learning - it's fast, in-memory, and requires no setup. For production with persistence, consider Pinecone, Weaviate, or Qdrant.

**Q: Can I use a different LLM?**  

A: Yes! LangChain supports many providers. Just change the LLM initialization in `shared/rag.py` and update your API key.

**Q: How do I persist the vector store?**  

A: The `VectorStore` class has `save()` and `load()` methods. You can modify the backend to persist embeddings between sessions.

**Q: Is this production-ready?**  

A: This is a learning project. For production, add authentication, rate limiting, logging, monitoring, and persistent vector storage.

**Q: What PDF formats are supported?**  

A: Currently supports standard PDFs with extractable text. Scanned PDFs (images) would require OCR preprocessing.

---

## 📚 Additional Resources

- [LangChain Documentation](https://python.langchain.com/)
- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [Streamlit Documentation](https://docs.streamlit.io/)
- [OpenAI API Reference](https://platform.openai.com/docs/)
- [FAISS Documentation](https://github.com/facebookresearch/faiss)
- [RAG Paper (Original)](https://arxiv.org/abs/2005.11401)

---

## 📝 License

MIT License - see [LICENSE](LICENSE) file for details

---

## 🙏 Acknowledgments

Built with ❤️ for students learning AI and generative models.

**Happy Learning! 🚀**

---

<div align="center">

**Made with** ❤️ **for the AI learning community**

⭐ **Star this repo if you found it helpful!**

</div>
