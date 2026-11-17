
import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()


def generate_answer(question: str):
    api_key = os.getenv("LLM_API_KEY")

    if not api_key:
        raise ValueError("LLM_API_KEY is missing from .env")

    client = OpenAI(
        api_key=api_key,
        base_url=os.getenv(
            "LLM_BASE_URL",
            "https://api.groq.com/openai/v1"
        )
    )

    response = client.chat.completions.create(
        model=os.getenv(
            "LLM_MODEL",
            "llama-3.3-70b-versatile"
        ),
        messages=[
            {
                "role": "system",
                "content": "You are a helpful AI study assistant."
            },
            {
                "role": "user",
                "content": question
            }
        ]
    )

    return response.choices[0].message.content
