from backend.database import Base, engine
from backend.schema import Prompt

Base.metadata.create_all(bind=engine)
print("✅ Database tables created.")
