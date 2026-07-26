from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
from langchain_community.embeddings import OpenAIEmbeddings
from langchain_community.vectorstores import Chroma

app = FastAPI()

# Configuration
VECTOR_DB_PATH = "./chroma_db"

class Query(BaseModel):
    text: str

@app.post("/retrieve/")
async def retrieve_context(query: Query):
    try:
        embeddings = OpenAIEmbeddings()
        vectorstore = Chroma(persist_directory=VECTOR_DB_PATH, embedding_function=embeddings)
        
        # Perform similarity search
        docs = vectorstore.similarity_search(query.text, k=4)
        
        context = "\n\n".join([doc.page_content for doc in docs])
        return {"context": context}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
