from fastapi import FastAPI
from pydantic import BaseModel
from pymongo import MongoClient

# Initialize FastAPI
app = FastAPI()

# Connect to MongoDB (replace credentials with yours)
client = MongoClient(
    "mongodb+srv://Sagato:AKKfvzQZ18ZTYKGn@cluster0.8tyqkcr.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
)


# Use your new database
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
    
    # Otherwise approve
    return {
        "status": "approved",
        "upi_id": txn.upi_id,
        "amount": txn.amount
    }
