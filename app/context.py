def build_prompt(messages):

    prompt = """<|system|>
Bạn là trợ lý AI hữu ích, luôn trả lời bằng tiếng Việt.
"""

    for msg in messages:

        if msg["role"] == "user":

            prompt += f"""
<|user|>
{msg["content"]}
"""

        elif msg["role"] == "assistant":

            prompt += f"""
<|assistant|>
{msg["content"]}
"""

    prompt += """
<|assistant|>
"""

    return prompt