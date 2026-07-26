# AI-powered Retrieval-Augmented Generation (RAG) System

This project implements an AI-powered Retrieval-Augmented Generation (RAG) system, demonstrating how to combine information retrieval with large language models (LLMs) to generate more accurate, up-to-date, and contextually relevant responses.

## Features

*   **Data Ingestion**: Ingests unstructured data, processes it, and stores embeddings in a vector database.
*   **Retrieval Service**: Retrieves relevant document chunks based on user queries.
*   **Generation Service**: Uses LLMs to generate grounded responses from retrieved context.
*   **Frontend**: User interface for interacting with the RAG system.

## Technologies Used

*   **Backend**: Python, FastAPI, LangChain, Uvicorn
*   **Vector Database**: ChromaDB
*   **Embedding Models**: Hugging Face Transformers (via LangChain)
*   **LLM**: OpenAI GPT series (via LangChain)
*   **Frontend**: React.js
*   **Containerization**: Docker, Docker Compose

## Setup and Installation

### Prerequisites

*   Docker and Docker Compose
*   Python 3.9+
*   Node.js (for Frontend)
*   OpenAI API Key (for Generation Service)

### Using Docker Compose (Recommended)

1.  Clone the repository:
    ```bash
    git clone https://github.com/your-username/ai-rag-system.git
    cd ai-rag-system
    ```
2.  Create a `.env` file in the `generation-service` directory and add your OpenAI API Key:
    ```
    OPENAI_API_KEY=your_openai_api_key
    ```
3.  Build and run the Docker containers:
    ```bash
    docker-compose up --build
    ```
4.  The frontend will be accessible at `http://localhost:3000`.

### Manual Setup

Refer to the `README.md` files within each service directory for manual setup instructions.

## Project Structure

```
ai-rag-system/
├── ingestion-service/
│   ├── app/
│   │   └── main.py
│   ├── requirements.txt
│   └── Dockerfile
├── retrieval-service/
│   ├── app/
│   │   └── main.py
│   ├── requirements.txt
│   └── Dockerfile
├── generation-service/
│   ├── app/
│   │   └── main.py
│   ├── requirements.txt
│   └── Dockerfile
├── frontend/
│   ├── public/
│   ├── src/
│   │   └── ... (React app)
│   ├── package.json
│   └── Dockerfile
├── data/
│   └── documents/
│       └── ... (raw documents for ingestion)
├── docker-compose.yml
└── README.md
```


*Last automated update: 2026-07-26 03:18:31*

*Last automated update: 2026-07-26 03:18:40*

*Last automated update: 2026-07-26 03:18:49*