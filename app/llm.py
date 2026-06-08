from langchain_community.llms import LlamaCpp

CONFIG = {
    "temperature": 0.1,
    "max_tokens": 80,
    "top_p": 0.9
}

llm = LlamaCpp(
    model_path="/models/tinyllama.gguf",
    verbose=False,
    stop=["<|user|>", "<|system|>"],
    **CONFIG
)


def get_llm():
    return llm