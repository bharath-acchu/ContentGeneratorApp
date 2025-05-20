from sqlalchemy import Column, String, Text, DateTime
from backend.database import Base
from datetime import datetime
import uuid

class Prompt(Base):
    __tablename__ = "prompts"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    user_id = Column(String, nullable=False)
    query = Column(Text, nullable=False)
    casual_response = Column(Text)
    formal_response = Column(Text)
    created_at = Column(DateTime, default=datetime.utcnow)
