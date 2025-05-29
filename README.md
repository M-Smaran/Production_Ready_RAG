# 🔍 Full-Stack Production-Ready RAG System

This repository contains a full-stack, production-ready implementation of a **Retrieval-Augmented Generation (RAG)** system. It allows users to upload documents, ask questions, and receive context-aware AI responses powered by language models and vector search.

---

## 🚀 Features

- 📁 **Document Uploading**: Supports `.pdf`, `.docx
- 🔎 **Semantic Search with Chroma**: Uses ChromaDB for efficient document chunk retrieval.
- 🧠 **Language Model Integration**: Plug-and-play LLM interface via LangChain.
- 🧾 **Chat History**: Tracks conversations with session IDs.
- 🧼 **Document Management**: Upload, list, and delete documents with metadata tracking.
- 🔒 **Environment Config**: Secure `.env` usage for API keys and configurations.
- 🛠️ **Production-ready FastAPI Backend** with ASGI, logging, and modular structure.

---

## 🧩 Tech Stack

| Layer        | Technology            |
|--------------|------------------------|
| Frontend     | [Sublime Text (custom interface or viewer)] |
| Backend      | FastAPI, Uvicorn       |
| LLM Framework| LangChain              |
| Vector DB    | ChromaDB               |
| Document Parsing | Unstructured / PyMuPDF / python-docx |
| Environment  | dotenv (.env)          |
| Logging      | Python logging         |

---

## 📂 Project Structure

python -m venv venv
source venv/bin/activate    # On Windows: venv\Scripts\activate

2. Create a Virtual Environment 
python -m venv venv
source venv/bin/activate    # On Windows: venv\Scripts\activate

3. Install dependencies 
pip install -r requirements.txt

4. Set Environment Variables
OPENAI_API_KEY=your_openai_key
CHROMA_DB_PATH=./chroma_db

5. Run the App
uvicorn main:app --reload
streamlit run streamlit_app.py



