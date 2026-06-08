from langchain_community.llms import LlamaCpp

from context import build_prompt

CONFIG = {
    "temperature": 0.7,
    "max_tokens": 100,
    "top_p": 0.95
}

llm = LlamaCpp(
    model_path="/models/tinyllama.gguf",
    verbose=False,
    **CONFIG
)

history = []

print("===== CHAT DEMO =====")
print("Gõ exit để thoát")

while True:

    question = input("\nUser: ")

    if question.lower() == "exit":
        break

    history.append({
        "role": "user",
        "content": question
    })

    prompt = build_prompt(history)

    answer = llm.invoke(prompt)

    print("\nAssistant:")
    print(answer)

    history.append({
        "role": "assistant",
        "content": answer
    })