from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
import models
from database import engine, get_db
from agents.agent_orchestrator import ask_ai


models.Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Samsung Phone Advisor is Live!"}

@app.get("/phones")
def read_phones(db: Session = Depends(get_db)):
    return db.query(models.Phone).all()

@app.get("/phone/{model_name}")
def get_phone(model_name: str, db: Session = Depends(get_db)):
    phone = db.query(models.Phone).filter(models.Phone.model_name.ilike(f"%{model_name}%")).first()
    return phone

@app.get("/ask")
async def chat_with_ai(query: str):
    response = ask_ai(query)
    return {"status": "success", "answer": response}

