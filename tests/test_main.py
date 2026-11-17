
from fastapi.testclient import TestClient
from app.main import app
import app.main as main_module

client = TestClient(app)


# Test 1: Successful question and answer
def test_ask_success(monkeypatch):

    def mock_llm(question):
        return "Photosynthesis is the process by which plants make food."

    monkeypatch.setattr(
        main_module,
        "generate_answer",
        mock_llm
    )

    response = client.post(
        "/ask",
        json={"question": "What is photosynthesis?"}
    )

    assert response.status_code == 200
    assert response.json()["question"] == "What is photosynthesis?"
    assert response.json()["answer"] == (
        "Photosynthesis is the process by which plants make food."
    )


# Test 2: Invalid question
def test_invalid_question():

    response = client.post(
        "/ask",
        json={"question": " " }
    )

    assert response.status_code == 422
