from pydantic import BaseModel

class GenerateRequest(BaseModel):
    user_id: str
    query: str
