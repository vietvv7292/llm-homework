from langchain_community.llms import LlamaCpp

CONFIG = {
    "temperature": 0.7,
    "max_tokens": 100,
    "top_p": 0.95
}

llm = LlamaCpp(
    model_path="/models/tinyllama.gguf",
    verbose=True,
    **CONFIG
)

prompt = """
<|system|>
Bạn là trợ lý AI hữu ích.
<|user|>
Xin chào
<|assistant|>
"""

print("===== INPUT =====")
print(prompt)

print("\n===== PARAMETERS =====")
print(CONFIG)

response = llm.invoke(prompt)

print("\n===== OUTPUT =====")
print(response)