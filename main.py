from fastapi import FastAPI
from pydantic import BaseModel
from transformers import pipeline

app = FastAPI(title="ClausePulse API")

# This pipeline integrates your PyTorch model directly into FastAPI
classifier = pipeline(
    "text-classification", 
    model="./contract_risk_model", 
    tokenizer="./contract_risk_model"
)

class ContractRequest(BaseModel):
    text: str

@app.post("/analyze")
async def analyze_contract(request: ContractRequest):
    # Pass the incoming text from the web request to the model
    prediction = classifier(request.text)
    return {
        "status": "success", 
        "results": prediction
    }

@app.get("/health")
async def health_check():
    return {"status": "ClausePulse API is live and model is loaded."}