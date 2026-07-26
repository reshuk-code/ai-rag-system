from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from langchain_community.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
import os

app = FastAPI()

# Configuration
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

class GenerationRequest(BaseModel):
    query: str
    context: str

@app.post("/generate/")
async def generate_response(request: GenerationRequest):
    if not OPENAI_API_KEY:
        raise HTTPException(status_code=500, detail="OpenAI API key not configured.")

    try:
        llm = OpenAI(openai_api_key=OPENAI_API_KEY, temperature=0.7)
        
        prompt_template = """Use the following context to answer the question at the end. If you don't know the answer, just say that you don't know, don't try to make up an answer.

Context: {context}

Question: {query}

Helpful Answer:"""
        
        prompt = PromptTemplate(template=prompt_template, input_variables=["context", "query"])
        llm_chain = LLMChain(prompt=prompt, llm=llm)
        
        response = llm_chain.run(context=request.context, query=request.query)
        
        return {"response": response.strip()}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
