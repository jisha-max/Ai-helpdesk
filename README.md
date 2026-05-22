# 🤖 GenAI Academic Helpdesk

An AI-powered academic helpdesk system built using Flask, LangChain, ChromaDB, and HuggingFace.

The system uses Retrieval Augmented Generation (RAG) to answer questions from multiple PDF documents such as:
- syllabus
- placement information
- hostel rules
- college circulars

---

#  Features

 Multi-PDF Question Answering  
Semantic Search using Embeddings  
Chroma Vector Database  
RAG Architecture  
Modern Chatbot UI  
Real-time AI Responses  

---

#  Technologies Used

- Python
- Flask
- LangChain
- ChromaDB
- HuggingFace
- Sentence Transformers
- HTML
- CSS
- JavaScript

---

#  Project Structure

```bash
student-ai-helpdesk/
│
├── app.py
├── requirements.txt
├── uploads/
│   ├── syllabus.pdf
│   ├── placement.pdf
│   ├── hostel.pdf
│   └── circular.pdf
│
├── templates/
│   └── index.html
│
├── static/
│   └── style.css
```

---

# Installation

## 1. Clone Repository

```bash
git clone https://github.com/jisha-max/student-ai-helpdesk.git
```

---

## 2. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 3. Run Application

```bash
python app.py
```

---

#  Open in Browser

```bash
http://127.0.0.1:5000
```

---

#  Architecture

```text
Multiple PDFs
        ↓
PyPDFLoader
        ↓
Text Chunking
        ↓
Embeddings
        ↓
Chroma Vector DB
        ↓
Retriever
        ↓
LLM
        ↓
Generated Answer
```

---

#  Example Questions

- What is placement eligibility?
- What are hostel rules?
- When do exams start?
- What is library timing?

---

#  How It Works

1. PDFs are loaded using PyPDFLoader
2. Documents are split into chunks
3. Embeddings are created using sentence transformers
4. ChromaDB stores vectors
5. RetrievalQA fetches relevant chunks
6. FLAN-T5 generates answers

---

#  Future Improvements

- Voice Assistant
- Dynamic PDF Upload
- Multi-language Support
- Cloud Deployment

---

#  Developed By

Jisha John  
AIML Trainer
