import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-2.0-flash")

def chain_prompts(prompt_style: str, query: str) -> str:
    if prompt_style == "casual":
        base_prompt = f"Explain in a casual and creative tone: {query}"
        refine_prompt = "Polish the above explanation with more humor and clarity with 300 words."
    else:
        base_prompt = f"Explain in a formal and analytical tone: {query}"
        refine_prompt = "Polish the above explanation for clarity and precision 300 words."

    try:
        base = model.generate_content(base_prompt).text
        refined = model.generate_content(f"{refine_prompt}\n\n{base}").text
        return refined
    except Exception as e:
        return f"Error generating {prompt_style} response: {e}"

def generate_ai_responses(query: str) -> tuple[str, str]:
    casual = chain_prompts("casual", query)
    formal = chain_prompts("formal", query)
    return casual, formal
