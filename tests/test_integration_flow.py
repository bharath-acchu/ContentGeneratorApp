import pytest
from httpx import AsyncClient, ASGITransport
from backend.main import app
from unittest.mock import patch

@pytest.mark.asyncio
@patch("backend.ai_engine.model.generate_content")
async def test_generate_and_history(mock_generate):
    mock_generate.return_value.text = "Mocked Gemini Response"
    user_id = "test_user"
    query = "What is machine learning?"

    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        # Test POST /generate
        gen_res = await ac.post("/generate", json={"user_id": user_id, "query": query})
        assert gen_res.status_code == 200
        gen_data = gen_res.json()
        assert "casual_response" in gen_data
        assert "formal_response" in gen_data

        # Test GET /history
        hist_res = await ac.get(f"/history?user_id={user_id}")
        assert hist_res.status_code == 200
        history = hist_res.json()
        assert any(h["query"] == query for h in history)
