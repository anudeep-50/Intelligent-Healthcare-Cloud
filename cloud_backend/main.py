# main.py - The Central Hub
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

@app.get("/")
def home():
    return {"status": "Healthcare Cloud System Online"}

# This is where Member A will send data
@app.post("/ingest")
def receive_data(data: dict):
    # Member C will add ECC decryption here
    # Member B will call the AI Model here
    return {"message": "Data processed", "analysis": "GREEN"}
