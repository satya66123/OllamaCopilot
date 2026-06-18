# OllamaCopilot v1.0

## Overview

OllamaCopilot is a full-stack AI assistant platform built using Python, Streamlit, Ollama, OpenAI, and MySQL. The application supports conversational AI, Retrieval-Augmented Generation (RAG), document search, hybrid retrieval, user authentication, analytics, and administrative management.

The project demonstrates the implementation of modern AI application architecture, including vector search, semantic retrieval, multi-user support, and real-time AI interactions.

ollamaCopilot intrgrated with openai also

---

## Features

### AI Chat Assistant

* Multi-model chat interface
* Ollama integration
* OpenAI integration
* Streaming responses
* Conversation history management

### Retrieval-Augmented Generation (RAG)

* PDF document ingestion
* DOCX document ingestion
* TXT document ingestion
* Automatic text chunking
* Embedding generation
* Vector-based retrieval
* Similarity search
* Source document tracking

### Advanced Search

* Vector Search
* Hybrid Search (Vector + Keyword)
* Re-ranking of retrieved chunks
* User-specific retrieval

### User Management

* User registration
* User login/logout
* Password hashing with bcrypt
* Session management
* User-specific chats
* User-specific documents

### Analytics & Monitoring

* Total chat statistics
* Document statistics
* Latest chat tracking
* User activity monitoring

### Export Features

* TXT Export
* PDF Export
* DOCX Export
* JSON Export

### Administrative Dashboard

* User management
* Total user count
* Total chat count
* Total document count
* System overview

### Web Search

* Dedicated web search interface
* Internet information retrieval

---

## Technology Stack

### Frontend

* Streamlit

### Backend

* Python

### AI Models

* Ollama
* OpenAI

### Database

* MySQL

### AI & NLP

* Embeddings
* Vector Search
* Cosine Similarity
* Retrieval-Augmented Generation (RAG)

### Libraries

* streamlit
* ollama
* openai
* mysql-connector-python
* bcrypt
* numpy
* python-docx
* reportlab
* ddgs

---

## System Architecture

User Interface (Streamlit)

↓

Application Layer

* Chat Module
* RAG Module
* Authentication Module
* Analytics Module
* Admin Module
* Web Search Module

↓

AI Services

* Ollama
* OpenAI

↓

Retrieval Layer

* Chunking
* Embeddings
* Similarity Search
* Hybrid Search
* Re-ranking

↓

Database Layer

* Users
* Chats
* Document Chunks

↓

MySQL

---

## Project Structure

```text
OllamaCopilot/

├── app.py
├── admin.py
├── web_search.py

├── database/
│   ├── db.py
│   ├── vector_db.py
│   └── vector_search.py

├── utils/
│   ├── embeddings.py
│   ├── similarity.py
│   ├── chunker.py
│   └── file_reader.py

├── exports/

├── requirements.txt

└── README.md
```

---

## Installation

### Clone Repository

```bash
git clone https://github.com/your-username/OllamaCopilot.git

cd OllamaCopilot
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Environment

Windows:

```bash
venv\Scripts\activate
```

Linux/Mac:

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Database Setup

Create a MySQL database:

```sql
CREATE DATABASE ollamacopilot;
```

Update database configuration in:

```python
database/db.py
```

---

## Run Application

Main Application:

```bash
streamlit run app.py
```

Admin Dashboard:

```bash
streamlit run admin.py
```

Web Search:

```bash
streamlit run web_search.py
```

---

## Key Achievements

* Built a complete AI assistant platform from scratch
* Implemented Retrieval-Augmented Generation (RAG)
* Developed multi-user authentication and authorization
* Integrated Ollama and OpenAI models
* Designed hybrid search and re-ranking mechanisms
* Implemented document ingestion and semantic retrieval
* Developed administrative dashboard and analytics system
* Added export functionality and streaming AI responses

---

## Future Enhancements

* Docker Support
* CI/CD Pipeline
* Cloud Deployment
* Multi-Agent Architecture
* Knowledge Graph Integration
* Advanced RAG Optimization
* Voice Assistant Integration

---

## Version

Current Version: v1.0

---

## Author

Satya Srinath Nekkanti

AI Engineer | Python Developer | Generative AI Enthusiast
