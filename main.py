from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Contract Risk Analyzer API")

class ContractRequest(BaseModel):
    text: str

@app.post("/analyze")
async def analyze_contract(request: ContractRequest):
    # We will load your Kaggle model here later
    # and pass the request.text through it
    return {"status": "success", "message": "Model integration pending."}

@app.get("/health")
async def health_check():
    return {"status": "API is live"}