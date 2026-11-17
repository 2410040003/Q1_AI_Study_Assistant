
# AI Study Assistant API

## Project Description
An AI-powered Study Assistant API developed using FastAPI.
It accepts student questions and generates answers using an
LLM API.

## Technologies Used
- Python
- FastAPI
- Groq LLM API
- OpenAI Python SDK
- Pytest
- GitHub Actions
- Docker

## Project Structure
Q1_AI_Study_Assistant/
- app/
  - main.py
  - llm.py
- tests/
  - test_main.py
- .github/workflows/
  - tests.yml
- .env
- .env.example
- requirements.txt
- Dockerfile
- .dockerignore
- README.md

## Installation

Create virtual environment:

python -m venv venv

Activate environment:

Windows:
venv\Scripts\activate

Install dependencies:

pip install -r requirements.txt

## Run Application

uvicorn app.main:app --reload

Open:
http://127.0.0.1:8000/docs

## Run Tests

pytest -v

## Docker

Build image:

docker build -t ai-study-assistant .

Run container:

docker run --rm -p 8000:8000 --env-file .env ai-study-assistant

## GitHub Actions

GitHub Actions automatically executes pytest
whenever code is pushed or a pull request is created.

## Author
MLOps Practical Examination Project
