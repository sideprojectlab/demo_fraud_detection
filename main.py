from fastapi import FastAPI
from pydantic import BaseModel
from pymongo import MongoClient


app = FastAPI()

# Connect to MongoDB 
client = MongoClient(
    "mongodb+srv://<db_username>:<db_password>@cluster0.8tyqkcr.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
)



db = client["fraud_detection"]
blocked_merchants = db["blocked_merchants"]

# Pydantic model for request body
class Transaction(BaseModel):
    user_id: str
    upi_id: str
    amount: float

# API endpoint
@app.post("/process_transaction")
def process_transaction(txn: Transaction):
    # Check if UPI ID is in blocked list
    blocked = blocked_merchants.find_one({"upi_id": txn.upi_id})
    if blocked:
        return {
            "status": "blocked",
            "reason": blocked["reason"],
            "upi_id": txn.upi_id
        }
    
    return {
        "status": "approved",
        "upi_id": txn.upi_id,
        "amount": txn.amount
    }
