import requests

BASE_URL = "https://ai-backend-ndil.onrender.com"

def generate_prompt(user_id: str, query: str):
    response = requests.post(f"{BASE_URL}/generate", json={
        "user_id": user_id,
        "query": query
    })
    return response.json()

def get_history(user_id: str):
    response = requests.get(f"{BASE_URL}/history", params={"user_id": user_id})
    return response.json()
