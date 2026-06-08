from fastapi import FastAPI

from schemas import ChatRequest
from llm import get_llm
from context import build_prompt
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
llm = get_llm()


@app.get("/")
def root():

    return {
        "message": "Chatbot API Running"
    }


@app.post("/chat")
def chat(req: ChatRequest):

    messages = []

    for msg in req.messages:

        messages.append({
            "role": msg.role,
            "content": msg.content
        })

    prompt = build_prompt(messages)

    answer = llm.invoke(prompt)

    return {
        "session_id": req.session_id,
        "answer": answer
    }