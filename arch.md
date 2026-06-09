# System Architecture

User
|
v
Streamlit UI
|
v
Application Layer
|
|-- Chat Module
|-- RAG Module
|-- Admin Module
|-- Authentication Module
|-- Web Search Module
|
v
Business Logic
|
|-- Embeddings
|-- Chunking
|-- Similarity Search
|-- Hybrid Search
|-- Re-ranking
|
v
Database Layer
|
|-- MySQL
|-- Chats
|-- Users
|-- Document Chunks
|
v
AI Layer
|
|-- Ollama
|-- OpenAI
