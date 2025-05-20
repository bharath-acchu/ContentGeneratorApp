from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from backend.database import SessionLocal
from backend.schema import Prompt
from backend.models import GenerateRequest
from backend.ai_engine import generate_ai_responses

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/generate")
def generate(request: GenerateRequest, db: Session = Depends(get_db)):
    casual, formal = generate_ai_responses(request.query)

    record = Prompt(
        user_id=request.user_id,
        query=request.query,
        casual_response=casual,
        formal_response=formal
    )
    db.add(record)
    db.commit()
    db.refresh(record)

    return {
        "casual_response": casual,
        "formal_response": formal
    }

@app.get("/history")
def get_history(user_id: str, db: Session = Depends(get_db)):
    records = db.query(Prompt).filter(Prompt.user_id == user_id).order_by(Prompt.created_at.desc()).all()
    return [
        {
            "query": r.query,
            "casual_response": r.casual_response,
            "formal_response": r.formal_response,
            "created_at": r.created_at.isoformat()
        }
        for r in records
    ]
