
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from app.llm import generate_answer

app = FastAPI(title="AI Study Assistant API")


class AskRequest(BaseModel):
    question: str = Field(min_length=3, max_length=2000)


@app.get("/")
def home():
    return {"message": "AI Study Assistant API is running"}


@app.post("/ask")
def ask_student(request: AskRequest):
    try:
        answer = generate_answer(request.question)

        return {
            "question": request.question,
            "answer": answer
        }

    except Exception as e:
        print("LLM ERROR:", repr(e))
        raise HTTPException(
            status_code=502,
            detail="LLM service failed"
        )
