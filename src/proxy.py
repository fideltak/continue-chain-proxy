from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
import requests
import os

class ProxyInput(BaseModel):
    query: str
    fullInput: str

class ChainInput(BaseModel):
    query: str
    top_k: int = 4

class ChainChunk(BaseModel):
    content: str
    filename: str
    score: float

class ChainOutput(BaseModel):
    chunks: List[ChainChunk]

app = FastAPI()
chain_server_url =  os.getenv("CHAIN_SERVER_URL")

@app.post("/retrieve")
async def retrieve(item: ProxyInput):
    data = {
        "query": item.fullInput
    }
    res_json = chain_server_search(chain_server_url, ChainInput(**data))
    context_items = []
    for result in ChainOutput(**res_json).chunks:
        context_items.append({
            "name": result.filename,
            "description": result.filename,
            "content": result.content,
        })
    return context_items

def chain_server_search(url: str, data: ChainInput):
    headers ={"Content-Type": "application/json"}
    response = requests.post(url+"/search", json=data.model_dump(), headers=headers)

    if response.status_code >= 400:
        print("Error:", response.status_code, response.text)
    return response.json()