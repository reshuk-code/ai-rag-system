from fastapi import FastAPI, UploadFile, File, HTTPException
from langchain_community.document_loaders import TextLoader, PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.embeddings import OpenAIEmbeddings
from langchain_community.vectorstores import Chroma
import os

app = FastAPI()

# Configuration
VECTOR_DB_PATH = "./chroma_db"

@app.post("/ingest/")
async def ingest_document(file: UploadFile = File(...)):
    try:
        # Save the uploaded file temporarily
        file_path = f"./data/{file.filename}"
        with open(file_path, "wb") as f:
            f.write(await file.read())

        # Load document based on type
        if file.filename.endswith(".pdf"):
            loader = PyPDFLoader(file_path)
        elif file.filename.endswith(".txt"):
            loader = TextLoader(file_path)
        else:
            raise HTTPException(status_code=400, detail="Unsupported file type. Only .pdf and .txt are supported.")
        
        documents = loader.load()

        # Split documents
        text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
        splits = text_splitter.split_documents(documents)

        # Create embeddings and store in vector DB
        embeddings = OpenAIEmbeddings()
        vectorstore = Chroma.from_documents(documents=splits, embedding=embeddings, persist_directory=VECTOR_DB_PATH)
        vectorstore.persist()

        os.remove(file_path) # Clean up temporary file

        return {"message": f"Successfully ingested {file.filename}"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

