# 📘 FastAPI + MongoDB Fraud Detection API — Setup Guide

## 1. Prerequisites
- Install **Python 3.9+**
- Install **Visual Studio Code (VS Code)**
- Have a **MongoDB Atlas cluster** (or local MongoDB) set up

---

## 2. Open Project in VS Code
1. Create a new folder, e.g., `demo_fraud_detection`
2. Open it in VS Code
3. Open the integrated terminal (**Terminal → New Terminal**)

---

## 3. Create Virtual Environment
```bash
python -m venv venv
```
---
4. Install Dependencies

Run in the VS Code terminal:
````
pip install fastapi uvicorn pymongo pydantic
````

(Optional, for file uploads later):
````
pip install python-multipar
````
5. Run the Server

In VS Code terminal:
````
uvicorn main:app --reload
````
Replace the mongoDB username and password with yours 
```
"mongodb+srv://<db_username>:<db_password>@cluster0.8tyqkcr.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
)
```
Create a now data base and data for blocked upi ids nad give them unique ids 



If successful, you’ll see:
```
INFO:     Uvicorn running on http://127.0.0.1:8000
```
