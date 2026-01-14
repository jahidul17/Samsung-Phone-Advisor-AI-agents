## 📱 Samsung Phone Advisor – RAG & Multi-Agent System

This project implements a smart assistant designed to help users make informed decisions when buying Samsung smartphones. The system combines **Retrieval-Augmented Generation (RAG)** with a **multi-agent architecture** to deliver both accurate specifications and natural-language reviews or recommendations.

Samsung phone data (20–30 models) is scraped from **GSMArena** and stored in a **PostgreSQL** database, including specifications such as display, battery, camera, RAM, storage, release date, and price. Users interact with the system through natural-language queries like phone comparisons, best-value recommendations, or detailed specs.

### 🔧 System Architecture

- **RAG Module** – Retrieves structured phone specifications from PostgreSQL  
- **Agent 1: Data Extractor** – Fetches relevant phone data based on the user query  
- **Agent 2: Review Generator** – Produces comparisons and recommendations in natural language  
- **Response Composer** – Unifies factual data and generated insights into a final answer  

### ⚙️ Tech Stack

- **langchain** 
- **langgraph** 
- **google-generativeai** 
- **fastapi** 
- **uvicorn** 
- **sqlalchemy** 
- **psycopg2-binary**

### 🚀 API Access

All interactions are handled through a single FastAPI endpoint:

## Setup Instructions

1. **Clone the repository**
    ```bash
    git clone https://github.com/jahidul17/Samsung-Phone-Advisor-AI-agents.git
    cd Samsung-Phone-Advisor-AI-agents/samsung_advisor
    ```

2. **Create and activate a virtual environment:**
    ```bash
    python -m venv venv
    # On Windows
    venv\Scripts\activate
    # On macOS/Linux
    source venv/bin/activate
    ```

3. **Install dependencies**
    ```bash
    pip install -r requirements.txt
    ```
4. **Create a .env file in the project root and add:**
    ```bash
    DATABASE_URL=postgresql://postgres:your_password@localhost:5432/database

    GOOGLE_API_KEY=your_google_api_key_here
    ```
5. **Run the Scraper From the project root:**
    ```bash
    python scraper.py
    ```
6. **Run the FastAPI Server**
    ```bash
    uvicorn main:app --reload
    ```
7. **Server will start at:**
    ```bash
    http://127.0.0.1:8000
  
    http://127.0.0.1:8000/docs
  
   ```
