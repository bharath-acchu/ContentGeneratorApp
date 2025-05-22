import pytest
from backend.ai_engine import chain_prompts, generate_ai_responses
from unittest.mock import patch

def test_chain_prompts_structure():
    result = chain_prompts("casual", "What is quantum computing?")
    assert isinstance(result, str)
    assert len(result) > 0

@patch("backend.ai_engine.model.generate_content")
def test_generate_ai_responses(mock_generate):
    mock_generate.return_value.text = "Mocked Gemini response"
    casual, formal = generate_ai_responses("What is AI?")
    assert casual == "Mocked Gemini response"
    assert formal == "Mocked Gemini response"
